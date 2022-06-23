# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Optional

from .. import _serialization


class SourcePath(_serialization.Model):
    """Uri or local path to source data.

    :ivar source: File source path.
    :vartype source: str
    """

    _validation = {
        "source": {"max_length": 2048},
    }

    _attribute_map = {
        "source": {"key": "source", "type": "str"},
    }

    def __init__(self, *, source: Optional[str] = None, **kwargs):
        """
        :keyword source: File source path.
        :paramtype source: str
        """
        super().__init__(**kwargs)
        self.source = source
