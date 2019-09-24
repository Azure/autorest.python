class ExtendedModelType:
    def __init__(self, value):
        self._type_documentation = None
        self._return_type_documentation = None
        self._value = value

    def type_documentation(self):
        return self._value