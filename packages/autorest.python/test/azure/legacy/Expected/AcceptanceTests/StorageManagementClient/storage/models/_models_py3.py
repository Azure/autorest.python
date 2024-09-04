# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from .. import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Bar(_serialization.Model):
    """The URIs that are used to perform a retrieval of a public blob, queue or table object.

    :ivar recursive_point: Recursive Endpoints.
    :vartype recursive_point: ~storage.models.Endpoints
    """

    _attribute_map = {
        "recursive_point": {"key": "RecursivePoint", "type": "Endpoints"},
    }

    def __init__(self, *, recursive_point: Optional["_models.Endpoints"] = None, **kwargs: Any) -> None:
        """
        :keyword recursive_point: Recursive Endpoints.
        :paramtype recursive_point: ~storage.models.Endpoints
        """
        super().__init__(**kwargs)
        self.recursive_point = recursive_point


class CheckNameAvailabilityResult(_serialization.Model):
    """The CheckNameAvailability operation response.

    :ivar name_available: Gets a boolean value that indicates whether the name is available for you
     to use. If true, the name is available. If false, the name has already been taken or invalid
     and cannot be used.
    :vartype name_available: bool
    :ivar reason: Gets the reason that a storage account name could not be used. The Reason element
     is only returned if NameAvailable is false. Known values are: "AccountNameInvalid" and
     "AlreadyExists".
    :vartype reason: str or ~storage.models.Reason
    :ivar message: Gets an error message explaining the Reason value in more detail.
    :vartype message: str
    """

    _attribute_map = {
        "name_available": {"key": "nameAvailable", "type": "bool"},
        "reason": {"key": "reason", "type": "str"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(
        self,
        *,
        name_available: Optional[bool] = None,
        reason: Optional[Union[str, "_models.Reason"]] = None,
        message: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword name_available: Gets a boolean value that indicates whether the name is available for
         you to use. If true, the name is available. If false, the name has already been taken or
         invalid and cannot be used.
        :paramtype name_available: bool
        :keyword reason: Gets the reason that a storage account name could not be used. The Reason
         element is only returned if NameAvailable is false. Known values are: "AccountNameInvalid" and
         "AlreadyExists".
        :paramtype reason: str or ~storage.models.Reason
        :keyword message: Gets an error message explaining the Reason value in more detail.
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.name_available = name_available
        self.reason = reason
        self.message = message


class CustomDomain(_serialization.Model):
    """The custom domain assigned to this storage account. This can be set via Update.

    :ivar name: Gets or sets the custom domain name. Name is the CNAME source.
    :vartype name: str
    :ivar use_sub_domain: Indicates whether indirect CName validation is enabled. Default value is
     false. This should only be set on updates.
    :vartype use_sub_domain: bool
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "use_sub_domain": {"key": "useSubDomain", "type": "bool"},
    }

    def __init__(self, *, name: Optional[str] = None, use_sub_domain: Optional[bool] = None, **kwargs: Any) -> None:
        """
        :keyword name: Gets or sets the custom domain name. Name is the CNAME source.
        :paramtype name: str
        :keyword use_sub_domain: Indicates whether indirect CName validation is enabled. Default value
         is false. This should only be set on updates.
        :paramtype use_sub_domain: bool
        """
        super().__init__(**kwargs)
        self.name = name
        self.use_sub_domain = use_sub_domain


class Endpoints(_serialization.Model):
    """The URIs that are used to perform a retrieval of a public blob, queue or table object.

    :ivar blob: Gets the blob endpoint.
    :vartype blob: str
    :ivar queue: Gets the queue endpoint.
    :vartype queue: str
    :ivar table: Gets the table endpoint.
    :vartype table: str
    :ivar dummy_end_point: Dummy EndPoint.
    :vartype dummy_end_point: ~storage.models.Endpoints
    :ivar foo_point: Foo point.
    :vartype foo_point: ~storage.models.Foo
    """

    _attribute_map = {
        "blob": {"key": "blob", "type": "str"},
        "queue": {"key": "queue", "type": "str"},
        "table": {"key": "table", "type": "str"},
        "dummy_end_point": {"key": "dummyEndPoint", "type": "Endpoints"},
        "foo_point": {"key": "FooPoint", "type": "Foo"},
    }

    def __init__(
        self,
        *,
        blob: Optional[str] = None,
        queue: Optional[str] = None,
        table: Optional[str] = None,
        dummy_end_point: Optional["_models.Endpoints"] = None,
        foo_point: Optional["_models.Foo"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword blob: Gets the blob endpoint.
        :paramtype blob: str
        :keyword queue: Gets the queue endpoint.
        :paramtype queue: str
        :keyword table: Gets the table endpoint.
        :paramtype table: str
        :keyword dummy_end_point: Dummy EndPoint.
        :paramtype dummy_end_point: ~storage.models.Endpoints
        :keyword foo_point: Foo point.
        :paramtype foo_point: ~storage.models.Foo
        """
        super().__init__(**kwargs)
        self.blob = blob
        self.queue = queue
        self.table = table
        self.dummy_end_point = dummy_end_point
        self.foo_point = foo_point


class Foo(_serialization.Model):
    """The URIs that are used to perform a retrieval of a public blob, queue or table object.

    :ivar bar_point: Bar point.
    :vartype bar_point: ~storage.models.Bar
    """

    _attribute_map = {
        "bar_point": {"key": "Bar\\.Point", "type": "Bar"},
    }

    def __init__(self, *, bar_point: Optional["_models.Bar"] = None, **kwargs: Any) -> None:
        """
        :keyword bar_point: Bar point.
        :paramtype bar_point: ~storage.models.Bar
        """
        super().__init__(**kwargs)
        self.bar_point = bar_point


class Resource(_serialization.Model):
    """Resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class StorageAccount(Resource):  # pylint: disable=too-many-instance-attributes
    """The storage account.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar provisioning_state: Gets the status of the storage account at the time the operation was
     called. Known values are: "Creating", "ResolvingDNS", and "Succeeded".
    :vartype provisioning_state: str or ~storage.models.ProvisioningState
    :ivar account_type: Gets the type of the storage account. Known values are: "Standard_LRS",
     "Standard_ZRS", "Standard_GRS", "Standard_RAGRS", and "Premium_LRS".
    :vartype account_type: str or ~storage.models.AccountType
    :ivar primary_endpoints: Gets the URLs that are used to perform a retrieval of a public blob,
     queue or table object.Note that StandardZRS and PremiumLRS accounts only return the blob
     endpoint.
    :vartype primary_endpoints: ~storage.models.Endpoints
    :ivar primary_location: Gets the location of the primary for the storage account.
    :vartype primary_location: str
    :ivar status_of_primary: Gets the status indicating whether the primary location of the storage
     account is available or unavailable. Known values are: "Available" and "Unavailable".
    :vartype status_of_primary: str or ~storage.models.AccountStatus
    :ivar last_geo_failover_time: Gets the timestamp of the most recent instance of a failover to
     the secondary location. Only the most recent timestamp is retained. This element is not
     returned if there has never been a failover instance. Only available if the accountType is
     StandardGRS or StandardRAGRS.
    :vartype last_geo_failover_time: ~datetime.datetime
    :ivar secondary_location: Gets the location of the geo replicated secondary for the storage
     account. Only available if the accountType is StandardGRS or StandardRAGRS.
    :vartype secondary_location: str
    :ivar status_of_secondary: Gets the status indicating whether the secondary location of the
     storage account is available or unavailable. Only available if the accountType is StandardGRS
     or StandardRAGRS. Known values are: "Available" and "Unavailable".
    :vartype status_of_secondary: str or ~storage.models.AccountStatus
    :ivar creation_time: Gets the creation date and time of the storage account in UTC.
    :vartype creation_time: ~datetime.datetime
    :ivar custom_domain: Gets the user assigned custom domain assigned to this storage account.
    :vartype custom_domain: ~storage.models.CustomDomain
    :ivar secondary_endpoints: Gets the URLs that are used to perform a retrieval of a public blob,
     queue or table object from the secondary location of the storage account. Only available if the
     accountType is StandardRAGRS.
    :vartype secondary_endpoints: ~storage.models.Endpoints
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
        "account_type": {"key": "properties.accountType", "type": "str"},
        "primary_endpoints": {"key": "properties.primaryEndpoints", "type": "Endpoints"},
        "primary_location": {"key": "properties.primaryLocation", "type": "str"},
        "status_of_primary": {"key": "properties.statusOfPrimary", "type": "str"},
        "last_geo_failover_time": {"key": "properties.lastGeoFailoverTime", "type": "iso-8601"},
        "secondary_location": {"key": "properties.secondaryLocation", "type": "str"},
        "status_of_secondary": {"key": "properties.statusOfSecondary", "type": "str"},
        "creation_time": {"key": "properties.creationTime", "type": "iso-8601"},
        "custom_domain": {"key": "properties.customDomain", "type": "CustomDomain"},
        "secondary_endpoints": {"key": "properties.secondaryEndpoints", "type": "Endpoints"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        provisioning_state: Optional[Union[str, "_models.ProvisioningState"]] = None,
        account_type: Optional[Union[str, "_models.AccountType"]] = None,
        primary_endpoints: Optional["_models.Endpoints"] = None,
        primary_location: Optional[str] = None,
        status_of_primary: Optional[Union[str, "_models.AccountStatus"]] = None,
        last_geo_failover_time: Optional[datetime.datetime] = None,
        secondary_location: Optional[str] = None,
        status_of_secondary: Optional[Union[str, "_models.AccountStatus"]] = None,
        creation_time: Optional[datetime.datetime] = None,
        custom_domain: Optional["_models.CustomDomain"] = None,
        secondary_endpoints: Optional["_models.Endpoints"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword provisioning_state: Gets the status of the storage account at the time the operation
         was called. Known values are: "Creating", "ResolvingDNS", and "Succeeded".
        :paramtype provisioning_state: str or ~storage.models.ProvisioningState
        :keyword account_type: Gets the type of the storage account. Known values are: "Standard_LRS",
         "Standard_ZRS", "Standard_GRS", "Standard_RAGRS", and "Premium_LRS".
        :paramtype account_type: str or ~storage.models.AccountType
        :keyword primary_endpoints: Gets the URLs that are used to perform a retrieval of a public
         blob, queue or table object.Note that StandardZRS and PremiumLRS accounts only return the blob
         endpoint.
        :paramtype primary_endpoints: ~storage.models.Endpoints
        :keyword primary_location: Gets the location of the primary for the storage account.
        :paramtype primary_location: str
        :keyword status_of_primary: Gets the status indicating whether the primary location of the
         storage account is available or unavailable. Known values are: "Available" and "Unavailable".
        :paramtype status_of_primary: str or ~storage.models.AccountStatus
        :keyword last_geo_failover_time: Gets the timestamp of the most recent instance of a failover
         to the secondary location. Only the most recent timestamp is retained. This element is not
         returned if there has never been a failover instance. Only available if the accountType is
         StandardGRS or StandardRAGRS.
        :paramtype last_geo_failover_time: ~datetime.datetime
        :keyword secondary_location: Gets the location of the geo replicated secondary for the storage
         account. Only available if the accountType is StandardGRS or StandardRAGRS.
        :paramtype secondary_location: str
        :keyword status_of_secondary: Gets the status indicating whether the secondary location of the
         storage account is available or unavailable. Only available if the accountType is StandardGRS
         or StandardRAGRS. Known values are: "Available" and "Unavailable".
        :paramtype status_of_secondary: str or ~storage.models.AccountStatus
        :keyword creation_time: Gets the creation date and time of the storage account in UTC.
        :paramtype creation_time: ~datetime.datetime
        :keyword custom_domain: Gets the user assigned custom domain assigned to this storage account.
        :paramtype custom_domain: ~storage.models.CustomDomain
        :keyword secondary_endpoints: Gets the URLs that are used to perform a retrieval of a public
         blob, queue or table object from the secondary location of the storage account. Only available
         if the accountType is StandardRAGRS.
        :paramtype secondary_endpoints: ~storage.models.Endpoints
        """
        super().__init__(location=location, tags=tags, **kwargs)
        self.provisioning_state = provisioning_state
        self.account_type = account_type
        self.primary_endpoints = primary_endpoints
        self.primary_location = primary_location
        self.status_of_primary = status_of_primary
        self.last_geo_failover_time = last_geo_failover_time
        self.secondary_location = secondary_location
        self.status_of_secondary = status_of_secondary
        self.creation_time = creation_time
        self.custom_domain = custom_domain
        self.secondary_endpoints = secondary_endpoints


class StorageAccountCheckNameAvailabilityParameters(_serialization.Model):  # pylint: disable=name-too-long
    """StorageAccountCheckNameAvailabilityParameters.

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    :ivar type:
    :vartype type: str
    """

    _validation = {
        "name": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(self, *, name: str, type: str = "Microsoft.Storage/storageAccounts", **kwargs: Any) -> None:
        """
        :keyword name: Required.
        :paramtype name: str
        :keyword type:
        :paramtype type: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.type = type


class StorageAccountCreateParameters(Resource):
    """The parameters to provide for the account.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar account_type: Gets or sets the account type. Known values are: "Standard_LRS",
     "Standard_ZRS", "Standard_GRS", "Standard_RAGRS", and "Premium_LRS".
    :vartype account_type: str or ~storage.models.AccountType
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "account_type": {"key": "properties.accountType", "type": "str"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        account_type: Optional[Union[str, "_models.AccountType"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword account_type: Gets or sets the account type. Known values are: "Standard_LRS",
         "Standard_ZRS", "Standard_GRS", "Standard_RAGRS", and "Premium_LRS".
        :paramtype account_type: str or ~storage.models.AccountType
        """
        super().__init__(location=location, tags=tags, **kwargs)
        self.account_type = account_type


class StorageAccountKeys(_serialization.Model):
    """The access keys for the storage account.

    :ivar key1: Gets the value of key 1.
    :vartype key1: str
    :ivar key2: Gets the value of key 2.
    :vartype key2: str
    """

    _attribute_map = {
        "key1": {"key": "key1", "type": "str"},
        "key2": {"key": "key2", "type": "str"},
    }

    def __init__(self, *, key1: Optional[str] = None, key2: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword key1: Gets the value of key 1.
        :paramtype key1: str
        :keyword key2: Gets the value of key 2.
        :paramtype key2: str
        """
        super().__init__(**kwargs)
        self.key1 = key1
        self.key2 = key2


class StorageAccountListResult(_serialization.Model):
    """The list storage accounts operation response.

    :ivar value: Gets the list of storage accounts and their properties.
    :vartype value: list[~storage.models.StorageAccount]
    :ivar next_link: Gets the link to the next set of results. Currently this will always be empty
     as the API does not support pagination.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[StorageAccount]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: Optional[List["_models.StorageAccount"]] = None, next_link: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword value: Gets the list of storage accounts and their properties.
        :paramtype value: list[~storage.models.StorageAccount]
        :keyword next_link: Gets the link to the next set of results. Currently this will always be
         empty as the API does not support pagination.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class StorageAccountRegenerateKeyParameters(_serialization.Model):
    """StorageAccountRegenerateKeyParameters.

    :ivar key_name: Known values are: "key1" and "key2".
    :vartype key_name: str or ~storage.models.KeyName
    """

    _attribute_map = {
        "key_name": {"key": "keyName", "type": "str"},
    }

    def __init__(self, *, key_name: Optional[Union[str, "_models.KeyName"]] = None, **kwargs: Any) -> None:
        """
        :keyword key_name: Known values are: "key1" and "key2".
        :paramtype key_name: str or ~storage.models.KeyName
        """
        super().__init__(**kwargs)
        self.key_name = key_name


class StorageAccountUpdateParameters(Resource):
    """The parameters to update on the account.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar account_type: Gets or sets the account type. Note that StandardZRS and PremiumLRS
     accounts cannot be changed to other account types, and other account types cannot be changed to
     StandardZRS or PremiumLRS. Known values are: "Standard_LRS", "Standard_ZRS", "Standard_GRS",
     "Standard_RAGRS", and "Premium_LRS".
    :vartype account_type: str or ~storage.models.AccountType
    :ivar custom_domain: User domain assigned to the storage account. Name is the CNAME source.
     Only one custom domain is supported per storage account at this time. To clear the existing
     custom domain, use an empty string for the custom domain name property.
    :vartype custom_domain: ~storage.models.CustomDomain
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "account_type": {"key": "properties.accountType", "type": "str"},
        "custom_domain": {"key": "properties.customDomain", "type": "CustomDomain"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        account_type: Optional[Union[str, "_models.AccountType"]] = None,
        custom_domain: Optional["_models.CustomDomain"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword account_type: Gets or sets the account type. Note that StandardZRS and PremiumLRS
         accounts cannot be changed to other account types, and other account types cannot be changed to
         StandardZRS or PremiumLRS. Known values are: "Standard_LRS", "Standard_ZRS", "Standard_GRS",
         "Standard_RAGRS", and "Premium_LRS".
        :paramtype account_type: str or ~storage.models.AccountType
        :keyword custom_domain: User domain assigned to the storage account. Name is the CNAME source.
         Only one custom domain is supported per storage account at this time. To clear the existing
         custom domain, use an empty string for the custom domain name property.
        :paramtype custom_domain: ~storage.models.CustomDomain
        """
        super().__init__(location=location, tags=tags, **kwargs)
        self.account_type = account_type
        self.custom_domain = custom_domain


class SubResource(_serialization.Model):
    """SubResource.

    :ivar id: Resource Id.
    :vartype id: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
    }

    def __init__(self, *, id: Optional[str] = None, **kwargs: Any) -> None:  # pylint: disable=redefined-builtin
        """
        :keyword id: Resource Id.
        :paramtype id: str
        """
        super().__init__(**kwargs)
        self.id = id


class Usage(_serialization.Model):
    """Describes Storage Resource Usage.

    :ivar unit: Gets the unit of measurement. Known values are: "Count", "Bytes", "Seconds",
     "Percent", "CountsPerSecond", and "BytesPerSecond".
    :vartype unit: str or ~storage.models.UsageUnit
    :ivar current_value: Gets the current count of the allocated resources in the subscription.
    :vartype current_value: int
    :ivar limit: Gets the maximum count of the resources that can be allocated in the subscription.
    :vartype limit: int
    :ivar name: Gets the name of the type of usage.
    :vartype name: ~storage.models.UsageName
    """

    _attribute_map = {
        "unit": {"key": "unit", "type": "str"},
        "current_value": {"key": "currentValue", "type": "int"},
        "limit": {"key": "limit", "type": "int"},
        "name": {"key": "name", "type": "UsageName"},
    }

    def __init__(
        self,
        *,
        unit: Optional[Union[str, "_models.UsageUnit"]] = None,
        current_value: Optional[int] = None,
        limit: Optional[int] = None,
        name: Optional["_models.UsageName"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword unit: Gets the unit of measurement. Known values are: "Count", "Bytes", "Seconds",
         "Percent", "CountsPerSecond", and "BytesPerSecond".
        :paramtype unit: str or ~storage.models.UsageUnit
        :keyword current_value: Gets the current count of the allocated resources in the subscription.
        :paramtype current_value: int
        :keyword limit: Gets the maximum count of the resources that can be allocated in the
         subscription.
        :paramtype limit: int
        :keyword name: Gets the name of the type of usage.
        :paramtype name: ~storage.models.UsageName
        """
        super().__init__(**kwargs)
        self.unit = unit
        self.current_value = current_value
        self.limit = limit
        self.name = name


class UsageListResult(_serialization.Model):
    """The List Usages operation response.

    :ivar value: Gets or sets the list Storage Resource Usages.
    :vartype value: list[~storage.models.Usage]
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[Usage]"},
    }

    def __init__(self, *, value: Optional[List["_models.Usage"]] = None, **kwargs: Any) -> None:
        """
        :keyword value: Gets or sets the list Storage Resource Usages.
        :paramtype value: list[~storage.models.Usage]
        """
        super().__init__(**kwargs)
        self.value = value


class UsageName(_serialization.Model):
    """The Usage Names.

    :ivar value: Gets a string describing the resource name.
    :vartype value: str
    :ivar localized_value: Gets a localized string describing the resource name.
    :vartype localized_value: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "str"},
        "localized_value": {"key": "localizedValue", "type": "str"},
    }

    def __init__(self, *, value: Optional[str] = None, localized_value: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword value: Gets a string describing the resource name.
        :paramtype value: str
        :keyword localized_value: Gets a localized string describing the resource name.
        :paramtype localized_value: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.localized_value = localized_value
