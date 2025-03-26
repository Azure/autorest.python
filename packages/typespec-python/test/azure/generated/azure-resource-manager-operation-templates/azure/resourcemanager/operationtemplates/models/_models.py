# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
# pylint: disable=useless-super-delegation

import datetime
from typing import Any, Dict, List, Mapping, Optional, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    from .. import models as _models


class CheckNameAvailabilityRequest(_model_base.Model):
    """The check availability request body.

    :ivar name: The name of the resource for which availability needs to be checked.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    """

    name: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name of the resource for which availability needs to be checked."""
    type: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The resource type."""

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
        type: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CheckNameAvailabilityResponse(_model_base.Model):
    """The check availability result.

    :ivar name_available: Indicates if the resource name is available.
    :vartype name_available: bool
    :ivar reason: The reason why the given name is not available. Known values are: "Invalid" and
     "AlreadyExists".
    :vartype reason: str or
     ~azure.resourcemanager.operationtemplates.models.CheckNameAvailabilityReason
    :ivar message: Detailed reason why the given name is not available.
    :vartype message: str
    """

    name_available: Optional[bool] = rest_field(
        name="nameAvailable", visibility=["read", "create", "update", "delete", "query"]
    )
    """Indicates if the resource name is available."""
    reason: Optional[Union[str, "_models.CheckNameAvailabilityReason"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The reason why the given name is not available. Known values are: \"Invalid\" and
     \"AlreadyExists\"."""
    message: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Detailed reason why the given name is not available."""

    @overload
    def __init__(
        self,
        *,
        name_available: Optional[bool] = None,
        reason: Optional[Union[str, "_models.CheckNameAvailabilityReason"]] = None,
        message: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ErrorAdditionalInfo(_model_base.Model):
    """The resource management error additional info.

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

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.resourcemanager.operationtemplates.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.resourcemanager.operationtemplates.models.ErrorAdditionalInfo]
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
    :vartype error: ~azure.resourcemanager.operationtemplates.models.ErrorDetail
    """

    error: Optional["_models.ErrorDetail"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The error object."""

    @overload
    def __init__(
        self,
        *,
        error: Optional["_models.ErrorDetail"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ExportRequest(_model_base.Model):
    """ExportRequest.

    :ivar format: Format of the exported order. Required.
    :vartype format: str
    """

    format: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Format of the exported order. Required."""

    @overload
    def __init__(
        self,
        *,
        format: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Operation(_model_base.Model):
    """Details of a REST API operation, returned from the Resource Provider Operations API.

    :ivar name: The name of the operation, as per Resource-Based Access Control (RBAC). Examples:
     "Microsoft.Compute/virtualMachines/write", "Microsoft.Compute/virtualMachines/capture/action".
    :vartype name: str
    :ivar is_data_action: Whether the operation applies to data-plane. This is "true" for
     data-plane operations and "false" for Azure Resource Manager/control-plane operations.
    :vartype is_data_action: bool
    :ivar display: Localized display information for this particular operation.
    :vartype display: ~azure.resourcemanager.operationtemplates.models.OperationDisplay
    :ivar origin: The intended executor of the operation; as in Resource Based Access Control
     (RBAC) and audit logs UX. Default value is "user,system". Known values are: "user", "system",
     and "user,system".
    :vartype origin: str or ~azure.resourcemanager.operationtemplates.models.Origin
    :ivar action_type: Extensible enum. Indicates the action type. "Internal" refers to actions
     that are for internal only APIs. "Internal"
    :vartype action_type: str or ~azure.resourcemanager.operationtemplates.models.ActionType
    """

    name: Optional[str] = rest_field(visibility=["read"])
    """The name of the operation, as per Resource-Based Access Control (RBAC). Examples:
     \"Microsoft.Compute/virtualMachines/write\",
     \"Microsoft.Compute/virtualMachines/capture/action\"."""
    is_data_action: Optional[bool] = rest_field(name="isDataAction", visibility=["read"])
    """Whether the operation applies to data-plane. This is \"true\" for data-plane operations and
     \"false\" for Azure Resource Manager/control-plane operations."""
    display: Optional["_models.OperationDisplay"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Localized display information for this particular operation."""
    origin: Optional[Union[str, "_models.Origin"]] = rest_field(visibility=["read"])
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
     logs UX. Default value is \"user,system\". Known values are: \"user\", \"system\", and
     \"user,system\"."""
    action_type: Optional[Union[str, "_models.ActionType"]] = rest_field(name="actionType", visibility=["read"])
    """Extensible enum. Indicates the action type. \"Internal\" refers to actions that are for
     internal only APIs. \"Internal\""""

    @overload
    def __init__(
        self,
        *,
        display: Optional["_models.OperationDisplay"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class OperationDisplay(_model_base.Model):
    """Localized display information for and operation.

    :ivar provider: The localized friendly form of the resource provider name, e.g. "Microsoft
     Monitoring Insights" or "Microsoft Compute".
    :vartype provider: str
    :ivar resource: The localized friendly name of the resource type related to this operation.
     E.g. "Virtual Machines" or "Job Schedule Collections".
    :vartype resource: str
    :ivar operation: The concise, localized friendly name for the operation; suitable for
     dropdowns. E.g. "Create or Update Virtual Machine", "Restart Virtual Machine".
    :vartype operation: str
    :ivar description: The short, localized friendly description of the operation; suitable for
     tool tips and detailed views.
    :vartype description: str
    """

    provider: Optional[str] = rest_field(visibility=["read"])
    """The localized friendly form of the resource provider name, e.g. \"Microsoft Monitoring
     Insights\" or \"Microsoft Compute\"."""
    resource: Optional[str] = rest_field(visibility=["read"])
    """The localized friendly name of the resource type related to this operation. E.g. \"Virtual
     Machines\" or \"Job Schedule Collections\"."""
    operation: Optional[str] = rest_field(visibility=["read"])
    """The concise, localized friendly name for the operation; suitable for dropdowns. E.g. \"Create
     or Update Virtual Machine\", \"Restart Virtual Machine\"."""
    description: Optional[str] = rest_field(visibility=["read"])
    """The short, localized friendly description of the operation; suitable for tool tips and detailed
     views."""


class Resource(_model_base.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.resourcemanager.operationtemplates.models.SystemData
    """

    id: Optional[str] = rest_field(visibility=["read"])
    """Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}."""
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

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.resourcemanager.operationtemplates.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    """

    tags: Optional[Dict[str, str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Resource tags."""
    location: str = rest_field(visibility=["read", "create"])
    """The geo-location where the resource lives. Required."""

    @overload
    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Order(TrackedResource):
    """Concrete tracked resource types can be created by aliasing this type using a specific property
    type.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.resourcemanager.operationtemplates.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar properties: The resource-specific properties for this resource.
    :vartype properties: ~azure.resourcemanager.operationtemplates.models.OrderProperties
    """

    properties: Optional["_models.OrderProperties"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The resource-specific properties for this resource."""

    @overload
    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        properties: Optional["_models.OrderProperties"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class OrderProperties(_model_base.Model):
    """OrderProperties.

    :ivar product_id: The product ID of the order. Required.
    :vartype product_id: str
    :ivar amount: Amount of the product. Required.
    :vartype amount: int
    :ivar provisioning_state: The provisioning state of the product.
    :vartype provisioning_state: str
    """

    product_id: str = rest_field(name="productId", visibility=["read", "create", "update", "delete", "query"])
    """The product ID of the order. Required."""
    amount: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Amount of the product. Required."""
    provisioning_state: Optional[str] = rest_field(name="provisioningState", visibility=["read"])
    """The provisioning state of the product."""

    @overload
    def __init__(
        self,
        *,
        product_id: str,
        amount: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SystemData(_model_base.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or ~azure.resourcemanager.operationtemplates.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or
     ~azure.resourcemanager.operationtemplates.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    created_by: Optional[str] = rest_field(name="createdBy", visibility=["read", "create", "update", "delete", "query"])
    """The identity that created the resource."""
    created_by_type: Optional[Union[str, "_models.CreatedByType"]] = rest_field(
        name="createdByType", visibility=["read", "create", "update", "delete", "query"]
    )
    """The type of identity that created the resource. Known values are: \"User\", \"Application\",
     \"ManagedIdentity\", and \"Key\"."""
    created_at: Optional[datetime.datetime] = rest_field(
        name="createdAt", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """The timestamp of resource creation (UTC)."""
    last_modified_by: Optional[str] = rest_field(
        name="lastModifiedBy", visibility=["read", "create", "update", "delete", "query"]
    )
    """The identity that last modified the resource."""
    last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = rest_field(
        name="lastModifiedByType", visibility=["read", "create", "update", "delete", "query"]
    )
    """The type of identity that last modified the resource. Known values are: \"User\",
     \"Application\", \"ManagedIdentity\", and \"Key\"."""
    last_modified_at: Optional[datetime.datetime] = rest_field(
        name="lastModifiedAt", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
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
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
