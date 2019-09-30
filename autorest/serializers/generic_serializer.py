from .base_serializer import BaseSerializer


class GenericSerializer(BaseSerializer):
    def __init__(self, code_model):
        super(GenericSerializer, self).__init__(code_model)


    def _format_model_for_file(self, model):
        for prop in model.properties:
            self._format_property_doc_string_for_file(prop)
        model.init_line = "def __init__(self, **kwargs):"
        init_args = []
        init_args.append("super({}, self).__init__(**kwargs)".format(model.name))

        for prop in model.properties:
            if prop.readonly:
                init_args.append("self.{} = None".format(prop.name))
            else:
                init_args.append("self.{} = kwargs.get('{}', None)".format(prop.name, prop.name))
        model.init_args = init_args
