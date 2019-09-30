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

class CodeModel:

    def __init__(self):
        self.client_name = None
        self.api_version = None
        self.schemas = None

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
            sorted_schemas.extend(ancestors)
        self.schemas = sorted_schemas

    def add_inheritance_to_models(self, and_schemas) -> None:
        for and_schema in and_schemas:
            if and_schema.get('allOf') and len(and_schema['allOf']) > 1 and and_schema['allOf'][0]['$key'] != and_schema['allOf'][1]['$key']:
                schema = [s for s in self.schemas if s.name == and_schema['language']['default']['name']][0]
                schema.base_model = [s for s in self.schemas if s.name == and_schema['allOf'][1]['language']['default']['name']][0]
