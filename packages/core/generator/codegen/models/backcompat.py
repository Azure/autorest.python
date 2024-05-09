# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from ...utils import to_snake_case
from ...types import Options

class BackcompatMixin:
    def __init__(self, options: Options):
        self.is_legacy = not (options.get("versionTolerant") or options.get("lowLevelClient"))

class SdkPackageBackcompatMixin(BackcompatMixin):
    def get_models_filename(self) -> str:
        return "_models_py3" if self.is_legacy else "_models"
    
    def get_enums_filename(self, client_filename: str) -> str:
        return f"_{client_filename}_enums"

class ClientBackcompatMixin(BackcompatMixin):

    def get_filename(self, name: str) -> str:
        return to_snake_case(name) if self.is_legacy else name



