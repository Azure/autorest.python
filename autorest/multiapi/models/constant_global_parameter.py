# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict

class ConstantGlobalParameter(object):
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value