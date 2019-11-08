# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import logging
from typing import List, Dict

from .base_schema import BaseSchema
from .dictionary_schema import DictionarySchema
from .enum_schema import EnumSchema
from .imports import FileImport, ImportType
from .operation_group import OperationGroup


_LOGGER = logging.getLogger(__name__)


class CodeModel:

    def __init__(self):
        self.client_name = None
        self.api_version = None
        self.description = None
        self.schemas: Dict[int, BaseSchema] = {}
        self.sorted_schemas: List[BaseSchema] = []
        self.enums: Dict[int, EnumSchema] = []
        self.primitives: Dict[int, BaseSchema] = {}
        self.namespace = None
        self.operation_groups: List[OperationGroup] = []

    def lookup_schema(self, schema_id):
        for attr in [self.schemas, self.enums, self.primitives]:
            for elt_key, elt_value in attr.items():
                if schema_id == elt_key:
                    return elt_value
        raise KeyError("Didn't find it!!!!!")

    def imports(self):
        file_import = FileImport()
        file_import.add_from_import("msrest.serialization", "Model", ImportType.AZURECORE)
        if len([s for s in self.schemas.values() if s.is_exception]) > 0:
            file_import.add_from_import("azure.core.exceptions", "HttpResponseError", ImportType.AZURECORE)
        return file_import

    def sort_schemas(self):
        seen_schemas = set()
        sorted_schemas = []
        for schema in sorted(self.schemas.values(), key=lambda x: x.name):
            if schema.name in seen_schemas:
                continue
            ancestors = []
            current = schema
            ancestors.append(schema)
            while current.base_model:
                parent = current.base_model
                if parent.name in seen_schemas:
                    break
                ancestors.insert(0, parent)
                seen_schemas.add(current.name)
                current = parent
            seen_schemas.add(current.name)
            sorted_schemas += ancestors
        self.sorted_schemas = sorted_schemas

    def _add_properties_from_inheritance(self):
        for schema in self.schemas.values():
            if schema.base_model:
                parent = schema.base_model
                while parent:
                    schema.properties = parent.properties + schema.properties
                    seen_properties = set()
                    schema.properties = [p for p in schema.properties if p.name not in seen_properties and not seen_properties.add(p.name)]
                    parent = parent.base_model

    def add_inheritance_to_models(self) -> None:
        for schema in self.schemas.values():
            if schema.base_model:
                # right now, the base model property just holds the name of the parent class
                schema.base_model = [b for b in self.schemas.values() if b.id == schema.base_model][0]
        self._add_properties_from_inheritance()

    def add_schema_link_to_operation(self) -> None:
        # Index schemas
        for operation_group in self.operation_groups:
            for operation in operation_group.operations:
                for obj in operation.parameters + operation.responses + operation.exceptions:
                    schema_obj = obj.schema
                    if schema_obj:
                        schema_obj_id = id(obj.schema)
                        _LOGGER.info("Looking for id %s (%s) for member %s of operation %s", schema_obj_id, schema_obj, obj, operation.name)
                        try:
                            obj.schema = self.lookup_schema(schema_obj_id)
                        except KeyError:
                            _LOGGER.critical("Unable to ref the object")
