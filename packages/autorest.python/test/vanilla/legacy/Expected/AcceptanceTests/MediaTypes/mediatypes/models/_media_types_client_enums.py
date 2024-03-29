# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ContentType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Content type for upload."""

    APPLICATION_PDF = "application/pdf"
    """Content Type 'application/pdf'"""
    IMAGE_JPEG = "image/jpeg"
    """Content Type 'image/jpeg'"""
    IMAGE_PNG = "image/png"
    """Content Type 'image/png'"""
    IMAGE_TIFF = "image/tiff"
    """Content Type 'image/tiff'"""


class ContentType1(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Content type for upload."""

    APPLICATION_JSON = "application/json"
    """Content Type 'application/json'"""
    APPLICATION_OCTET_STREAM = "application/octet-stream"
    """Content Type 'application/octet-stream'"""


class ContentType2(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Content type for upload."""

    APPLICATION_JSON = "application/json"
    """Content Type 'application/json'"""
    APPLICATION_OCTET_STREAM = "application/octet-stream"
    """Content Type 'application/octet-stream'"""
    TEXT_PLAIN = "text/plain"
    """Content Type 'text/plain'"""


class ContentType3(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Content type for upload."""

    APPLICATION_JSON = "application/json"
    """Content Type 'application/json'"""
    TEXT_PLAIN = "text/plain"
    """Content Type 'text/plain'"""
