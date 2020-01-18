# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List

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

    def __init__(self, *, product_id: str, description: str=None, **kwargs) -> None:
        super(BaseProduct, self).__init__(**kwargs)
        self.product_id = product_id
        self.description = description


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

    def __init__(self, *, status: int=None, message: str=None, parent_error: "Error"=None, **kwargs) -> None:
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message
        self.parent_error = parent_error


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

    def __init__(self, *, tags: Dict[str, str]=None, location: str=None, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.tags = tags
        self.location = location
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
    :param pname:
    :type pname: str
    :ivar provisioning_state_values:  Possible values include: 'Succeeded',
     'Failed', 'canceled', 'Accepted', 'Creating', 'Created', 'Updating', 'Updated',
     'Deleting', 'Deleted', 'OK'.
    :vartype provisioning_state_values: str or
     ~modelflattening.models.FlattenedProductPropertiesProvisioningStateValues
    :param provisioning_state:
    :type provisioning_state: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'provisioning_state_values': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'pname': {'key': 'properties.p\\.name', 'type': 'str'},
        'provisioning_state_values': {'key': 'properties.provisioningStateValues', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, tags: Dict[str, str]=None, location: str=None, pname: str=None, provisioning_state: str=None, **kwargs) -> None:
        super(FlattenedProduct, self).__init__(tags=tags, location=location, **kwargs)
        self.pname = pname
        self.provisioning_state = provisioning_state


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

    def __init__(self, *, pname: str=None, type: str=None, provisioning_state: str=None, **kwargs) -> None:
        super(FlattenedProductProperties, self).__init__(**kwargs)
        self.pname = pname
        self.type = type
        self.provisioning_state_values = None
        self.provisioning_state = provisioning_state


class GenericUrl(Model):
    """The Generic URL.

    :param generic_value: Generic URL value.
    :type generic_value: str
    """

    _attribute_map = {
        'generic_value': {'key': 'generic_value', 'type': 'str'},
    }

    def __init__(self, *, generic_value: str=None, **kwargs) -> None:
        super(GenericUrl, self).__init__(**kwargs)
        self.generic_value = generic_value


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

    def __init__(self, *, generic_value: str=None, odatavalue: str=None, **kwargs) -> None:
        super(ProductUrl, self).__init__(generic_value=generic_value, **kwargs)
        self.odatavalue = odatavalue


class ProductWrapper(Model):
    """The wrapped produc.

    :param value: the product value.
    :type value: str
    """

    _attribute_map = {
        'value': {'key': 'property.value', 'type': 'str'},
    }

    def __init__(self, *, value: str=None, **kwargs) -> None:
        super(ProductWrapper, self).__init__(**kwargs)
        self.value = value


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

    def __init__(self, *, productresource: "FlattenedProduct"=None, arrayofresources: List["FlattenedProduct"]=None, dictionaryofresources: Dict[str, "FlattenedProduct"]=None, **kwargs) -> None:
        super(ResourceCollection, self).__init__(**kwargs)
        self.productresource = productresource
        self.arrayofresources = arrayofresources
        self.dictionaryofresources = dictionaryofresources


class SimpleProduct(BaseProduct):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param product_id: Required. Unique identifier representing a specific product
     for a given latitude & longitude. For example, uberX in San Francisco will have
     a different product_id than uberX in Los Angeles.
    :type product_id: str
    :param description: Description of product.
    :type description: str
    :param max_product_display_name: Display name of product.
    :type max_product_display_name: str
    :ivar capacity: Capacity of product. For example, 4 people. Default value:
     "Large".
    :vartype capacity: str
    :param odatavalue: URL value.
    :type odatavalue: str
    """

    _validation = {
        'product_id': {'required': True},
        'capacity': {'constant': True},
    }

    _attribute_map = {
        'product_id': {'key': 'base_product_id', 'type': 'str'},
        'description': {'key': 'base_product_description', 'type': 'str'},
        'max_product_display_name': {'key': 'details.max_product_display_name', 'type': 'str'},
        'capacity': {'key': 'details.max_product_capacity', 'type': 'str'},
        'odatavalue': {'key': 'details.max_product_image.@odata\\.value', 'type': 'str'},
    }

    capacity = "Large"

    def __init__(self, *, product_id: str, description: str=None, max_product_display_name: str=None, odatavalue: str=None, **kwargs) -> None:
        super(SimpleProduct, self).__init__(product_id=product_id, description=description, **kwargs)
        self.max_product_display_name = max_product_display_name
        self.odatavalue = odatavalue


class SimpleProductProperties(Model):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param max_product_display_name: Required. Display name of product.
    :type max_product_display_name: str
    :ivar capacity: Required. Capacity of product. For example, 4 people. Default
     value: "Large".
    :vartype capacity: str
    :param odatavalue: URL value.
    :type odatavalue: str
    """

    _validation = {
        'max_product_display_name': {'required': True},
        'capacity': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'max_product_display_name': {'key': 'max_product_display_name', 'type': 'str'},
        'capacity': {'key': 'max_product_capacity', 'type': 'str'},
        'odatavalue': {'key': 'max_product_image.@odata\\.value', 'type': 'str'},
    }

    capacity = "Large"

    def __init__(self, *, max_product_display_name: str, odatavalue: str=None, **kwargs) -> None:
        super(SimpleProductProperties, self).__init__(**kwargs)
        self.max_product_display_name = max_product_display_name
        self.odatavalue = odatavalue


class WrappedProduct(Model):
    """The wrapped produc.

    :param value: the product value.
    :type value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, *, value: str=None, **kwargs) -> None:
        super(WrappedProduct, self).__init__(**kwargs)
        self.value = value
