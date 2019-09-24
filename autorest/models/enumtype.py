from .modeltype import ModelType

class EnumType(ModelType):
    def __init__(self, element_type, **kwargs):
        super(SequenceType, self).__init__()
        self._element_type = element_type

    def type_documentation(self):
        self._type_documentation = "list[{}]".format(self._element_type.type_documentation())
        return self._type_documentation