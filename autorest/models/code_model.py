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

from .dictionary_schema import DictionarySchema
from .enum_schema import EnumSchema
from .imports import FileImport, ImportType

class CodeModel:

    def __init__(self):
        self.client_name = None
        self.api_version = None
        self.description = None
        self.schemas = None
        self.enums = None
        self.namespace = None


    def imports(self):
        file_import = FileImport()
        file_import.add_from_import("msrest.serialization", "Model", ImportType.AZURECORE)
        if len([s for s in self.schemas if s.is_exception]) > 0:
            file_import.add_from_import("azure.core.exceptions", "HttpResponseError", ImportType.AZURECORE)
        return file_import

    def build_enums(self):
        enums = []
        for schema in self.schemas:
            for prop in schema.properties:
                if isinstance(prop, EnumSchema):
                    enums.append(prop)
        self.enums = enums

    def sort_schemas(self):
        seen_schemas = set()
        sorted_schemas = []
        for schema in sorted(self.schemas, key=lambda x: x.name):
            if schema in seen_schemas:
                continue
            ancestors = []
            current = schema
            ancestors.append(schema)
            while current.base_model:
                parent = current.base_model
                if parent.name in seen_schemas:
                    break
                ancestors.insert(0, parent)
                seen_schemas.add(current)
                current = parent
            seen_schemas.add(current)
            sorted_schemas += ancestors
        self.schemas = sorted_schemas

    def _add_properties_from_inheritance(self):
        for schema in self.schemas:
            if schema.base_model:
                parent = schema.base_model
                while parent:
                    schema.properties = parent.properties + schema.properties
                    seen_properties = set()
                    schema.properties = [p for p in schema.properties if p.name not in seen_properties and not seen_properties.add(p.name)]
                    parent = parent.base_model

    def add_inheritance_to_models(self) -> None:
        for schema in self.schemas:
            if schema.base_model:
                # right now, the base model property just holds the id of the parent class
                schema.base_model = [b for b in self.schemas if b.id == schema.base_model][0]
        self._add_properties_from_inheritance()

    def add_additional_properties_to_models(self) -> None:
        for schema in self.schemas:
            if schema.has_additional_properties:
                # checking to see if there's already an additional_properties in the schema's properties.
                    # If so, we name it additional_properties_1
                for prop in schema.properties:
                    if prop.name == 'additional_properties':
                        prop.name = 'additional_properties1'
                schema.properties.insert(0, DictionarySchema.create_additional_properties_dict())
