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

from .resource import Resource


class StorageAccountUpdateParameters(Resource):
    """The parameters to update on the account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
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
        'account_type': {'key': 'properties.accountType', 'type': 'str', 'enum':'AccountType'},
        'custom_domain': {'key': 'properties.customDomain', 'type': 'CustomDomain'},
    }

    def __init__(self, **kwargs):
        super(StorageAccountUpdateParameters, self).__init__(**kwargs)
        self.account_type = kwargs.get('account_type', None)
        self.custom_domain = kwargs.get('custom_domain', None)
