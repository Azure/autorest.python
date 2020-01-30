# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Bar(Model):
    """The URIs that are used to perform a retrieval of a public blob, queue or table object.

    :param recursive_point: The URIs that are used to perform a retrieval of a
     public blob, queue or table object.
    :type recursive_point: ~storage.models.Endpoints
    """

    _attribute_map = {
        'recursive_point': {'key': 'RecursivePoint', 'type': 'Endpoints'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Bar, self).__init__(**kwargs)
        self.recursive_point = kwargs.get('recursive_point', None)


class CheckNameAvailabilityResult(Model):
    """The CheckNameAvailability operation response.

    :param name_available: Gets a boolean value that indicates whether the name is
     available for you to use. If true, the name is available. If false, the name has
     already been taken or invalid and cannot be used.
    :type name_available: bool
    :param reason: Gets the reason that a storage account name could not be used.
     The Reason element is only returned if NameAvailable is false. Possible values
     include: 'AccountNameInvalid', 'AlreadyExists'.
    :type reason: str or ~storage.models.Reason
    :param message: Gets an error message explaining the Reason value in more
     detail.
    :type message: str
    """

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CheckNameAvailabilityResult, self).__init__(**kwargs)
        self.name_available = kwargs.get('name_available', None)
        self.reason = kwargs.get('reason', None)
        self.message = kwargs.get('message', None)


class CustomDomain(Model):
    """The custom domain assigned to this storage account. This can be set via Update.

    :param name: Gets or sets the custom domain name. Name is the CNAME source.
    :type name: str
    :param use_sub_domain: Indicates whether indirect CName validation is enabled.
     Default value is false. This should only be set on updates.
    :type use_sub_domain: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'use_sub_domain': {'key': 'useSubDomain', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CustomDomain, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.use_sub_domain = kwargs.get('use_sub_domain', None)


class Endpoints(Model):
    """The URIs that are used to perform a retrieval of a public blob, queue or table object.

    :param blob: Gets the blob endpoint.
    :type blob: str
    :param queue: Gets the queue endpoint.
    :type queue: str
    :param table: Gets the table endpoint.
    :type table: str
    :param dummy_end_point: The URIs that are used to perform a retrieval of a
     public blob, queue or table object.
    :type dummy_end_point: ~storage.models.Endpoints
    :param foo_point: The URIs that are used to perform a retrieval of a public
     blob, queue or table object.
    :type foo_point: ~storage.models.Foo
    """

    _attribute_map = {
        'blob': {'key': 'blob', 'type': 'str'},
        'queue': {'key': 'queue', 'type': 'str'},
        'table': {'key': 'table', 'type': 'str'},
        'dummy_end_point': {'key': 'dummyEndPoint', 'type': 'Endpoints'},
        'foo_point': {'key': 'FooPoint', 'type': 'Foo'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Endpoints, self).__init__(**kwargs)
        self.blob = kwargs.get('blob', None)
        self.queue = kwargs.get('queue', None)
        self.table = kwargs.get('table', None)
        self.dummy_end_point = kwargs.get('dummy_end_point', None)
        self.foo_point = kwargs.get('foo_point', None)


class Foo(Model):
    """The URIs that are used to perform a retrieval of a public blob, queue or table object.

    :param bar_point: The URIs that are used to perform a retrieval of a public
     blob, queue or table object.
    :type bar_point: ~storage.models.Bar
    """

    _attribute_map = {
        'bar_point': {'key': 'Bar\\.Point', 'type': 'Bar'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Foo, self).__init__(**kwargs)
        self.bar_point = kwargs.get('bar_point', None)


class Resource(Model):
    """Resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
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

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)


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
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param provisioning_state: Gets the status of the storage account at the time
     the operation was called. Possible values include: 'Creating', 'ResolvingDNS',
     'Succeeded'.
    :type provisioning_state: str or ~storage.models.ProvisioningState
    :param account_type: Gets or sets the account type. Possible values include:
     'Standard_LRS', 'Standard_ZRS', 'Standard_GRS', 'Standard_RAGRS', 'Premium_LRS'.
    :type account_type: str or ~storage.models.AccountType
    :param primary_endpoints: The URIs that are used to perform a retrieval of a
     public blob, queue or table object.
    :type primary_endpoints: ~storage.models.Endpoints
    :param primary_location: Gets the location of the primary for the storage
     account.
    :type primary_location: str
    :param status_of_primary: Gets the status indicating whether the primary
     location of the storage account is available or unavailable. Possible values
     include: 'Available', 'Unavailable'.
    :type status_of_primary: str or ~storage.models.AccountStatus
    :param last_geo_failover_time: Gets the timestamp of the most recent instance of
     a failover to the secondary location. Only the most recent timestamp is
     retained. This element is not returned if there has never been a failover
     instance. Only available if the accountType is StandardGRS or StandardRAGRS.
    :type last_geo_failover_time: ~datetime.datetime
    :param secondary_location: Gets the location of the geo replicated secondary for
     the storage account. Only available if the accountType is StandardGRS or
     StandardRAGRS.
    :type secondary_location: str
    :param status_of_secondary: Gets the status indicating whether the primary
     location of the storage account is available or unavailable. Possible values
     include: 'Available', 'Unavailable'.
    :type status_of_secondary: str or ~storage.models.AccountStatus
    :param creation_time: Gets the creation date and time of the storage account in
     UTC.
    :type creation_time: ~datetime.datetime
    :param custom_domain: The custom domain assigned to this storage account. This
     can be set via Update.
    :type custom_domain: ~storage.models.CustomDomain
    :param secondary_endpoints: The URIs that are used to perform a retrieval of a
     public blob, queue or table object.
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
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'account_type': {'key': 'properties.accountType', 'type': 'str'},
        'primary_endpoints': {'key': 'properties.primaryEndpoints', 'type': 'Endpoints'},
        'primary_location': {'key': 'properties.primaryLocation', 'type': 'str'},
        'status_of_primary': {'key': 'properties.statusOfPrimary', 'type': 'str'},
        'last_geo_failover_time': {'key': 'properties.lastGeoFailoverTime', 'type': 'iso-8601'},
        'secondary_location': {'key': 'properties.secondaryLocation', 'type': 'str'},
        'status_of_secondary': {'key': 'properties.statusOfSecondary', 'type': 'str'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'custom_domain': {'key': 'properties.customDomain', 'type': 'CustomDomain'},
        'secondary_endpoints': {'key': 'properties.secondaryEndpoints', 'type': 'Endpoints'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccount, self).__init__(**kwargs)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.account_type = kwargs.get('account_type', None)
        self.primary_endpoints = kwargs.get('primary_endpoints', None)
        self.primary_location = kwargs.get('primary_location', None)
        self.status_of_primary = kwargs.get('status_of_primary', None)
        self.last_geo_failover_time = kwargs.get('last_geo_failover_time', None)
        self.secondary_location = kwargs.get('secondary_location', None)
        self.status_of_secondary = kwargs.get('status_of_secondary', None)
        self.creation_time = kwargs.get('creation_time', None)
        self.custom_domain = kwargs.get('custom_domain', None)
        self.secondary_endpoints = kwargs.get('secondary_endpoints', None)


class StorageAccountCheckNameAvailabilityParameters(Model):
    """StorageAccountCheckNameAvailabilityParameters.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param type:
    :type type: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountCheckNameAvailabilityParameters, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', "Microsoft.Storage/storageAccounts")


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
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param account_type: Gets or sets the account type. Possible values include:
     'Standard_LRS', 'Standard_ZRS', 'Standard_GRS', 'Standard_RAGRS', 'Premium_LRS'.
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
        'account_type': {'key': 'properties.accountType', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountCreateParameters, self).__init__(**kwargs)
        self.account_type = kwargs.get('account_type', None)


class StorageAccountKeys(Model):
    """The access keys for the storage account.

    :param key1: Gets the value of key 1.
    :type key1: str
    :param key2: Gets the value of key 1.
    :type key2: str
    """

    _attribute_map = {
        'key1': {'key': 'key1', 'type': 'str'},
        'key2': {'key': 'key2', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountKeys, self).__init__(**kwargs)
        self.key1 = kwargs.get('key1', None)
        self.key2 = kwargs.get('key2', None)


class StorageAccountListResult(Model):
    """The list storage accounts operation response.

    :param value: Gets the list of storage accounts and their properties.
    :type value: list[~storage.models.StorageAccount]
    :param next_link: Gets the link to the next set of results. Currently this will
     always be empty as the API does not support pagination.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[StorageAccount]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class StorageAccountProperties(Model):
    """StorageAccountProperties.

    :param provisioning_state: Gets the status of the storage account at the time
     the operation was called. Possible values include: 'Creating', 'ResolvingDNS',
     'Succeeded'.
    :type provisioning_state: str or ~storage.models.ProvisioningState
    :param account_type: Gets or sets the account type. Possible values include:
     'Standard_LRS', 'Standard_ZRS', 'Standard_GRS', 'Standard_RAGRS', 'Premium_LRS'.
    :type account_type: str or ~storage.models.AccountType
    :param primary_endpoints: The URIs that are used to perform a retrieval of a
     public blob, queue or table object.
    :type primary_endpoints: ~storage.models.Endpoints
    :param primary_location: Gets the location of the primary for the storage
     account.
    :type primary_location: str
    :param status_of_primary: Gets the status indicating whether the primary
     location of the storage account is available or unavailable. Possible values
     include: 'Available', 'Unavailable'.
    :type status_of_primary: str or ~storage.models.AccountStatus
    :param last_geo_failover_time: Gets the timestamp of the most recent instance of
     a failover to the secondary location. Only the most recent timestamp is
     retained. This element is not returned if there has never been a failover
     instance. Only available if the accountType is StandardGRS or StandardRAGRS.
    :type last_geo_failover_time: ~datetime.datetime
    :param secondary_location: Gets the location of the geo replicated secondary for
     the storage account. Only available if the accountType is StandardGRS or
     StandardRAGRS.
    :type secondary_location: str
    :param status_of_secondary: Gets the status indicating whether the primary
     location of the storage account is available or unavailable. Possible values
     include: 'Available', 'Unavailable'.
    :type status_of_secondary: str or ~storage.models.AccountStatus
    :param creation_time: Gets the creation date and time of the storage account in
     UTC.
    :type creation_time: ~datetime.datetime
    :param custom_domain: The custom domain assigned to this storage account. This
     can be set via Update.
    :type custom_domain: ~storage.models.CustomDomain
    :param secondary_endpoints: The URIs that are used to perform a retrieval of a
     public blob, queue or table object.
    :type secondary_endpoints: ~storage.models.Endpoints
    """

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'account_type': {'key': 'accountType', 'type': 'str'},
        'primary_endpoints': {'key': 'primaryEndpoints', 'type': 'Endpoints'},
        'primary_location': {'key': 'primaryLocation', 'type': 'str'},
        'status_of_primary': {'key': 'statusOfPrimary', 'type': 'str'},
        'last_geo_failover_time': {'key': 'lastGeoFailoverTime', 'type': 'iso-8601'},
        'secondary_location': {'key': 'secondaryLocation', 'type': 'str'},
        'status_of_secondary': {'key': 'statusOfSecondary', 'type': 'str'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'custom_domain': {'key': 'customDomain', 'type': 'CustomDomain'},
        'secondary_endpoints': {'key': 'secondaryEndpoints', 'type': 'Endpoints'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountProperties, self).__init__(**kwargs)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.account_type = kwargs.get('account_type', None)
        self.primary_endpoints = kwargs.get('primary_endpoints', None)
        self.primary_location = kwargs.get('primary_location', None)
        self.status_of_primary = kwargs.get('status_of_primary', None)
        self.last_geo_failover_time = kwargs.get('last_geo_failover_time', None)
        self.secondary_location = kwargs.get('secondary_location', None)
        self.status_of_secondary = kwargs.get('status_of_secondary', None)
        self.creation_time = kwargs.get('creation_time', None)
        self.custom_domain = kwargs.get('custom_domain', None)
        self.secondary_endpoints = kwargs.get('secondary_endpoints', None)


class StorageAccountPropertiesCreateParameters(Model):
    """StorageAccountPropertiesCreateParameters.

    :param account_type: Gets or sets the account type. Possible values include:
     'Standard_LRS', 'Standard_ZRS', 'Standard_GRS', 'Standard_RAGRS', 'Premium_LRS'.
    :type account_type: str or ~storage.models.AccountType
    """

    _attribute_map = {
        'account_type': {'key': 'accountType', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountPropertiesCreateParameters, self).__init__(**kwargs)
        self.account_type = kwargs.get('account_type', None)


class StorageAccountPropertiesUpdateParameters(Model):
    """StorageAccountPropertiesUpdateParameters.

    :param account_type: Gets or sets the account type. Possible values include:
     'Standard_LRS', 'Standard_ZRS', 'Standard_GRS', 'Standard_RAGRS', 'Premium_LRS'.
    :type account_type: str or ~storage.models.AccountType
    :param custom_domain: The custom domain assigned to this storage account. This
     can be set via Update.
    :type custom_domain: ~storage.models.CustomDomain
    """

    _attribute_map = {
        'account_type': {'key': 'accountType', 'type': 'str'},
        'custom_domain': {'key': 'customDomain', 'type': 'CustomDomain'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountPropertiesUpdateParameters, self).__init__(**kwargs)
        self.account_type = kwargs.get('account_type', None)
        self.custom_domain = kwargs.get('custom_domain', None)


class StorageAccountRegenerateKeyParameters(Model):
    """StorageAccountRegenerateKeyParameters.

    :param key_name:  Possible values include: 'key1', 'key2'.
    :type key_name: str or ~storage.models.KeyName
    """

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountRegenerateKeyParameters, self).__init__(**kwargs)
        self.key_name = kwargs.get('key_name', None)


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
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param account_type: Gets or sets the account type. Possible values include:
     'Standard_LRS', 'Standard_ZRS', 'Standard_GRS', 'Standard_RAGRS', 'Premium_LRS'.
    :type account_type: str or ~storage.models.AccountType
    :param custom_domain: The custom domain assigned to this storage account. This
     can be set via Update.
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
        'account_type': {'key': 'properties.accountType', 'type': 'str'},
        'custom_domain': {'key': 'properties.customDomain', 'type': 'CustomDomain'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageAccountUpdateParameters, self).__init__(**kwargs)
        self.account_type = kwargs.get('account_type', None)
        self.custom_domain = kwargs.get('custom_domain', None)


class SubResource(Model):
    """SubResource.

    :param id: Resource Id.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SubResource, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)


class Usage(Model):
    """Describes Storage Resource Usage.

    :param unit: Gets the unit of measurement. Possible values include: 'Count',
     'Bytes', 'Seconds', 'Percent', 'CountsPerSecond', 'BytesPerSecond'.
    :type unit: str or ~storage.models.UsageUnit
    :param current_value: Gets the current count of the allocated resources in the
     subscription.
    :type current_value: int
    :param limit: Gets the maximum count of the resources that can be allocated in
     the subscription.
    :type limit: int
    :param name: The Usage Names.
    :type name: ~storage.models.UsageName
    """

    _attribute_map = {
        'unit': {'key': 'unit', 'type': 'str'},
        'current_value': {'key': 'currentValue', 'type': 'int'},
        'limit': {'key': 'limit', 'type': 'int'},
        'name': {'key': 'name', 'type': 'UsageName'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Usage, self).__init__(**kwargs)
        self.unit = kwargs.get('unit', None)
        self.current_value = kwargs.get('current_value', None)
        self.limit = kwargs.get('limit', None)
        self.name = kwargs.get('name', None)


class UsageListResult(Model):
    """The List Usages operation response.

    :param value: Gets or sets the list Storage Resource Usages.
    :type value: list[~storage.models.Usage]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Usage]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(UsageListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class UsageName(Model):
    """The Usage Names.

    :param value: Gets a string describing the resource name.
    :type value: str
    :param localized_value: Gets a localized string describing the resource name.
    :type localized_value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'localized_value': {'key': 'localizedValue', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(UsageName, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.localized_value = kwargs.get('localized_value', None)
