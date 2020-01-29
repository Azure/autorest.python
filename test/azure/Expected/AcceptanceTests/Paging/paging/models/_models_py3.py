# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Union

from msrest.serialization import Model


class CustomParameterGroup(Model):
    """Parameter group.

    All required parameters must be populated in order to send to Azure.

    :param api_version: Required. Sets the api version to use.
    :type api_version: str
    :param tenant: Required. Sets the tenant to use.
    :type tenant: str
    """

    _validation = {
        'api_version': {'required': True},
        'tenant': {'required': True},
    }

    _attribute_map = {
        'api_version': {'key': 'api_version', 'type': 'str'},
        'tenant': {'key': 'tenant', 'type': 'str'},
    }

    def __init__(self, *, api_version: str, tenant: str, **kwargs) -> None:
        super(CustomParameterGroup, self).__init__(**kwargs)
        self.api_version = api_version
        self.tenant = tenant


class OdataProductResult(Model):
    """

    :param values:
    :type values: list[~paging.models.Product]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'values': {'key': 'values', 'type': '[Product]'},
        'odata_next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
    }

    def __init__(self, *, values: List["Product"]=None, odata_next_link: str=None, **kwargs) -> None:
        super(OdataProductResult, self).__init__(**kwargs)
        self.values = values
        self.odata_next_link = odata_next_link


class OperationResult(Model):
    """

    :param status: The status of the request. Possible values include: 'Succeeded',
     'Failed', 'canceled', 'Accepted', 'Creating', 'Created', 'Updating', 'Updated',
     'Deleting', 'Deleted', 'OK'.
    :type status: str or ~paging.models.OperationResultStatus
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, *, status: Union[str, "OperationResultStatus"]=None, **kwargs) -> None:
        super(OperationResult, self).__init__(**kwargs)
        self.status = status


class PagingGetMultiplePagesLroOptions(Model):
    """Parameter group.

    :param maxresults: Sets the maximum number of items to return in the response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing the
     request, in seconds. The default is 30 seconds.
    :type timeout: int
    """

    _attribute_map = {
        'maxresults': {'key': 'maxresults', 'type': 'int'},
        'timeout': {'key': 'timeout', 'type': 'int'},
    }

    def __init__(self, *, maxresults: int=None, timeout: int=30, **kwargs) -> None:
        super(PagingGetMultiplePagesLroOptions, self).__init__(**kwargs)
        self.maxresults = maxresults
        self.timeout = timeout


class PagingGetMultiplePagesOptions(Model):
    """Parameter group.

    :param maxresults: Sets the maximum number of items to return in the response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing the
     request, in seconds. The default is 30 seconds.
    :type timeout: int
    """

    _attribute_map = {
        'maxresults': {'key': 'maxresults', 'type': 'int'},
        'timeout': {'key': 'timeout', 'type': 'int'},
    }

    def __init__(self, *, maxresults: int=None, timeout: int=30, **kwargs) -> None:
        super(PagingGetMultiplePagesOptions, self).__init__(**kwargs)
        self.maxresults = maxresults
        self.timeout = timeout


class PagingGetMultiplePagesWithOffsetOptions(Model):
    """Parameter group.

    All required parameters must be populated in order to send to Azure.

    :param maxresults: Sets the maximum number of items to return in the response.
    :type maxresults: int
    :param offset: Required. Offset of return value.
    :type offset: int
    :param timeout: Sets the maximum time that the server can spend processing the
     request, in seconds. The default is 30 seconds.
    :type timeout: int
    """

    _validation = {
        'offset': {'required': True},
    }

    _attribute_map = {
        'maxresults': {'key': 'maxresults', 'type': 'int'},
        'offset': {'key': 'offset', 'type': 'int'},
        'timeout': {'key': 'timeout', 'type': 'int'},
    }

    def __init__(self, *, offset: int, maxresults: int=None, timeout: int=30, **kwargs) -> None:
        super(PagingGetMultiplePagesWithOffsetOptions, self).__init__(**kwargs)
        self.maxresults = maxresults
        self.offset = offset
        self.timeout = timeout


class PagingGetOdataMultiplePagesOptions(Model):
    """Parameter group.

    :param maxresults: Sets the maximum number of items to return in the response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing the
     request, in seconds. The default is 30 seconds.
    :type timeout: int
    """

    _attribute_map = {
        'maxresults': {'key': 'maxresults', 'type': 'int'},
        'timeout': {'key': 'timeout', 'type': 'int'},
    }

    def __init__(self, *, maxresults: int=None, timeout: int=30, **kwargs) -> None:
        super(PagingGetOdataMultiplePagesOptions, self).__init__(**kwargs)
        self.maxresults = maxresults
        self.timeout = timeout


class Product(Model):
    """

    :param properties:
    :type properties: ~paging.models.ProductProperties
    """

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'ProductProperties'},
    }

    def __init__(self, *, properties: "ProductProperties"=None, **kwargs) -> None:
        super(Product, self).__init__(**kwargs)
        self.properties = properties


class ProductProperties(Model):
    """

    :param id:
    :type id: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, id: int=None, name: str=None, **kwargs) -> None:
        super(ProductProperties, self).__init__(**kwargs)
        self.id = id
        self.name = name


class ProductResult(Model):
    """

    :param values:
    :type values: list[~paging.models.Product]
    :param next_link:
    :type next_link: str
    """

    _attribute_map = {
        'values': {'key': 'values', 'type': '[Product]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, *, values: List["Product"]=None, next_link: str=None, **kwargs) -> None:
        super(ProductResult, self).__init__(**kwargs)
        self.values = values
        self.next_link = next_link


class ProductResultValue(Model):
    """

    :param value:
    :type value: list[~paging.models.Product]
    :param next_link:
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Product]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, *, value: List["Product"]=None, next_link: str=None, **kwargs) -> None:
        super(ProductResultValue, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link
