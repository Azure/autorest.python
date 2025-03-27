# coding=utf-8

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Extensible enum. Indicates the action type. "Internal" refers to actions that are for internal
    only APIs.
    """

    INTERNAL = "Internal"
    """Actions are for internal-only APIs."""


class CheckNameAvailabilityReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Possible reasons for a name not being available."""

    INVALID = "Invalid"
    """Name is invalid."""
    ALREADY_EXISTS = "AlreadyExists"
    """Name already exists."""


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


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    """Indicates the operation is initiated by a user."""
    SYSTEM = "system"
    """Indicates the operation is initiated by a system."""
    USER_SYSTEM = "user,system"
    """Indicates the operation is initiated by a user or system."""
