from .model_base_serializer import ModelBaseSerializer


class ModelGenericSerializer(ModelBaseSerializer):
    def __init__(self, code_model, namespace):
        super(ModelGenericSerializer, self).__init__(code_model, namespace)


    def _format_model_for_file(self, model):
        for prop in model.properties:
            self._format_property_doc_string_for_file(prop)
        model.init_line = "def __init__(self, **kwargs):"
        init_args = []
        init_args.append("super({}, self).__init__(**kwargs)".format(model.name))

        for prop in model.properties:
            if model.base_model and prop in model.base_model.properties:
                continue
            if prop.readonly:
                init_args.append("self.{} = None".format(prop.name))
            else:
                default_value = "\"" + prop.default_value + "\"" if prop.default_value else "None"
                init_args.append("self.{} = kwargs.get('{}', {})".format(prop.name, prop.name, default_value))
        model.init_args = init_args
