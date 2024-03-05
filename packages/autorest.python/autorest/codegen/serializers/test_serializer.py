# pylint: disable=too-many-lines
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, Any, List, Optional
from jinja2 import Environment

from .import_serializer import FileImportSerializer
from .base_serializer import BaseSerializer
from ..models import (
    CodeModel,
    ImportType,
    OperationGroup,
    Client,
    OperationType,
    ModelType,
    BaseType,
    CombinedType,
)
from .utils import get_namespace_from_package_name, json_dumps_template


class TestName:
    def __init__(self, client_name: str, *, is_async: bool = False) -> None:
        self.client_name = client_name
        self.is_async = is_async

    @property
    def async_suffix_capt(self) -> str:
        return "Async" if self.is_async else ""

    @property
    def create_client_name(self) -> str:
        return "create_async_client" if self.is_async else "create_client"

    @property
    def prefix(self) -> str:
        return self.client_name.replace("Client", "")

    @property
    def preparer_name(self) -> str:
        return self.prefix + "Preparer"

    @property
    def base_test_class_name(self) -> str:
        return f"{self.client_name}TestBase{self.async_suffix_capt}"


class TestCase:
    def __init__(
        self,
        operation_groups: List[OperationGroup],
        params: Dict[str, Any],
        operation: OperationType,
        *,
        is_async: bool = False,
    ) -> None:
        self.operation_groups = operation_groups
        self.params = params
        self.operation = operation
        self.is_async = is_async

    @property
    def operation_group_prefix(self) -> str:
        if self.operation_groups[-1].is_mixin:
            return ""
        return "." + ".".join([og.property_name for og in self.operation_groups])

    @property
    def response(self) -> str:
        if self.is_async:
            if self.operation.operation_type == "lropaging":
                return "response = await (await "
            return "response = await "
        return "response = "

    @property
    def lro_comment(self) -> str:
        return " # poll until service return final result"

    @property
    def operation_suffix(self) -> str:
        if self.operation.operation_type == "lropaging":
            extra = ")" if self.is_async else ""
            return f"{extra}.result(){self.lro_comment}"
        return ""

    @property
    def extra_operation(self) -> str:
        if self.is_async:
            if self.operation.operation_type == "lro":
                return f"result = await response.result(){self.lro_comment}"
            if self.operation.operation_type == ("lropaging", "paging"):
                return "result = [r async for r in response]"
        else:
            if self.operation.operation_type == "lro":
                return f"result = response.result(){self.lro_comment}"
            if self.operation.operation_type in ("lropaging", "paging"):
                return "result = [r for r in response]"
        return ""


class Test(TestName):
    def __init__(
        self,
        client_name: str,
        operation_group: OperationGroup,
        testcases: List[TestCase],
        test_class_name: str,
        *,
        is_async: bool = False,
    ) -> None:
        super().__init__(client_name, is_async=is_async)
        self.operation_group = operation_group
        self.testcases = testcases
        self.test_class_name = test_class_name


class TestGeneralSerializer(BaseSerializer):
    def __init__(
        self, code_model: CodeModel, env: Environment, *, is_async: bool = False
    ) -> None:
        super().__init__(code_model, env)
        self.is_async = is_async

    @property
    def aio_str(self) -> str:
        return ".aio" if self.is_async else ""

    @property
    def test_names(self) -> List[TestName]:
        return [
            TestName(c.name, is_async=self.is_async) for c in self.code_model.clients
        ]

    @property
    def import_clients(self) -> FileImportSerializer:
        imports = self.init_file_import()
        namespace = get_namespace_from_package_name(
            self.code_model.options["package_name"]
        )

        imports.add_submodule_import(
            "devtools_testutils", "AzureRecordedTestCase", ImportType.STDLIB
        )
        if not self.is_async:
            imports.add_import("functools", ImportType.STDLIB)
            imports.add_submodule_import(
                "devtools_testutils", "PowerShellPreparer", ImportType.STDLIB
            )
        for client in self.code_model.clients:
            imports.add_submodule_import(
                namespace + self.aio_str, client.name, ImportType.STDLIB
            )
        return FileImportSerializer(imports, self.is_async)

    def serialize_conftest(self) -> str:
        return self.env.get_template("conftest.py.jinja2").render(
            test_names=self.test_names,
            code_model=self.code_model,
        )

    def serialize_testpreparer(self) -> str:
        return self.env.get_template("testpreparer.py.jinja2").render(
            test_names=self.test_names,
            imports=self.import_clients,
            code_model=self.code_model,
        )


class TestSerializer(TestGeneralSerializer):
    def __init__(
        self,
        code_model: CodeModel,
        env: Environment,
        *,
        client: Client,
        operation_group: OperationGroup,
        is_async: bool = False,
    ) -> None:
        super().__init__(code_model, env, is_async=is_async)
        self.client = client
        self.operation_group = operation_group

    @property
    def import_test(self) -> FileImportSerializer:
        imports = self.init_file_import()
        test_name = TestName(self.client.name, is_async=self.is_async)
        async_suffix = "_async" if self.is_async else ""
        imports.add_submodule_import(
            "testpreparer" + async_suffix,
            test_name.base_test_class_name,
            ImportType.LOCAL,
        )
        imports.add_submodule_import(
            "testpreparer", test_name.preparer_name, ImportType.LOCAL
        )
        imports.add_submodule_import(
            "devtools_testutils" + self.aio_str,
            "recorded_by_proxy" + async_suffix,
            ImportType.LOCAL,
        )
        return FileImportSerializer(imports, self.is_async)

    @property
    def breadth_search_operation_group(self) -> List[List[OperationGroup]]:
        result = []
        queue = [[self.operation_group]]
        while queue:
            current = queue.pop(0)
            if current[-1].operations:
                result.append(current)
            if current[-1].operation_groups:
                queue.extend([current + [og] for og in current[-1].operation_groups])
        return result

    def get_sub_type(self, param_type: ModelType) -> ModelType:
        if param_type.discriminated_subtypes:
            for item in param_type.discriminated_subtypes.values():
                return self.get_sub_type(item)
        return param_type

    def get_model_type(self, param_type: BaseType) -> Optional[ModelType]:
        if isinstance(param_type, ModelType):
            return param_type
        if isinstance(param_type, CombinedType):
            return param_type.target_model_subtype((ModelType,))
        return None

    def get_operation_params(self, operation: OperationType) -> Dict[str, Any]:
        operation_params = {}
        required_params = [p for p in operation.parameters.method if not p.optional]
        for param in required_params:
            model_type = self.get_model_type(param.type)
            param_type = self.get_sub_type(model_type) if model_type else param.type
            operation_params[param.client_name] = json_dumps_template(
                param_type.get_json_template_representation(for_test=True)
            )
        return operation_params

    def get_test(self) -> Test:
        testcases = []
        for operation_groups in self.breadth_search_operation_group:
            for operation in operation_groups[-1].operations:
                if operation.internal or operation.is_lro_initial_operation:
                    continue
                operation_params = self.get_operation_params(operation)
                testcase = TestCase(
                    operation_groups=operation_groups,
                    params=operation_params,
                    operation=operation,
                    is_async=self.is_async,
                )
                testcases.append(testcase)
        if not testcases:
            raise Exception(  # pylint: disable=broad-exception-raised
                "no public operation to test"
            )

        return Test(
            client_name=self.client.name,
            operation_group=self.operation_group,
            testcases=testcases,
            test_class_name=self.test_class_name,
            is_async=self.is_async,
        )

    @property
    def test_class_name(self) -> str:
        test_name = TestName(self.client.name, is_async=self.is_async)
        class_name = (
            "" if self.operation_group.is_mixin else self.operation_group.class_name
        )
        return f"Test{test_name.prefix}{class_name}{test_name.async_suffix_capt}"

    def serialize_test(self) -> str:
        return self.env.get_template("test.py.jinja2").render(
            imports=self.import_test,
            code_model=self.code_model,
            test=self.get_test(),
        )
