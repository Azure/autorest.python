# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta

class CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name) from None


class AccessTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    P4 = "P4"
    P6 = "P6"
    P10 = "P10"
    P20 = "P20"
    P30 = "P30"
    P40 = "P40"
    P50 = "P50"
    HOT = "Hot"
    COOL = "Cool"
    ARCHIVE = "Archive"

class ArchiveStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    REHYDRATE_PENDING_TO_HOT = "rehydrate-pending-to-hot"
    REHYDRATE_PENDING_TO_COOL = "rehydrate-pending-to-cool"

class BlobType(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    BLOCK_BLOB = "BlockBlob"
    PAGE_BLOB = "PageBlob"
    APPEND_BLOB = "AppendBlob"

class CopyStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    PENDING = "pending"
    SUCCESS = "success"
    ABORTED = "aborted"
    FAILED = "failed"

class LeaseDurationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    INFINITE = "infinite"
    FIXED = "fixed"

class LeaseStateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    AVAILABLE = "available"
    LEASED = "leased"
    EXPIRED = "expired"
    BREAKING = "breaking"
    BROKEN = "broken"

class LeaseStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    LOCKED = "locked"
    UNLOCKED = "unlocked"

class PublicAccessType(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    CONTAINER = "container"
    BLOB = "blob"
