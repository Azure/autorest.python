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


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of ProvisioningState."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""
    PROVISIONING = "Provisioning"
    UPDATING = "Updating"
    DELETING = "Deleting"
    ACCEPTED = "Accepted"
