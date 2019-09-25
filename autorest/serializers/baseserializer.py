from ..models import CompositeType, DictionaryType, SequenceType, EnumType


class BaseSerializer:
    def __init__(self, code_model):
        self.code_model = code_model
        self._service_client_file = None
        self._model_file = None


    def _format_property_doc_string_for_file(self, prop):
        # building the param line of the property doc
        if prop.constant or prop.readonly:
            param_doc_string = ":ivar {}:".format(prop.name)
        else:
            param_doc_string = ":param {}:".format(prop.name)
        description = prop.description
        if description and description[-1] != ".":
            description += "."
        if description:
            param_doc_string += " " + description

        # building the type line of the property doc
        type_doc_string = ":type {}: ".format(prop.name)
        if isinstance(prop, DictionaryType):
            type_doc_string += "dict[str, {}]".format(prop.element_type)
        elif isinstance(prop, SequenceType):
            type_doc_string += "list[{}]".format(prop.element_type)
        elif isinstance(prop, EnumType):
            type_doc_string += "str or {}".format(prop.enum_type)
        else:
            type_doc_string += prop.property_type

        prop.documentation_string = param_doc_string + "\n\t" + type_doc_string


    def service_client_file(self):
        return self._service_client_file


    def model_file(self):
        return self._model_file