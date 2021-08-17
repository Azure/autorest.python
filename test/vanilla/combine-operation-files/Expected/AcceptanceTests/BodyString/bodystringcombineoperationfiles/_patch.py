import importlib
import sys


class PatchAddedModel(object):
    pass


def patch_sdk():
    try:
        models = sys.modules["bodystringcombineoperationfiles.models"]
    except KeyError:
        models = importlib.import_module("bodystringcombineoperationfiles.models")
    setattr(models, "PatchAddedModel", PatchAddedModel)
