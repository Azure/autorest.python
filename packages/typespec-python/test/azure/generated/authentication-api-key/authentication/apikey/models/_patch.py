# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import List
from azure.core.messaging import CloudEvent

from .._utils.model_base import _DESERIALIZE_REGISTER, _SERIALIZE_REGISTER

__all__: List[str] = []  # Add all objects you want publicly available to users at this package level


def cloud_event_serialize(obj) -> dict:
    return {
        "source": obj.source,
        "type": obj.type,
    }

def cloud_event_deserialize(data: dict) -> CloudEvent:
    return CloudEvent(source=data["source"], type=data["type"])

def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
    
    _SERIALIZE_REGISTER[CloudEvent] = cloud_event_serialize
    _DESERIALIZE_REGISTER[CloudEvent] = cloud_event_deserialize
