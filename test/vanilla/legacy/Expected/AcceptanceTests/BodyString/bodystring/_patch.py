import importlib
import sys


class PatchAddedModel(object):
    pass


def patch_sdk():
    try:
        models = sys.modules["bodystring.models"]
    except KeyError:
        models = importlib.import_module("bodystring.models")
    setattr(models, "PatchAddedModel", PatchAddedModel)
