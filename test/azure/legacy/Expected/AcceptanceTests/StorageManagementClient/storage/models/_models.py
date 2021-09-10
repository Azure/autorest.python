# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class Bar(msrest.serialization.Model):
    """The URIs that are used to perform a retrieval of a public blob, queue or table object.

    :keyword recursive_point: Recursive Endpoints.
    :paramtype recursive_point: ~storage.models.Endpoints
    """

    _attribute_map = {
        "recursive_point": {"key": "RecursivePoint", "type": "Endpoints"},
    }

    def __init__(self, **kwargs):
        super(Bar, self).__init__(**kwargs)
        self.recursive_point = kwargs.get("recursive_point", None)


class CheckNameAvailabilityResult(msrest.serialization.Model):
    """The CheckNameAvailability operation response.

    :keyword name_available: Gets a boolean value that indicates whether the name is available for
     you to use. If true, the name is available. If false, the name has already been taken or
     invalid and cannot be used.
    :paramtype name_available: bool
    :keyword reason: Gets the reason that a storage account name could not be used. The Reason
     element is only returned if NameAvailable is false. Possible values include:
     "AccountNameInvalid", "AlreadyExists".
    :paramtype reason: str or ~storage.models.Reason
    :keyword message: Gets an error message explaining the Reason value in more detail.
    :paramtype message: str
    """

    _attribute_map = {
        "name_available": {"key": "nameAvailable", "type": "bool"},
        "reason": {"key": "reason", "type": "str"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(CheckNameAvailabilityResult, self).__init__(**kwargs)
        self.name_available = kwargs.get("name_available", None)
        self.reason = kwargs.get("reason", None)
        self.message = kwargs.get("message", None)


class CustomDomain(msrest.serialization.Model):
    """The custom domain assigned to this storage account. This can be set via Update.

    :keyword name: Gets or sets the custom domain name. Name is the CNAME source.
    :paramtype name: str
    :keyword use_sub_domain: Indicates whether indirect CName validation is enabled. Default value
     is false. This should only be set on updates.
    :paramtype use_sub_domain: bool
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "use_sub_domain": {"key": "useSubDomain", "type": "bool"},
    }

    def __init__(self, **kwargs):
        super(CustomDomain, self).__init__(**kwargs)
        self.name = kwargs.get("name", None)
        self.use_sub_domain = kwargs.get("use_sub_domain", None)


class Endpoints(msrest.serialization.Model):
    """The URIs that are used to perform a retrieval of a public blob, queue or table object.

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

    _attribute_map = {
        "blob": {"key": "blob", "type": "str"},
        "queue": {"key": "queue", "type": "str"},
        "table": {"key": "table", "type": "str"},
        "dummy_end_point": {"key": "dummyEndPoint", "type": "Endpoints"},
        "foo_point": {"key": "FooPoint", "type": "Foo"},
    }

    def __init__(self, **kwargs):
        super(Endpoints, self).__init__(**kwargs)
        self.blob = kwargs.get("blob", None)
        self.queue = kwargs.get("queue", None)
        self.table = kwargs.get("table", None)
        self.dummy_end_point = kwargs.get("dummy_end_point", None)
        self.foo_point = kwargs.get("foo_point", None)


class Foo(msrest.serialization.Model):
    """The URIs that are used to perform a retrieval of a public blob, queue or table object.

    :keyword bar_point: Bar point.
    :paramtype bar_point: ~storage.models.Bar
    """

    _attribute_map = {
        "bar_point": {"key": "Bar\\.Point", "type": "Bar"},
    }

    def __init__(self, **kwargs):
        super(Foo, self).__init__(**kwargs)
        self.bar_point = kwargs.get("bar_point", None)


class Resource(msrest.serialization.Model):
    """Resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :keyword location: Required. Resource location.
    :paramtype location: str
    :keyword tags: A set of tags. Resource tags.
    :paramtype tags: dict[str, str]
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

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs["location"]
        self.tags = kwargs.get("tags", None)


class StorageAccount(Resource):
    """The storage account.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :keyword location: Required. Resource location.
    :paramtype location: str
    :keyword tags: A set of tags. Resource tags.
    :paramtype tags: dict[str, str]
    :keyword provisioning_state: Gets the status of the storage account at the time the operation
     was called. Possible values include: "Creating", "ResolvingDNS", "Succeeded".
    :paramtype provisioning_state: str or ~storage.models.ProvisioningState
    :keyword account_type: Gets the type of the storage account. Possible values include:
     "Standard_LRS", "Standard_ZRS", "Standard_GRS", "Standard_RAGRS", "Premium_LRS".
    :paramtype account_type: str or ~storage.models.AccountType
    :keyword primary_endpoints: Gets the URLs that are used to perform a retrieval of a public
     blob, queue or table object.Note that StandardZRS and PremiumLRS accounts only return the blob
     endpoint.
    :paramtype primary_endpoints: ~storage.models.Endpoints
    :keyword primary_location: Gets the location of the primary for the storage account.
    :paramtype primary_location: str
    :keyword status_of_primary: Gets the status indicating whether the primary location of the
     storage account is available or unavailable. Possible values include: "Available",
     "Unavailable".
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
     or StandardRAGRS. Possible values include: "Available", "Unavailable".
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

    def __init__(self, **kwargs):
        super(StorageAccount, self).__init__(**kwargs)
        self.provisioning_state = kwargs.get("provisioning_state", None)
        self.account_type = kwargs.get("account_type", None)
        self.primary_endpoints = kwargs.get("primary_endpoints", None)
        self.primary_location = kwargs.get("primary_location", None)
        self.status_of_primary = kwargs.get("status_of_primary", None)
        self.last_geo_failover_time = kwargs.get("last_geo_failover_time", None)
        self.secondary_location = kwargs.get("secondary_location", None)
        self.status_of_secondary = kwargs.get("status_of_secondary", None)
        self.creation_time = kwargs.get("creation_time", None)
        self.custom_domain = kwargs.get("custom_domain", None)
        self.secondary_endpoints = kwargs.get("secondary_endpoints", None)


class StorageAccountCheckNameAvailabilityParameters(msrest.serialization.Model):
    """StorageAccountCheckNameAvailabilityParameters.

    All required parameters must be populated in order to send to Azure.

    :keyword name: Required.
    :paramtype name: str
    :keyword type:
    :paramtype type: str
    """

    _validation = {
        "name": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(StorageAccountCheckNameAvailabilityParameters, self).__init__(**kwargs)
        self.name = kwargs["name"]
        self.type = kwargs.get("type", "Microsoft.Storage/storageAccounts")


class StorageAccountCreateParameters(Resource):
    """The parameters to provide for the account.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :keyword location: Required. Resource location.
    :paramtype location: str
    :keyword tags: A set of tags. Resource tags.
    :paramtype tags: dict[str, str]
    :keyword account_type: Gets or sets the account type. Possible values include: "Standard_LRS",
     "Standard_ZRS", "Standard_GRS", "Standard_RAGRS", "Premium_LRS".
    :paramtype account_type: str or ~storage.models.AccountType
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

    def __init__(self, **kwargs):
        super(StorageAccountCreateParameters, self).__init__(**kwargs)
        self.account_type = kwargs.get("account_type", None)


class StorageAccountKeys(msrest.serialization.Model):
    """The access keys for the storage account.

    :keyword key1: Gets the value of key 1.
    :paramtype key1: str
    :keyword key2: Gets the value of key 2.
    :paramtype key2: str
    """

    _attribute_map = {
        "key1": {"key": "key1", "type": "str"},
        "key2": {"key": "key2", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(StorageAccountKeys, self).__init__(**kwargs)
        self.key1 = kwargs.get("key1", None)
        self.key2 = kwargs.get("key2", None)


class StorageAccountListResult(msrest.serialization.Model):
    """The list storage accounts operation response.

    :keyword value: Gets the list of storage accounts and their properties.
    :paramtype value: list[~storage.models.StorageAccount]
    :keyword next_link: Gets the link to the next set of results. Currently this will always be
     empty as the API does not support pagination.
    :paramtype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[StorageAccount]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(StorageAccountListResult, self).__init__(**kwargs)
        self.value = kwargs.get("value", None)
        self.next_link = kwargs.get("next_link", None)


class StorageAccountRegenerateKeyParameters(msrest.serialization.Model):
    """StorageAccountRegenerateKeyParameters.

    :keyword key_name:  Possible values include: "key1", "key2".
    :paramtype key_name: str or ~storage.models.KeyName
    """

    _attribute_map = {
        "key_name": {"key": "keyName", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(StorageAccountRegenerateKeyParameters, self).__init__(**kwargs)
        self.key_name = kwargs.get("key_name", None)


class StorageAccountUpdateParameters(Resource):
    """The parameters to update on the account.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :keyword location: Required. Resource location.
    :paramtype location: str
    :keyword tags: A set of tags. Resource tags.
    :paramtype tags: dict[str, str]
    :keyword account_type: Gets or sets the account type. Note that StandardZRS and PremiumLRS
     accounts cannot be changed to other account types, and other account types cannot be changed to
     StandardZRS or PremiumLRS. Possible values include: "Standard_LRS", "Standard_ZRS",
     "Standard_GRS", "Standard_RAGRS", "Premium_LRS".
    :paramtype account_type: str or ~storage.models.AccountType
    :keyword custom_domain: User domain assigned to the storage account. Name is the CNAME source.
     Only one custom domain is supported per storage account at this time. To clear the existing
     custom domain, use an empty string for the custom domain name property.
    :paramtype custom_domain: ~storage.models.CustomDomain
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

    def __init__(self, **kwargs):
        super(StorageAccountUpdateParameters, self).__init__(**kwargs)
        self.account_type = kwargs.get("account_type", None)
        self.custom_domain = kwargs.get("custom_domain", None)


class SubResource(msrest.serialization.Model):
    """SubResource.

    :keyword id: Resource Id.
    :paramtype id: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(SubResource, self).__init__(**kwargs)
        self.id = kwargs.get("id", None)


class Usage(msrest.serialization.Model):
    """Describes Storage Resource Usage.

    :keyword unit: Gets the unit of measurement. Possible values include: "Count", "Bytes",
     "Seconds", "Percent", "CountsPerSecond", "BytesPerSecond".
    :paramtype unit: str or ~storage.models.UsageUnit
    :keyword current_value: Gets the current count of the allocated resources in the subscription.
    :paramtype current_value: int
    :keyword limit: Gets the maximum count of the resources that can be allocated in the
     subscription.
    :paramtype limit: int
    :keyword name: Gets the name of the type of usage.
    :paramtype name: ~storage.models.UsageName
    """

    _attribute_map = {
        "unit": {"key": "unit", "type": "str"},
        "current_value": {"key": "currentValue", "type": "int"},
        "limit": {"key": "limit", "type": "int"},
        "name": {"key": "name", "type": "UsageName"},
    }

    def __init__(self, **kwargs):
        super(Usage, self).__init__(**kwargs)
        self.unit = kwargs.get("unit", None)
        self.current_value = kwargs.get("current_value", None)
        self.limit = kwargs.get("limit", None)
        self.name = kwargs.get("name", None)


class UsageListResult(msrest.serialization.Model):
    """The List Usages operation response.

    :keyword value: Gets or sets the list Storage Resource Usages.
    :paramtype value: list[~storage.models.Usage]
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[Usage]"},
    }

    def __init__(self, **kwargs):
        super(UsageListResult, self).__init__(**kwargs)
        self.value = kwargs.get("value", None)


class UsageName(msrest.serialization.Model):
    """The Usage Names.

    :keyword value: Gets a string describing the resource name.
    :paramtype value: str
    :keyword localized_value: Gets a localized string describing the resource name.
    :paramtype localized_value: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "str"},
        "localized_value": {"key": "localizedValue", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(UsageName, self).__init__(**kwargs)
        self.value = kwargs.get("value", None)
        self.localized_value = kwargs.get("localized_value", None)
