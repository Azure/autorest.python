# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, Dict, List, Mapping, Optional, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class ErrorAdditionalInfo(_model_base.Model):
    """The resource management error additional info.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: any
    """

    type: Optional[str] = rest_field(visibility=["read"])
    """The additional info type."""
    info: Optional[Any] = rest_field(visibility=["read"])
    """The additional info."""


class ErrorDetail(_model_base.Model):
    """The error detail.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details:
     list[~azure.resourcemanager.models.commontypes.managedidentity.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.resourcemanager.models.commontypes.managedidentity.models.ErrorAdditionalInfo]
    """

    code: Optional[str] = rest_field(visibility=["read"])
    """The error code."""
    message: Optional[str] = rest_field(visibility=["read"])
    """The error message."""
    target: Optional[str] = rest_field(visibility=["read"])
    """The error target."""
    details: Optional[List["_models.ErrorDetail"]] = rest_field(visibility=["read"])
    """The error details."""
    additional_info: Optional[List["_models.ErrorAdditionalInfo"]] = rest_field(
        name="additionalInfo", visibility=["read"]
    )
    """The error additional info."""


class ErrorResponse(_model_base.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed
    operations.

    :ivar error: The error object.
    :vartype error: ~azure.resourcemanager.models.commontypes.managedidentity.models.ErrorDetail
    """

    error: Optional["_models.ErrorDetail"] = rest_field()
    """The error object."""

    @overload
    def __init__(
        self,
        *,
        error: Optional["_models.ErrorDetail"] = None,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class Resource(_model_base.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data:
     ~azure.resourcemanager.models.commontypes.managedidentity.models.SystemData
    """

    id: Optional[str] = rest_field(visibility=["read"])
    """Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long"""
    name: Optional[str] = rest_field(visibility=["read"])
    """The name of the resource."""
    type: Optional[str] = rest_field(visibility=["read"])
    """The type of the resource. E.g. \"Microsoft.Compute/virtualMachines\" or
     \"Microsoft.Storage/storageAccounts\"."""
    system_data: Optional["_models.SystemData"] = rest_field(name="systemData", visibility=["read"])
    """Azure Resource Manager metadata containing createdBy and modifiedBy information."""


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which
    has 'tags' and a 'location'.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data:
     ~azure.resourcemanager.models.commontypes.managedidentity.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    """

    tags: Optional[Dict[str, str]] = rest_field()
    """Resource tags."""
    location: str = rest_field(visibility=["read", "create"])
    """The geo-location where the resource lives. Required."""

    @overload
    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ManagedIdentityTrackedResource(TrackedResource):
    """Concrete tracked resource types can be created by aliasing this type using a specific property
    type.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data:
     ~azure.resourcemanager.models.commontypes.managedidentity.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar properties: The resource-specific properties for this resource.
    :vartype properties:
     ~azure.resourcemanager.models.commontypes.managedidentity.models.ManagedIdentityTrackedResourceProperties
    :ivar identity: The managed service identities assigned to this resource.
    :vartype identity:
     ~azure.resourcemanager.models.commontypes.managedidentity.models.ManagedServiceIdentity
    """

    properties: Optional["_models.ManagedIdentityTrackedResourceProperties"] = rest_field()
    """The resource-specific properties for this resource."""
    identity: Optional["_models.ManagedServiceIdentity"] = rest_field()
    """The managed service identities assigned to this resource."""

    @overload
    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        properties: Optional["_models.ManagedIdentityTrackedResourceProperties"] = None,
        identity: Optional["_models.ManagedServiceIdentity"] = None,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ManagedIdentityTrackedResourceProperties(_model_base.Model):
    """Managed Identity Arm Resource Properties.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar provisioning_state: The status of the last operation. Required.
    :vartype provisioning_state: str
    """

    provisioning_state: str = rest_field(name="provisioningState", visibility=["read"])
    """The status of the last operation. Required."""


class ManagedServiceIdentity(_model_base.Model):
    """Managed service identity (system assigned and/or user assigned identities).

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar principal_id: The service principal ID of the system assigned identity. This property
     will only be provided for a system assigned identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of the system assigned identity. This property will only be
     provided for a system assigned identity.
    :vartype tenant_id: str
    :ivar type: The type of managed identity assigned to this resource. Required. Known values are:
     "None", "SystemAssigned", "UserAssigned", and "SystemAssigned,UserAssigned".
    :vartype type: str or
     ~azure.resourcemanager.models.commontypes.managedidentity.models.ManagedServiceIdentityType
    :ivar user_assigned_identities: The identities assigned to this resource by the user.
    :vartype user_assigned_identities: dict[str,
     ~azure.resourcemanager.models.commontypes.managedidentity.models.UserAssignedIdentity]
    """

    principal_id: Optional[str] = rest_field(name="principalId", visibility=["read"])
    """The service principal ID of the system assigned identity. This property will only be provided
     for a system assigned identity."""
    tenant_id: Optional[str] = rest_field(name="tenantId", visibility=["read"])
    """The tenant ID of the system assigned identity. This property will only be provided for a system
     assigned identity."""
    type: Union[str, "_models.ManagedServiceIdentityType"] = rest_field()
    """The type of managed identity assigned to this resource. Required. Known values are: \"None\",
     \"SystemAssigned\", \"UserAssigned\", and \"SystemAssigned,UserAssigned\"."""
    user_assigned_identities: Optional[Dict[str, "_models.UserAssignedIdentity"]] = rest_field(
        name="userAssignedIdentities"
    )
    """The identities assigned to this resource by the user."""

    @overload
    def __init__(
        self,
        *,
        type: Union[str, "_models.ManagedServiceIdentityType"],
        user_assigned_identities: Optional[Dict[str, "_models.UserAssignedIdentity"]] = None,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class SystemData(_model_base.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or
     ~azure.resourcemanager.models.commontypes.managedidentity.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or
     ~azure.resourcemanager.models.commontypes.managedidentity.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    created_by: Optional[str] = rest_field(name="createdBy")
    """The identity that created the resource."""
    created_by_type: Optional[Union[str, "_models.CreatedByType"]] = rest_field(name="createdByType")
    """The type of identity that created the resource. Known values are: \"User\", \"Application\",
     \"ManagedIdentity\", and \"Key\"."""
    created_at: Optional[datetime.datetime] = rest_field(name="createdAt", format="rfc3339")
    """The timestamp of resource creation (UTC)."""
    last_modified_by: Optional[str] = rest_field(name="lastModifiedBy")
    """The identity that last modified the resource."""
    last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = rest_field(name="lastModifiedByType")
    """The type of identity that last modified the resource. Known values are: \"User\",
     \"Application\", \"ManagedIdentity\", and \"Key\"."""
    last_modified_at: Optional[datetime.datetime] = rest_field(name="lastModifiedAt", format="rfc3339")
    """The timestamp of resource last modification (UTC)."""

    @overload
    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class UserAssignedIdentity(_model_base.Model):
    """User assigned identity properties.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal ID of the assigned identity.
    :vartype principal_id: str
    :ivar client_id: The client ID of the assigned identity.
    :vartype client_id: str
    """

    principal_id: Optional[str] = rest_field(name="principalId", visibility=["read"])
    """The principal ID of the assigned identity."""
    client_id: Optional[str] = rest_field(name="clientId", visibility=["read"])
    """The client ID of the assigned identity."""
