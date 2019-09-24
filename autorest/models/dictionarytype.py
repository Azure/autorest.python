from .modeltype import ModelType
class DictionaryType(ModelType):
    def __init__(self, value_type, **kwargs):
        super(DictionaryType, self).__init__()
        self._type_documentation = None
        self._value_type = value_type

    def value_type(self):
        return self._value_type

    def type_documentation(self):
        self._type_documentation = "dict[str, {}]".format(self._value_type)
        return self._type_documentation