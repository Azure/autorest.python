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


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class CustomParameterGroup(Model):
    """Additional parameters for
    get_multiple_pages_fragment_with_grouping_next_link operation.

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
        'api_version': {'key': '', 'type': 'str'},
        'tenant': {'key': '', 'type': 'str'},
    }

    def __init__(self, *, api_version: str, tenant: str, **kwargs) -> None:
        super(CustomParameterGroup, self).__init__(**kwargs)
        self.api_version = api_version
        self.tenant = tenant


class OdataProductResult(Model):
    """OdataProductResult.

    :param values:
    :type values: list[~paging.models.Product]
    :param odatanext_link:
    :type odatanext_link: str
    """

    _attribute_map = {
        'values': {'key': 'values', 'type': '[Product]'},
        'odatanext_link': {'key': 'odata\\.nextLink', 'type': 'str'},
    }

    def __init__(self, *, values=None, odatanext_link: str=None, **kwargs) -> None:
        super(OdataProductResult, self).__init__(**kwargs)
        self.values = values
        self.odatanext_link = odatanext_link


class OperationResult(Model):
    """OperationResult.

    :param status: The status of the request. Possible values include:
     'Succeeded', 'Failed', 'canceled', 'Accepted', 'Creating', 'Created',
     'Updating', 'Updated', 'Deleting', 'Deleted', 'OK'
    :type status: str or ~paging.models.enum
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, *, status=None, **kwargs) -> None:
        super(OperationResult, self).__init__(**kwargs)
        self.status = status


class PagingGetMultiplePagesLroOptions(Model):
    """Additional parameters for get_multiple_pages_lro operation.

    :param maxresults: Sets the maximum number of items to return in the
     response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing
     the request, in seconds. The default is 30 seconds. Default value: 30 .
    :type timeout: int
    """

    _attribute_map = {
        'maxresults': {'key': '', 'type': 'int'},
        'timeout': {'key': '', 'type': 'int'},
    }

    def __init__(self, *, maxresults: int=None, timeout: int=30, **kwargs) -> None:
        super(PagingGetMultiplePagesLroOptions, self).__init__(**kwargs)
        self.maxresults = maxresults
        self.timeout = timeout


class PagingGetMultiplePagesOptions(Model):
    """Additional parameters for get_multiple_pages operation.

    :param maxresults: Sets the maximum number of items to return in the
     response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing
     the request, in seconds. The default is 30 seconds. Default value: 30 .
    :type timeout: int
    """

    _attribute_map = {
        'maxresults': {'key': '', 'type': 'int'},
        'timeout': {'key': '', 'type': 'int'},
    }

    def __init__(self, *, maxresults: int=None, timeout: int=30, **kwargs) -> None:
        super(PagingGetMultiplePagesOptions, self).__init__(**kwargs)
        self.maxresults = maxresults
        self.timeout = timeout


class PagingGetMultiplePagesWithOffsetOptions(Model):
    """Additional parameters for get_multiple_pages_with_offset operation.

    All required parameters must be populated in order to send to Azure.

    :param maxresults: Sets the maximum number of items to return in the
     response.
    :type maxresults: int
    :param offset: Required. Offset of return value
    :type offset: int
    :param timeout: Sets the maximum time that the server can spend processing
     the request, in seconds. The default is 30 seconds. Default value: 30 .
    :type timeout: int
    """

    _validation = {
        'offset': {'required': True},
    }

    _attribute_map = {
        'maxresults': {'key': '', 'type': 'int'},
        'offset': {'key': '', 'type': 'int'},
        'timeout': {'key': '', 'type': 'int'},
    }

    def __init__(self, *, offset: int, maxresults: int=None, timeout: int=30, **kwargs) -> None:
        super(PagingGetMultiplePagesWithOffsetOptions, self).__init__(**kwargs)
        self.maxresults = maxresults
        self.offset = offset
        self.timeout = timeout


class PagingGetOdataMultiplePagesOptions(Model):
    """Additional parameters for get_odata_multiple_pages operation.

    :param maxresults: Sets the maximum number of items to return in the
     response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing
     the request, in seconds. The default is 30 seconds. Default value: 30 .
    :type timeout: int
    """

    _attribute_map = {
        'maxresults': {'key': '', 'type': 'int'},
        'timeout': {'key': '', 'type': 'int'},
    }

    def __init__(self, *, maxresults: int=None, timeout: int=30, **kwargs) -> None:
        super(PagingGetOdataMultiplePagesOptions, self).__init__(**kwargs)
        self.maxresults = maxresults
        self.timeout = timeout


class Product(Model):
    """Product.

    :param properties:
    :type properties: ~paging.models.ProductProperties
    """

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'ProductProperties'},
    }

    def __init__(self, *, properties=None, **kwargs) -> None:
        super(Product, self).__init__(**kwargs)
        self.properties = properties


class ProductProperties(Model):
    """ProductProperties.

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
    """ProductResult.

    :param values:
    :type values: list[~paging.models.Product]
    :param next_link:
    :type next_link: str
    """

    _attribute_map = {
        'values': {'key': 'values', 'type': '[Product]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, *, values=None, next_link: str=None, **kwargs) -> None:
        super(ProductResult, self).__init__(**kwargs)
        self.values = values
        self.next_link = next_link
