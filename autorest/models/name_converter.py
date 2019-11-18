import re
from ..common.python_mappings import basic_latin_chars, reserved_words

class NameConverter:

    def __init__(self):
        self.seen_yaml_ids = []

    def _seen_id(self, yaml_id):
        for elt_id in self.seen_yaml_ids:
            if yaml_id == elt_id:
                return True
        self.seen_yaml_ids.append(yaml_id)
        return False

    def convert_yaml_names(self, yaml_code):
        NameConverter._convert_language_default_name(yaml_code)
        yaml_code['info']['python_title'] = NameConverter._to_valid_python_name(yaml_code['info']['title'].replace(" ", ""))
        yaml_code['info']['camel_case_title'] = NameConverter._to_camel_case(yaml_code['info']['title'].replace(" ", ""))
        self._convert_schemas(yaml_code['schemas'])
        self._convert_operation_groups(yaml_code['operationGroups'])
        self._convert_global_parameters(yaml_code['globalParameters'])

    def _convert_global_parameters(self, global_parameters):
        for global_parameter in global_parameters:
            if self._seen_id(id(global_parameter)):
                continue
            NameConverter._convert_language_default_name(global_parameter)


    def _convert_operation_groups(self, operation_groups):
        for operation_group in operation_groups:
            if self._seen_id(id(operation_group)):
                continue
            NameConverter._convert_language_default_name(operation_group, pad_string="Model")
            operation_group['language']['python']['className'] = NameConverter._to_camel_case(operation_group['language']['python']['name'])
            for operation in operation_group['operations']:
                if self._seen_id(id(operation)):
                    continue
                NameConverter._convert_language_default_name(operation, pad_string='Method')
                for exception in operation_group.get('exceptions', []):
                    if self._seen_id(id(exception)):
                        continue
                NameConverter._convert_language_default_name(operation['request'])
                for parameter in operation['request'].get('parameters', []):
                    if self._seen_id(id(parameter)):
                        continue
                    NameConverter._convert_language_default_name(parameter, pad_string="Parameter")
                for response in operation.get('responses', []):
                    if self._seen_id(id(response)):
                        continue
                    NameConverter._convert_language_default_name(response)

    def _convert_schemas(self, schemas):
        for obj in schemas['objects']:
            if self._seen_id(id(obj)):
                continue
            self._convert_object_schema(obj)
        for type_list, schema_yamls in schemas.items():
            for schema in schema_yamls:
                if self._seen_id(id(schema)):
                    continue
                if type_list == 'objects':
                    continue
                if type_list == 'arrays' or type_list == 'arrays':
                    NameConverter._convert_language_default_name(schema)
                    NameConverter._convert_language_default_name(schema['elementType'])
                elif type_list == 'constants':
                    NameConverter._convert_language_default_name(schema)
                    NameConverter._convert_language_default_name(schema['value'])
                    NameConverter._convert_language_default_name(schema['valueType'])
                elif type_list == 'sealedChoices' or type_list == 'choices':
                    self._convert_enum_schema(schema)
                else:
                    NameConverter._convert_language_default_name(schema)

    def _convert_enum_schema(self, schema):
        schema['language']['python'] = dict(schema['language']['default'])
        schema_name = schema['language']['default']['name']
        schema_python_name = schema['language']['python']['name']
        schema_python_name = NameConverter._to_camel_case(schema_name)
        schema['language']['python']['name'] = schema_python_name

        NameConverter._convert_language_default_name(schema['choiceType'])

        for choice in schema['choices']:
            if self._seen_id(id(choice)):
                continue
            NameConverter._convert_language_default_name(choice, pad_string='Enum')

    def _convert_object_schema(self, schema):
        schema['language']['python'] = dict(schema['language']['default'])
        schema_name = schema['language']['default']['name']
        schema_python_name = schema['language']['python']['name']

        schema_python_name = NameConverter._to_camel_case(schema_name)
        schema['language']['python']['name'] = schema_python_name
        for prop in schema.get('properties', []):
            if self._seen_id(id(prop)):
                continue
            NameConverter._convert_language_default_name(schema=prop, pad_string='Property')

    @staticmethod
    def _convert_language_default_name(schema, **kwargs):
        schema['language']['python'] = dict(schema['language']['default'])
        schema_name = schema['language']['default']['name']
        schema_python_name = schema['language']['python']['name']

        schema_python_name = NameConverter._to_valid_python_name(schema_name, **kwargs)
        schema['language']['python']['name'] = schema_python_name


    @staticmethod
    def _to_camel_case(name):
        name_list = re.split('[^a-zA-Z\\d]', name)
        name_list = [s[0].upper() + s[1:] if len(s) > 1 else s.upper()
                            for s in name_list]
        return ''.join(name_list)

    @staticmethod
    def _to_valid_python_name(name, **kwargs):
        pad_string = kwargs.pop('pad_string', "")
        if not name:
            return pad_string
        return NameConverter._to_python_case(
            NameConverter._get_escaped_reserved_name(
                NameConverter._to_valid_name(
                    name.replace('-', '_'), '_'),
                    pad_string
                )
            )

    @staticmethod
    def _to_python_case(name):
        def replace_upper_characters(m):
            match_str = m.group().lower()
            if m.start() > 0 and name[m.start() - 1] == '_':
                # we are good if a '_' already exists
                return match_str
            # the first letter should not have _
            prefix = '_' if m.start() > 0 else ''

            # we will add an extra _ if there are multiple upper case chars together
            next_non_upper_case_char_location = m.start() + len(match_str)
            if (len(match_str) > 2 and len(name) - next_non_upper_case_char_location > 1 and
                name[next_non_upper_case_char_location].isalpha()):

                return prefix + match_str[: len(match_str) - 1] + '_' + match_str[len(match_str) - 1]

            return prefix + match_str

        return re.sub("[A-Z]+", replace_upper_characters, name)

    @staticmethod
    def _get_escaped_reserved_name(name, append_value):
        if name is None:
            raise TypeError("The value for name can not be None")
        if append_value is None:
            raise TypeError("The value for append_value can not be None")
        if name.lower() in reserved_words:
            name += append_value
        return name

    @staticmethod
    def _remove_invalid_characters(name, allowed_characters):
        name = name.replace('[]', 'Sequence')
        valid_string = ''.join([n for n in name if n.isalpha() or n.isdigit() or n in allowed_characters])
        return valid_string

    @staticmethod
    def _to_valid_name(name, allowed_characters):
        correct_name = NameConverter._remove_invalid_characters(name, allowed_characters)

        # here we have an empty string or a string that consists only of invalid characters
        if not correct_name or correct_name[0] in basic_latin_chars.keys():
            ret_name = ""
            for c in name:
                if c in basic_latin_chars.keys():
                    ret_name += basic_latin_chars[c]
                else:
                    ret_name += c
            correct_name = NameConverter._remove_invalid_characters(ret_name, allowed_characters)

        if not correct_name:
            raise ValueError("Property name {} cannot be used as an identifier, as it contains only invalid characters.".format(name))
        return correct_name
