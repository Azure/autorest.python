# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional

from azure.core.exceptions import HttpResponseError
from msrest.serialization import Model


class BaseProduct(Model):
    """The product documentation.

    All required parameters must be populated in order to send to Azure.

    :param product_id: Required. Unique identifier representing a specific product
     for a given latitude & longitude. For example, uberX in San Francisco will have
     a different product_id than uberX in Los Angeles.
    :type product_id: str
    :param description: Description of product.
    :type description: str
    """

    _validation = {
        'product_id': {'required': True},
    }

    _attribute_map = {
        'product_id': {'key': 'base_product_id', 'type': 'str'},
        'description': {'key': 'base_product_description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BaseProduct, self).__init__(**kwargs)
        self.product_id = kwargs.get('product_id', None)
        self.description = kwargs.get('description', None)


class ErrorException(HttpResponseError):
    """Server responded with exception of type: 'Error'.

    :param response: Server response to be deserialized.
    :param error_model: A deserialized model of the response body as model.
    """

    def __init__(self, response, error_model):
        self.error = error_model
        super(ErrorException, self).__init__(response=response, error_model=error_model)

    @classmethod
    def from_response(cls, response, deserialize):
        """Deserialize this response as this exception, or a subclass of this exception.

        :param response: Server response to be deserialized.
        :param deserialize: A deserializer
        """
        model_name = 'Error'
        error = deserialize(model_name, response)
        if error is None:
            error = deserialize.dependencies[model_name]()
        return error._EXCEPTION_TYPE(response, error)


class Error(Model):
    """Error.

    :param status:
    :type status: int
    :param message:
    :type message: str
    :param parent_error:
    :type parent_error: ~modelflattening.models.Error
    """
    _EXCEPTION_TYPE = ErrorException

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'parent_error': {'key': 'parentError', 'type': 'Error'},
    }

    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.message = kwargs.get('message', None)
        self.parent_error = kwargs.get('parent_error', None)


class Resource(Model):
    """Resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar type: Resource Type.
    :vartype type: str
    :param tags: A set of tags. Dictionary of
     <components·schemas·resource·properties·tags·additionalproperties>.
    :type tags: dict[str, str]
    :param location: Resource Location.
    :type location: str
    :ivar name: Resource Name.
    :vartype name: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.tags = kwargs.get('tags', None)
        self.location = kwargs.get('location', None)
        self.name = None


class FlattenedProduct(Resource):
    """Flattened product.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar type: Resource Type.
    :vartype type: str
    :param tags: A set of tags. Dictionary of
     <components·schemas·resource·properties·tags·additionalproperties>.
    :type tags: dict[str, str]
    :param location: Resource Location.
    :type location: str
    :ivar name: Resource Name.
    :vartype name: str
    :param properties:
    :type properties: ~modelflattening.models.FlattenedProductProperties
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'FlattenedProductProperties'},
    }

    def __init__(self, **kwargs):
        super(FlattenedProduct, self).__init__(**kwargs)
        self.properties = kwargs.get('properties', None)


class FlattenedProductProperties(Model):
    """FlattenedProductProperties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param pname:
    :type pname: str
    :param type:
    :type type: str
    :ivar provisioning_state_values:  Possible values include: 'Succeeded',
     'Failed', 'canceled', 'Accepted', 'Creating', 'Created', 'Updating', 'Updated',
     'Deleting', 'Deleted', 'OK'.
    :vartype provisioning_state_values: str or
     ~modelflattening.models.FlattenedProductPropertiesProvisioningStateValues
    :param provisioning_state:
    :type provisioning_state: str
    """

    _validation = {
        'provisioning_state_values': {'readonly': True},
    }

    _attribute_map = {
        'pname': {'key': 'p\\.name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state_values': {'key': 'provisioningStateValues', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(FlattenedProductProperties, self).__init__(**kwargs)
        self.pname = kwargs.get('pname', None)
        self.type = kwargs.get('type', None)
        self.provisioning_state_values = None
        self.provisioning_state = kwargs.get('provisioning_state', None)


class GenericUrl(Model):
    """The Generic URL.

    :param generic_value: Generic URL value.
    :type generic_value: str
    """

    _attribute_map = {
        'generic_value': {'key': 'generic_value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(GenericUrl, self).__init__(**kwargs)
        self.generic_value = kwargs.get('generic_value', None)


class ProductUrl(GenericUrl):
    """The product URL.

    :param generic_value: Generic URL value.
    :type generic_value: str
    :param odatavalue: URL value.
    :type odatavalue: str
    """

    _attribute_map = {
        'generic_value': {'key': 'generic_value', 'type': 'str'},
        'odatavalue': {'key': '@odata\\.value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ProductUrl, self).__init__(**kwargs)
        self.odatavalue = kwargs.get('odatavalue', None)


class ProductWrapper(Model):
    """The wrapped produc.

    :param property: The wrapped produc.
    :type property: ~modelflattening.models.WrappedProduct
    """

    _attribute_map = {
        'property': {'key': 'property', 'type': 'WrappedProduct'},
    }

    def __init__(self, **kwargs):
        super(ProductWrapper, self).__init__(**kwargs)
        self.property = kwargs.get('property', None)


class ResourceCollection(Model):
    """ResourceCollection.

    :param productresource: Flattened product.
    :type productresource: ~modelflattening.models.FlattenedProduct
    :param arrayofresources:
    :type arrayofresources: list[~modelflattening.models.FlattenedProduct]
    :param dictionaryofresources: Dictionary of :code:`<FlattenedProduct>`.
    :type dictionaryofresources: dict[str, ~modelflattening.models.FlattenedProduct]
    """

    _attribute_map = {
        'productresource': {'key': 'productresource', 'type': 'FlattenedProduct'},
        'arrayofresources': {'key': 'arrayofresources', 'type': '[FlattenedProduct]'},
        'dictionaryofresources': {'key': 'dictionaryofresources', 'type': '{FlattenedProduct}'},
    }

    def __init__(self, **kwargs):
        super(ResourceCollection, self).__init__(**kwargs)
        self.productresource = kwargs.get('productresource', None)
        self.arrayofresources = kwargs.get('arrayofresources', None)
        self.dictionaryofresources = kwargs.get('dictionaryofresources', None)


class SimpleProduct(BaseProduct):
    """The product documentation.

    All required parameters must be populated in order to send to Azure.

    :param product_id: Required. Unique identifier representing a specific product
     for a given latitude & longitude. For example, uberX in San Francisco will have
     a different product_id than uberX in Los Angeles.
    :type product_id: str
    :param description: Description of product.
    :type description: str
    :param details: The product documentation.
    :type details: ~modelflattening.models.SimpleProductProperties
    """

    _validation = {
        'product_id': {'required': True},
    }

    _attribute_map = {
        'product_id': {'key': 'base_product_id', 'type': 'str'},
        'description': {'key': 'base_product_description', 'type': 'str'},
        'details': {'key': 'details', 'type': 'SimpleProductProperties'},
    }

    def __init__(self, **kwargs):
        super(SimpleProduct, self).__init__(**kwargs)
        self.details = kwargs.get('details', None)


class SimpleProductProperties(Model):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param max_product_display_name: Required. Display name of product.
    :type max_product_display_name: str
    :ivar capacity: Required. Capacity of product. For example, 4 people. Default
     value: "Large".
    :vartype capacity: str
    :param max_product_image: The product URL.
    :type max_product_image: ~modelflattening.models.ProductUrl
    """

    _validation = {
        'max_product_display_name': {'required': True},
        'capacity': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'max_product_display_name': {'key': 'max_product_display_name', 'type': 'str'},
        'capacity': {'key': 'max_product_capacity', 'type': 'str'},
        'max_product_image': {'key': 'max_product_image', 'type': 'ProductUrl'},
    }

    capacity = "Large"

    def __init__(self, **kwargs):
        super(SimpleProductProperties, self).__init__(**kwargs)
        self.max_product_display_name = kwargs.get('max_product_display_name', None)
        self.max_product_image = kwargs.get('max_product_image', None)


class WrappedProduct(Model):
    """The wrapped produc.

    :param value: the product value.
    :type value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(WrappedProduct, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
