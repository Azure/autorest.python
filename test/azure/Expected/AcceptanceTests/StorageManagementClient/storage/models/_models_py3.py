# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class StorageAccountCheckNameAvailabilityParameters(Model):
    """StorageAccountCheckNameAvailabilityParameters.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param type:  Default value: "Microsoft.Storage/storageAccounts" .
    :type type: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, name: str, type: str="Microsoft.Storage/storageAccounts", **kwargs) -> None:
        super(StorageAccountCheckNameAvailabilityParameters, self).__init__(**kwargs)
        self.name = name
        self.type = type
from msrest.serialization import Model


class CheckNameAvailabilityResult(Model):
    """The CheckNameAvailability operation response.

    :param name_available: Gets a boolean value that indicates whether the
     name is available for you to use. If true, the name is available. If
     false, the name has already been taken or invalid and cannot be used.
    :type name_available: bool
    :param reason: Gets the reason that a storage account name could not be
     used. The Reason element is only returned if NameAvailable is false.
     Possible values include: 'AccountNameInvalid', 'AlreadyExists'
    :type reason: str or ~storage.models.Reason
    :param message: Gets an error message explaining the Reason value in more
     detail.
    :type message: str
    """

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'Reason'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, name_available: bool=None, reason=None, message: str=None, **kwargs) -> None:
        super(CheckNameAvailabilityResult, self).__init__(**kwargs)
        self.name_available = name_available
        self.reason = reason
        self.message = message
from msrest.serialization import Model


class Resource(Model):
    """Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags
from msrest.serialization import Model


class StorageAccountCreateParameters(Resource):
    """The parameters to provide for the account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param account_type: Gets or sets the account type. Possible values
     include: 'Standard_LRS', 'Standard_ZRS', 'Standard_GRS', 'Standard_RAGRS',
     'Premium_LRS'
    :type account_type: str or ~storage.models.AccountType
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'account_type': {'key': 'properties.accountType', 'type': 'AccountType'},
    }

    def __init__(self, *, location: str, tags=None, account_type=None, **kwargs) -> None:
        super(StorageAccountCreateParameters, self).__init__(location=location, tags=tags, **kwargs)
        self.account_type = account_type
from msrest.serialization import Model


class Bar(Model):
    """The URIs that are used to perform a retrieval of a public blob, queue or
    table object.

    :param recursive_point: Recursive Endpoints
    :type recursive_point: ~storage.models.Endpoints
    """

    _attribute_map = {
        'recursive_point': {'key': 'RecursivePoint', 'type': 'Endpoints'},
    }

    def __init__(self, *, recursive_point=None, **kwargs) -> None:
        super(Bar, self).__init__(**kwargs)
        self.recursive_point = recursive_point
from msrest.serialization import Model


class Foo(Model):
    """The URIs that are used to perform a retrieval of a public blob, queue or
    table object.

    :param bar_point: Bar point
    :type bar_point: ~storage.models.Bar
    """

    _attribute_map = {
        'bar_point': {'key': 'Bar\\.Point', 'type': 'Bar'},
    }

    def __init__(self, *, bar_point=None, **kwargs) -> None:
        super(Foo, self).__init__(**kwargs)
        self.bar_point = bar_point
from msrest.serialization import Model


class Endpoints(Model):
    """The URIs that are used to perform a retrieval of a public blob, queue or
    table object.

    :param blob: Gets the blob endpoint.
    :type blob: str
    :param queue: Gets the queue endpoint.
    :type queue: str
    :param table: Gets the table endpoint.
    :type table: str
    :param dummy_end_point: Dummy EndPoint
    :type dummy_end_point: ~storage.models.Endpoints
    :param foo_point: Foo point
    :type foo_point: ~storage.models.Foo
    """

    _attribute_map = {
        'blob': {'key': 'blob', 'type': 'str'},
        'queue': {'key': 'queue', 'type': 'str'},
        'table': {'key': 'table', 'type': 'str'},
        'dummy_end_point': {'key': 'dummyEndPoint', 'type': 'Endpoints'},
        'foo_point': {'key': 'FooPoint', 'type': 'Foo'},
    }

    def __init__(self, *, blob: str=None, queue: str=None, table: str=None, dummy_end_point=None, foo_point=None, **kwargs) -> None:
        super(Endpoints, self).__init__(**kwargs)
        self.blob = blob
        self.queue = queue
        self.table = table
        self.dummy_end_point = dummy_end_point
        self.foo_point = foo_point
from msrest.serialization import Model


class CustomDomain(Model):
    """The custom domain assigned to this storage account. This can be set via
    Update.

    :param name: Gets or sets the custom domain name. Name is the CNAME
     source.
    :type name: str
    :param use_sub_domain: Indicates whether indirect CName validation is
     enabled. Default value is false. This should only be set on updates
    :type use_sub_domain: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'use_sub_domain': {'key': 'useSubDomain', 'type': 'bool'},
    }

    def __init__(self, *, name: str=None, use_sub_domain: bool=None, **kwargs) -> None:
        super(CustomDomain, self).__init__(**kwargs)
        self.name = name
        self.use_sub_domain = use_sub_domain
from msrest.serialization import Model


class StorageAccount(Resource):
    """The storage account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param provisioning_state: Gets the status of the storage account at the
     time the operation was called. Possible values include: 'Creating',
     'ResolvingDNS', 'Succeeded'
    :type provisioning_state: str or ~storage.models.ProvisioningState
    :param account_type: Gets the type of the storage account. Possible values
     include: 'Standard_LRS', 'Standard_ZRS', 'Standard_GRS', 'Standard_RAGRS',
     'Premium_LRS'
    :type account_type: str or ~storage.models.AccountType
    :param primary_endpoints: Gets the URLs that are used to perform a
     retrieval of a public blob, queue or table object.Note that StandardZRS
     and PremiumLRS accounts only return the blob endpoint.
    :type primary_endpoints: ~storage.models.Endpoints
    :param primary_location: Gets the location of the primary for the storage
     account.
    :type primary_location: str
    :param status_of_primary: Gets the status indicating whether the primary
     location of the storage account is available or unavailable. Possible
     values include: 'Available', 'Unavailable'
    :type status_of_primary: str or ~storage.models.AccountStatus
    :param last_geo_failover_time: Gets the timestamp of the most recent
     instance of a failover to the secondary location. Only the most recent
     timestamp is retained. This element is not returned if there has never
     been a failover instance. Only available if the accountType is StandardGRS
     or StandardRAGRS.
    :type last_geo_failover_time: datetime
    :param secondary_location: Gets the location of the geo replicated
     secondary for the storage account. Only available if the accountType is
     StandardGRS or StandardRAGRS.
    :type secondary_location: str
    :param status_of_secondary: Gets the status indicating whether the
     secondary location of the storage account is available or unavailable.
     Only available if the accountType is StandardGRS or StandardRAGRS.
     Possible values include: 'Available', 'Unavailable'
    :type status_of_secondary: str or ~storage.models.AccountStatus
    :param creation_time: Gets the creation date and time of the storage
     account in UTC.
    :type creation_time: datetime
    :param custom_domain: Gets the user assigned custom domain assigned to
     this storage account.
    :type custom_domain: ~storage.models.CustomDomain
    :param secondary_endpoints: Gets the URLs that are used to perform a
     retrieval of a public blob, queue or table object from the secondary
     location of the storage account. Only available if the accountType is
     StandardRAGRS.
    :type secondary_endpoints: ~storage.models.Endpoints
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningState'},
        'account_type': {'key': 'properties.accountType', 'type': 'AccountType'},
        'primary_endpoints': {'key': 'properties.primaryEndpoints', 'type': 'Endpoints'},
        'primary_location': {'key': 'properties.primaryLocation', 'type': 'str'},
        'status_of_primary': {'key': 'properties.statusOfPrimary', 'type': 'AccountStatus'},
        'last_geo_failover_time': {'key': 'properties.lastGeoFailoverTime', 'type': 'iso-8601'},
        'secondary_location': {'key': 'properties.secondaryLocation', 'type': 'str'},
        'status_of_secondary': {'key': 'properties.statusOfSecondary', 'type': 'AccountStatus'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'custom_domain': {'key': 'properties.customDomain', 'type': 'CustomDomain'},
        'secondary_endpoints': {'key': 'properties.secondaryEndpoints', 'type': 'Endpoints'},
    }

    def __init__(self, *, location: str, tags=None, provisioning_state=None, account_type=None, primary_endpoints=None, primary_location: str=None, status_of_primary=None, last_geo_failover_time=None, secondary_location: str=None, status_of_secondary=None, creation_time=None, custom_domain=None, secondary_endpoints=None, **kwargs) -> None:
        super(StorageAccount, self).__init__(location=location, tags=tags, **kwargs)
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
from msrest.serialization import Model


class StorageAccountKeys(Model):
    """The access keys for the storage account.

    :param key1: Gets the value of key 1.
    :type key1: str
    :param key2: Gets the value of key 2.
    :type key2: str
    """

    _attribute_map = {
        'key1': {'key': 'key1', 'type': 'str'},
        'key2': {'key': 'key2', 'type': 'str'},
    }

    def __init__(self, *, key1: str=None, key2: str=None, **kwargs) -> None:
        super(StorageAccountKeys, self).__init__(**kwargs)
        self.key1 = key1
        self.key2 = key2
from msrest.serialization import Model


class StorageAccountUpdateParameters(Resource):
    """The parameters to update on the account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param account_type: Gets or sets the account type. Note that StandardZRS
     and PremiumLRS accounts cannot be changed to other account types, and
     other account types cannot be changed to StandardZRS or PremiumLRS.
     Possible values include: 'Standard_LRS', 'Standard_ZRS', 'Standard_GRS',
     'Standard_RAGRS', 'Premium_LRS'
    :type account_type: str or ~storage.models.AccountType
    :param custom_domain: User domain assigned to the storage account. Name is
     the CNAME source. Only one custom domain is supported per storage account
     at this time. To clear the existing custom domain, use an empty string for
     the custom domain name property.
    :type custom_domain: ~storage.models.CustomDomain
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'account_type': {'key': 'properties.accountType', 'type': 'AccountType'},
        'custom_domain': {'key': 'properties.customDomain', 'type': 'CustomDomain'},
    }

    def __init__(self, *, location: str, tags=None, account_type=None, custom_domain=None, **kwargs) -> None:
        super(StorageAccountUpdateParameters, self).__init__(location=location, tags=tags, **kwargs)
        self.account_type = account_type
        self.custom_domain = custom_domain
from msrest.serialization import Model


class StorageAccountRegenerateKeyParameters(Model):
    """StorageAccountRegenerateKeyParameters.

    :param key_name: Possible values include: 'key1', 'key2'
    :type key_name: str or ~storage.models.KeyName
    """

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'KeyName'},
    }

    def __init__(self, *, key_name=None, **kwargs) -> None:
        super(StorageAccountRegenerateKeyParameters, self).__init__(**kwargs)
        self.key_name = key_name
from msrest.serialization import Model


class UsageName(Model):
    """The Usage Names.

    :param value: Gets a string describing the resource name.
    :type value: str
    :param localized_value: Gets a localized string describing the resource
     name.
    :type localized_value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'localized_value': {'key': 'localizedValue', 'type': 'str'},
    }

    def __init__(self, *, value: str=None, localized_value: str=None, **kwargs) -> None:
        super(UsageName, self).__init__(**kwargs)
        self.value = value
        self.localized_value = localized_value
from msrest.serialization import Model


class Usage(Model):
    """Describes Storage Resource Usage.

    :param unit: Gets the unit of measurement. Possible values include:
     'Count', 'Bytes', 'Seconds', 'Percent', 'CountsPerSecond',
     'BytesPerSecond'
    :type unit: str or ~storage.models.UsageUnit
    :param current_value: Gets the current count of the allocated resources in
     the subscription.
    :type current_value: int
    :param limit: Gets the maximum count of the resources that can be
     allocated in the subscription.
    :type limit: int
    :param name: Gets the name of the type of usage.
    :type name: ~storage.models.UsageName
    """

    _attribute_map = {
        'unit': {'key': 'unit', 'type': 'UsageUnit'},
        'current_value': {'key': 'currentValue', 'type': 'int'},
        'limit': {'key': 'limit', 'type': 'int'},
        'name': {'key': 'name', 'type': 'UsageName'},
    }

    def __init__(self, *, unit=None, current_value: int=None, limit: int=None, name=None, **kwargs) -> None:
        super(Usage, self).__init__(**kwargs)
        self.unit = unit
        self.current_value = current_value
        self.limit = limit
        self.name = name
from msrest.serialization import Model


class UsageListResult(Model):
    """The List Usages operation response.

    :param value: Gets or sets the list Storage Resource Usages.
    :type value: list[~storage.models.Usage]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Usage]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(UsageListResult, self).__init__(**kwargs)
        self.value = value
from msrest.serialization import Model


class SubResource(Model):
    """SubResource.

    :param id: Resource Id
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, **kwargs) -> None:
        super(SubResource, self).__init__(**kwargs)
        self.id = id
from msrest.serialization import Model


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }
