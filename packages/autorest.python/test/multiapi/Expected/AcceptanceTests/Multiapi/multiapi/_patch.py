import importlib
import sys


class PatchAddedModel(object):
    pass


def patch_sdk():
    try:
        models = sys.modules["multiapi.models"]
    except KeyError:
        models = importlib.import_module("multiapi.models")
    setattr(models, "PatchAddedModel", PatchAddedModel)
