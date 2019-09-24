class ModelType:
    def __init__(self, **kwargs):
        self.code_model = None
        self.is_constant = kwargs.pop('constant', False)
