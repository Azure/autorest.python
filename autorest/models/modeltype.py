class ModelType:
    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description
        self.required = kwargs.pop('required', False)
        self.readonly = kwargs.pop('readonly', False)
        self.constant = kwargs.pop('constant', False)

    """Constructs the documentation string for a property

    :returns: The documentation string of the property
    :rtype: str
    """
    def get_property_documentation_string(self) -> str:
        if self.constant or self.readonly:
            doc_string = ":ivar {}:".format(self.name)
        else:
            doc_string = ":param {}:".format(self.name)
        if self.required:
            doc_string += " Required."

        description = self.description
        if description and description[-1] != ".":
            description += "."
        if description:
            doc_string += " " + description
        return doc_string