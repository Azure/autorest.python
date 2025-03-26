# coding=utf-8

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The kind of entity that created the resource."""

    USER = "User"
    """The entity was created by a user."""
    APPLICATION = "Application"
    """The entity was created by an application."""
    MANAGED_IDENTITY = "ManagedIdentity"
    """The entity was created by a managed identity."""
    KEY = "Key"
    """The entity was created by a key."""


class ManagedServiceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of managed service identity (where both SystemAssigned and UserAssigned types are
    allowed).
    """

    NONE = "None"
    """No managed identity."""
    SYSTEM_ASSIGNED = "SystemAssigned"
    """System assigned managed identity."""
    USER_ASSIGNED = "UserAssigned"
    """User assigned managed identity."""
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"
    """System and user assigned managed identity."""
