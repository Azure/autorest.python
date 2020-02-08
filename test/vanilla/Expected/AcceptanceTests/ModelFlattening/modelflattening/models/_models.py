# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class BaseProduct(msrest.serialization.Model):
    """The product documentation.

    All required parameters must be populated in order to send to Azure.

    :param product_id: Required. Unique identifier representing a specific product for a given
     latitude & longitude. For example, uberX in San Francisco will have a different product_id than
     uberX in Los Angeles.
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

    def __init__(
        self,
        **kwargs
    ):
        super(BaseProduct, self).__init__(**kwargs)
        self.product_id = kwargs.get('product_id', None)
        self.description = kwargs.get('description', None)


class Error(msrest.serialization.Model):
    """Error.

    :param status:
    :type status: int
    :param message:
    :type message: str
    :param parent_error:
    :type parent_error: ~modelflattening.models.Error
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'parent_error': {'key': 'parentError', 'type': 'Error'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.message = kwargs.get('message', None)
        self.parent_error = kwargs.get('parent_error', None)


class Resource(msrest.serialization.Model):
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

    def __init__(
        self,
        **kwargs
    ):
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
    :param p_name:
    :type p_name: str
    :param type_properties_type:
    :type type_properties_type: str
    :ivar provisioning_state_values:  Possible values include: 'Succeeded', 'Failed', 'canceled',
     'Accepted', 'Creating', 'Created', 'Updating', 'Updated', 'Deleting', 'Deleted', 'OK'.
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
        'p_name': {'key': 'properties.p\\.name', 'type': 'str'},
        'type_properties_type': {'key': 'properties.type', 'type': 'str'},
        'provisioning_state_values': {'key': 'properties.provisioningStateValues', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FlattenedProduct, self).__init__(**kwargs)
        self.p_name = kwargs.get('p_name', None)
        self.type_properties_type = kwargs.get('type_properties_type', None)
        self.provisioning_state_values = None
        self.provisioning_state = kwargs.get('provisioning_state', None)


class FlattenedProductProperties(msrest.serialization.Model):
    """FlattenedProductProperties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param p_name:
    :type p_name: str
    :param type:
    :type type: str
    :ivar provisioning_state_values:  Possible values include: 'Succeeded', 'Failed', 'canceled',
     'Accepted', 'Creating', 'Created', 'Updating', 'Updated', 'Deleting', 'Deleted', 'OK'.
    :vartype provisioning_state_values: str or
     ~modelflattening.models.FlattenedProductPropertiesProvisioningStateValues
    :param provisioning_state:
    :type provisioning_state: str
    """

    _validation = {
        'provisioning_state_values': {'readonly': True},
    }

    _attribute_map = {
        'p_name': {'key': 'p\\.name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state_values': {'key': 'provisioningStateValues', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FlattenedProductProperties, self).__init__(**kwargs)
        self.p_name = kwargs.get('p_name', None)
        self.type = kwargs.get('type', None)
        self.provisioning_state_values = None
        self.provisioning_state = kwargs.get('provisioning_state', None)


class FlattenParameterGroup(msrest.serialization.Model):
    """Parameter group.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Product name with value 'groupproduct'.
    :type name: str
    :param simple_body_product: Simple body product to put.
    :type simple_body_product: ~modelflattening.models.SimpleProduct
    :param product_id: Required. Unique identifier representing a specific product for a given
     latitude & longitude. For example, uberX in San Francisco will have a different product_id than
     uberX in Los Angeles.
    :type product_id: str
    :param description: Description of product.
    :type description: str
    :param max_product_display_name: Display name of product.
    :type max_product_display_name: str
    :ivar capacity: Capacity of product. For example, 4 people. Default value: "Large".
    :vartype capacity: str
    :param generic_value: Generic URL value.
    :type generic_value: str
    :param odatavalue: URL value.
    :type odatavalue: str
    """

    _validation = {
        'name': {'required': True},
        'product_id': {'required': True},
        'capacity': {'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'simple_body_product': {'key': 'SimpleBodyProduct', 'type': 'SimpleProduct'},
        'product_id': {'key': 'productId', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'max_product_display_name': {'key': 'max_product_display_name', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'str'},
        'generic_value': {'key': 'generic_value', 'type': 'str'},
        'odatavalue': {'key': '@odata\\.value', 'type': 'str'},
    }

    capacity = "Large"

    def __init__(
        self,
        **kwargs
    ):
        super(FlattenParameterGroup, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.simple_body_product = kwargs.get('simple_body_product', None)
        self.product_id = kwargs.get('product_id', None)
        self.description = kwargs.get('description', None)
        self.max_product_display_name = kwargs.get('max_product_display_name', None)
        self.generic_value = kwargs.get('generic_value', None)
        self.odatavalue = kwargs.get('odatavalue', None)


class GenericUrl(msrest.serialization.Model):
    """The Generic URL.

    :param generic_value: Generic URL value.
    :type generic_value: str
    """

    _attribute_map = {
        'generic_value': {'key': 'generic_value', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(GenericUrl, self).__init__(**kwargs)
        self.generic_value = kwargs.get('generic_value', None)


class ProductUrl(GenericUrl):
    """The product URL.

    :param generic_value: Generic URL value.
    :type generic_value: str
    :param odata_value: URL value.
    :type odata_value: str
    """

    _attribute_map = {
        'generic_value': {'key': 'generic_value', 'type': 'str'},
        'odata_value': {'key': '@odata\\.value', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProductUrl, self).__init__(**kwargs)
        self.odata_value = kwargs.get('odata_value', None)


class ProductWrapper(msrest.serialization.Model):
    """The wrapped produc.

    :param value: the product value.
    :type value: str
    """

    _attribute_map = {
        'value': {'key': 'property.value', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProductWrapper, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class ResourceCollection(msrest.serialization.Model):
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

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceCollection, self).__init__(**kwargs)
        self.productresource = kwargs.get('productresource', None)
        self.arrayofresources = kwargs.get('arrayofresources', None)
        self.dictionaryofresources = kwargs.get('dictionaryofresources', None)


class SimpleProduct(BaseProduct):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param product_id: Required. Unique identifier representing a specific product for a given
     latitude & longitude. For example, uberX in San Francisco will have a different product_id than
     uberX in Los Angeles.
    :type product_id: str
    :param description: Description of product.
    :type description: str
    :param max_product_display_name: Display name of product.
    :type max_product_display_name: str
    :ivar capacity: Capacity of product. For example, 4 people. Default value: "Large".
    :vartype capacity: str
    :param generic_value: Generic URL value.
    :type generic_value: str
    :param odata_value: URL value.
    :type odata_value: str
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
        'generic_value': {'key': 'details.max_product_image.generic_value', 'type': 'str'},
        'odata_value': {'key': 'details.max_product_image.@odata\\.value', 'type': 'str'},
    }

    capacity = "Large"

    def __init__(
        self,
        **kwargs
    ):
        super(SimpleProduct, self).__init__(**kwargs)
        self.max_product_display_name = kwargs.get('max_product_display_name', None)
        self.generic_value = kwargs.get('generic_value', None)
        self.odata_value = kwargs.get('odata_value', None)


class SimpleProductProperties(msrest.serialization.Model):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param max_product_display_name: Required. Display name of product.
    :type max_product_display_name: str
    :ivar capacity: Required. Capacity of product. For example, 4 people. Default value: "Large".
    :vartype capacity: str
    :param generic_value: Generic URL value.
    :type generic_value: str
    :param odata_value: URL value.
    :type odata_value: str
    """

    _validation = {
        'max_product_display_name': {'required': True},
        'capacity': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'max_product_display_name': {'key': 'max_product_display_name', 'type': 'str'},
        'capacity': {'key': 'max_product_capacity', 'type': 'str'},
        'generic_value': {'key': 'max_product_image.generic_value', 'type': 'str'},
        'odata_value': {'key': 'max_product_image.@odata\\.value', 'type': 'str'},
    }

    capacity = "Large"

    def __init__(
        self,
        **kwargs
    ):
        super(SimpleProductProperties, self).__init__(**kwargs)
        self.max_product_display_name = kwargs.get('max_product_display_name', None)
        self.generic_value = kwargs.get('generic_value', None)
        self.odata_value = kwargs.get('odata_value', None)


class WrappedProduct(msrest.serialization.Model):
    """The wrapped produc.

    :param value: the product value.
    :type value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(WrappedProduct, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
