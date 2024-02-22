# pylint: disable=too-many-lines
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, Any, Optional, List
from jinja2 import Environment

from .import_serializer import FileImportSerializer
from .base_serializer import BaseSerializer
from ..models import (
    CodeModel,
    ImportType,
    OperationGroup,
    FileImport,
    Client,
    OperationType,
)
from .builder_serializer import _json_dumps_template
from .utils import get_namespace_from_package_name

class TestName:
    def __init__(self, client_name: str) -> None:
        self.client_name = client_name

    @property
    def prefix(self) -> str:
        return self.client_name.replace("Client", "")

    @property
    def preparer_name(self) -> str:
        return self.prefix + "Preparer"

    @property
    def base_test_class_name(self) -> str:
        return self.client_name + "TestBase"


class TestOperation:
    def __init__(
        self,
        operation_groups: List[OperationGroup],
        params: Dict[str, Any],
        operation: OperationType,
    ) -> None:
        self.operation_groups = operation_groups
        self.params = params
        self.operation = operation

    @property
    def operation_group_prefix(self) -> str:
        if self.operation_groups[-1].is_mixin:
            return ""
        return "." + ".".join([og.property_name for og in self.operation_groups])

    @property
    def extra_operation(self) -> str:
        lro = "result = response.result()"
        paging = "result = list(response)"
        lropaging = "result = list(response.result())"

        if self.operation.operation_type == "paging":
            return paging
        if self.operation.operation_type == "lro":
            return lro
        if self.operation.operation_type == "lropaging":
            return lropaging
        return ""


class TestOperationGroup(TestName):
    def __init__(
        self,
        client_name: str,
        operation_group: OperationGroup,
        test_operations: List[TestOperation],
    ) -> None:
        super().__init__(client_name)
        self.operation_group = operation_group
        self.test_operations = test_operations

class TestSerializer(BaseSerializer):
    def __init__(
        self,
        code_model: CodeModel,
        env: Environment,
        client: Optional[Client] = None,
        operation_group: Optional[OperationGroup] = None,
    ) -> None:
        super().__init__(code_model, env)
        self.client = client
        self.operation_group = operation_group

    @property
    def import_clients(self) -> FileImportSerializer:
        imports = FileImport(self.code_model)
        namespace = get_namespace_from_package_name(
            self.code_model.options["package_name"]
        )
        for client in self.code_model.clients:
            imports.add_submodule_import(namespace, client.name, ImportType.STDLIB)
        return FileImportSerializer(imports, True)

    @property
    def import_test(self) -> FileImport:
        imports = FileImport(self.code_model)
        test_name = TestName(self.client.name)
        imports.add_submodule_import(
            "testpreparer", test_name.base_test_class_name, ImportType.LOCAL
        )
        imports.add_submodule_import(
            "testpreparer", test_name.preparer_name, ImportType.LOCAL
        )
        return FileImportSerializer(imports, True)

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

    @staticmethod
    def get_operation_params(operation: OperationType) -> Dict[str, Any]:
        operation_params = {}
        required_params = [p for p in operation.parameters.method if not p.optional]
        for param in required_params:
            operation_params[
                param.client_name
            ] = _json_dumps_template(param.type.get_json_template_representation(need_comment=False))
        return operation_params

    def handle_operation_group(self) -> TestOperationGroup:
        test_operations = []
        for operation_groups in self.breadth_search_operation_group:
            for operation in operation_groups[-1].operations:
                if operation.internal or operation.is_lro_initial_operation:
                    continue
                operation_params = self.get_operation_params(operation)
                test_operation = TestOperation(
                    operation_groups=operation_groups,
                    params=operation_params,
                    operation=operation,
                )
                test_operations.append(test_operation)
        if not test_operations:
            raise Exception("no public operation to test")

        return TestOperationGroup(
            self.client.name,
            self.operation_group,
            test_operations,
        )

    @property
    def test_names(self) -> List[TestName]:
        return [TestName(c.name) for c in self.code_model.clients]

    def serialize_test(self) -> str:
        return self.env.get_template("test.py.jinja2").render(
            imports=self.import_test,
            code_model=self.code_model,
            test_operation_group=self.handle_operation_group(),
        )

    def serialize_testpreparer(self) -> str:
        return self.env.get_template("testpreparer.py.jinja2").render(
            test_names=self.test_names,
            imports=self.import_clients,
            code_model=self.code_model,
        )

    def serialize_conftest(self) -> str:
        return self.env.get_template("conftest.py.jinja2").render(
            test_names=self.test_names,
            code_model=self.code_model,
        )
