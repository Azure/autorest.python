from .modeltype import ModelType

class SequenceType(ModelType):
    def __init__(self, element_type, **kwargs):
        super(SequenceType, self).__init__()
        self._element_type = element_type

    def element_type(self):
        return self._element_type

    def type_documentation(self):
        self._type_documentation = "list[{}]".format(self._element_type)
        return self._type_documentation