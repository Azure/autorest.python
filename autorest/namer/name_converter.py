# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import re
from enum import Enum
from .python_mappings import basic_latin_chars, reserved_words


class PadType(Enum):
    Model = "Model"
    Method = "Method"
    Parameter = "Parameter"
    Enum = "Enum"
    Property = "Property"


class NameConverter:
    @staticmethod
    def convert_yaml_names(yaml_data):
        NameConverter._convert_language_default_python_case(yaml_data)
        yaml_data["info"]["python_title"] = NameConverter._to_valid_python_name(
            name=yaml_data["info"]["title"].replace(" ", ""), convert_name=True
        )
        yaml_data['info']['pascal_case_title'] = yaml_data["language"]["default"]["name"]
        if yaml_data['info'].get("description"):
            if yaml_data["info"]["description"][-1] != ".":
                yaml_data["info"]["description"] += "."
        else:
            yaml_data["info"]["description"] = yaml_data['info']['pascal_case_title'] + "."
        NameConverter._convert_schemas(yaml_data['schemas'])
        NameConverter._convert_operation_groups(yaml_data['operationGroups'], yaml_data['info']['pascal_case_title'])
        if yaml_data.get('globalParameters'):
            NameConverter._convert_global_parameters(yaml_data['globalParameters'])

    @staticmethod
    def _convert_global_parameters(global_parameters):
        for global_parameter in global_parameters:
            NameConverter._convert_language_default_python_case(global_parameter)

    @staticmethod
    def _convert_operation_groups(operation_groups, code_model_title):
        for operation_group in operation_groups:
            NameConverter._convert_language_default_python_case(
                operation_group, pad_string=PadType.Model, convert_name=True
            )
            if not operation_group['language']['default']['name']:
                operation_group['language']['python']['className'] = code_model_title + "OperationsMixin"
            else:
                operation_group_name = operation_group['language']['default']['name']
                if operation_group_name == 'Operations':
                    operation_group['language']['python']['className'] = operation_group_name
                else:
                    operation_group['language']['python']['className'] = operation_group_name + "Operations"
            for operation in operation_group['operations']:
                NameConverter._convert_language_default_python_case(operation, pad_string=PadType.Method)
                for exception in operation.get('exceptions', []):
                    NameConverter._convert_language_default_python_case(exception)
                for parameter in operation.get("parameters", []):
                    NameConverter._convert_language_default_python_case(parameter, pad_string=PadType.Parameter)
                for request in operation.get("requests", []):
                    NameConverter._convert_language_default_python_case(request)
                    for parameter in request.get("parameters", []):
                        NameConverter._convert_language_default_python_case(parameter, pad_string=PadType.Parameter)
                for response in operation.get("responses", []):
                    NameConverter._convert_language_default_python_case(response)

    @staticmethod
    def _convert_schemas(schemas):
        for enum in schemas.get("sealedChoices", []) + schemas.get("choices", []):
            NameConverter._convert_enum_schema(enum)
        for obj in schemas.get("objects", []) + schemas.get("groups", []):
            NameConverter._convert_object_schema(obj)
        for type_list, schema_yamls in schemas.items():
            for schema in schema_yamls:
                if type_list == "objects":
                    continue
                if type_list in ["arrays", "dictionaries"]:
                    NameConverter._convert_language_default_python_case(schema)
                    NameConverter._convert_language_default_python_case(schema["elementType"])
                elif type_list == "constants":
                    NameConverter._convert_language_default_python_case(schema)
                    NameConverter._convert_language_default_python_case(schema["value"])
                    NameConverter._convert_language_default_python_case(schema["valueType"])
                else:
                    NameConverter._convert_language_default_python_case(schema)

    @staticmethod
    def _convert_enum_schema(schema):
        NameConverter._convert_language_default_pascal_case(schema)
        for choice in schema["choices"]:
            NameConverter._convert_language_default_python_case(choice, pad_string=PadType.Enum)

    @staticmethod
    def _convert_object_schema(schema):
        NameConverter._convert_language_default_pascal_case(schema)
        for prop in schema.get("properties", []):
            NameConverter._convert_language_default_python_case(schema=prop, pad_string=PadType.Property)

    @staticmethod
    def _convert_language_default_python_case(schema, **kwargs):
        if not schema.get("language") or schema["language"].get("python"):
            return
        schema['language']['python'] = dict(schema['language']['default'])
        schema_name = schema['language']['default']['name']
        schema_python_name = schema['language']['python']['name']

        schema_python_name = NameConverter._to_valid_python_name(name=schema_name, **kwargs)
        schema['language']['python']['name'] = schema_python_name.lower()

        schema_description = schema["language"]["default"]["description"].strip()
        if kwargs.get("pad_string") == PadType.Method and not schema_description:
            schema_description = schema["language"]["python"]["name"]
        if schema_description and schema_description[-1] != ".":
            schema_description += "."
        schema["language"]["python"]["description"] = schema_description

        schema_summary = schema["language"]["python"].get("summary")
        if schema_summary:
            schema_summary = schema_summary.strip()
            if schema_summary[-1] != ".":
                schema_summary += "."
            schema["language"]["python"]["summary"] = schema_summary

    @staticmethod
    def _convert_language_default_pascal_case(schema):
        if schema["language"].get("python"):
            return
        schema['language']['python'] = dict(schema['language']['default'])

        schema_description = schema["language"]["default"]["description"].strip()
        if not schema_description:
            # what is being used for empty ObjectSchema descriptions
            schema_description = schema["language"]["python"]["name"]
        if schema_description and schema_description[-1] != ".":
            schema_description += "."
        schema["language"]["python"]["description"] = schema_description

    @staticmethod
    def _to_pascal_case(name):
        name_list = re.split("[^a-zA-Z\\d]", name)
        name_list = [s[0].upper() + s[1:] if len(s) > 1 else s.upper() for s in name_list]
        return "".join(name_list)

    @staticmethod
    def _to_valid_python_name(name, *, pad_string="", convert_name=False):
        if not name:
            return NameConverter._to_python_case(pad_string.value if isinstance(pad_string, PadType) else pad_string)
        escaped_name = NameConverter._get_escaped_reserved_name(
            NameConverter._to_valid_name(name.replace("-", "_"), "_"), pad_string
        )
        if convert_name or name != escaped_name:
            return NameConverter._to_python_case(escaped_name)
        return escaped_name

    @staticmethod
    def _to_python_case(name):
        def replace_upper_characters(m):
            match_str = m.group().lower()
            if m.start() > 0 and name[m.start() - 1] == "_":
                # we are good if a '_' already exists
                return match_str
            # the first letter should not have _
            prefix = "_" if m.start() > 0 else ""

            # we will add an extra _ if there are multiple upper case chars together
            next_non_upper_case_char_location = m.start() + len(match_str)
            if (
                len(match_str) > 2
                and len(name) - next_non_upper_case_char_location > 1
                and name[next_non_upper_case_char_location].isalpha()
            ):

                return prefix + match_str[: len(match_str) - 1] + "_" + match_str[len(match_str) - 1]

            return prefix + match_str
        return re.sub("[A-Z]+", replace_upper_characters, name)

    @staticmethod
    def _get_escaped_reserved_name(name, pad_string):
        if name is None:
            raise ValueError("The value for name can not be None")
        if pad_string is None:
            raise ValueError("The value for pad_string can not be None")

        # check to see if name is reserved for the type of name we are converting
        if name.lower() in reserved_words["always_reserved"]:
            name += pad_string.value
        elif pad_string in [PadType.Method, PadType.Parameter]:
            if name.lower() in reserved_words["reserved_for_operations"]:
                name += pad_string.value
        elif pad_string in [PadType.Model, PadType.Property]:
            if name.lower() in reserved_words["reserved_for_models"]:
                name += pad_string.value
        elif pad_string == PadType.Enum:
            if name.lower() in reserved_words["reserved_for_enums"]:
                name += pad_string.value
        return name

    @staticmethod
    def _remove_invalid_characters(name, allowed_characters):
        name = name.replace("[]", "Sequence")
        valid_string = "".join([n for n in name if n.isalpha() or n.isdigit() or n in allowed_characters])
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
            raise ValueError(
                "Property name {} cannot be used as an identifier, as it contains only invalid characters.".format(name)
            )
        return correct_name
