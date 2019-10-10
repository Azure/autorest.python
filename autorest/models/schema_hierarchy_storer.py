class SchemaHierarchyStorer:
    def __init__(self, id, **kwargs):
        self.id = id
        self.parent_id = kwargs.pop('parent_id', None)
        self.has_additional_properties = kwargs.pop('has_additional_properties', False)
        self.discriminator = kwargs.pop('discriminator', None)

    @classmethod
    def from_yaml(cls, yaml_data):
        id = yaml_data['$key']

        # # this means it has no parent
        # if id == yaml_data['allOf'][0]['$key']:
        #     parent_id = None
        #     # if there is more than one entry, that means that
        #     # this object has additional properties
        #     has_additional_properties = len(yaml_data['allOf']) > 1
        # else:
        #     parent_id = yaml_data['allOf'][1]['$key']
        # return cls(
        #     id=id,
        #     parent_id=parent_id
        # )