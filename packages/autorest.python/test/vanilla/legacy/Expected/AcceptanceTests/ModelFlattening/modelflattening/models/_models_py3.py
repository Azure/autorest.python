# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Dict, List, Optional, TYPE_CHECKING

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports

from .. import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class BaseProduct(_serialization.Model):
    """The product documentation.

    All required parameters must be populated in order to send to Azure.

    :ivar product_id: Unique identifier representing a specific product for a given latitude &
     longitude. For example, uberX in San Francisco will have a different product_id than uberX in
     Los Angeles. Required.
    :vartype product_id: str
    :ivar description: Description of product.
    :vartype description: str
    """

    _validation = {
        "product_id": {"required": True},
    }

    _attribute_map = {
        "product_id": {"key": "base_product_id", "type": "str"},
        "description": {"key": "base_product_description", "type": "str"},
    }

    def __init__(self, *, product_id: str, description: Optional[str] = None, **kwargs):
        """
        :keyword product_id: Unique identifier representing a specific product for a given latitude &
         longitude. For example, uberX in San Francisco will have a different product_id than uberX in
         Los Angeles. Required.
        :paramtype product_id: str
        :keyword description: Description of product.
        :paramtype description: str
        """
        super().__init__(**kwargs)
        self.product_id = product_id
        self.description = description


class Error(_serialization.Model):
    """Error.

    :ivar status:
    :vartype status: int
    :ivar message:
    :vartype message: str
    :ivar parent_error:
    :vartype parent_error: ~modelflattening.models.Error
    """

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "message": {"key": "message", "type": "str"},
        "parent_error": {"key": "parentError", "type": "Error"},
    }

    def __init__(
        self,
        *,
        status: Optional[int] = None,
        message: Optional[str] = None,
        parent_error: Optional["_models.Error"] = None,
        **kwargs
    ):
        """
        :keyword status:
        :paramtype status: int
        :keyword message:
        :paramtype message: str
        :keyword parent_error:
        :paramtype parent_error: ~modelflattening.models.Error
        """
        super().__init__(**kwargs)
        self.status = status
        self.message = message
        self.parent_error = parent_error


class Resource(_serialization.Model):
    """Resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar type: Resource Type.
    :vartype type: str
    :ivar tags: Dictionary of :code:`<string>`.
    :vartype tags: dict[str, str]
    :ivar location: Resource Location.
    :vartype location: str
    :ivar name: Resource Name.
    :vartype name: str
    """

    _validation = {
        "id": {"readonly": True},
        "type": {"readonly": True},
        "name": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
        "name": {"key": "name", "type": "str"},
    }

    def __init__(self, *, tags: Optional[Dict[str, str]] = None, location: Optional[str] = None, **kwargs):
        """
        :keyword tags: Dictionary of :code:`<string>`.
        :paramtype tags: dict[str, str]
        :keyword location: Resource Location.
        :paramtype location: str
        """
        super().__init__(**kwargs)
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
    :ivar tags: Dictionary of :code:`<string>`.
    :vartype tags: dict[str, str]
    :ivar location: Resource Location.
    :vartype location: str
    :ivar name: Resource Name.
    :vartype name: str
    :ivar p_name:
    :vartype p_name: str
    :ivar type_properties_type:
    :vartype type_properties_type: str
    :ivar provisioning_state_values: Known values are: "Succeeded", "Failed", "canceled",
     "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", and "OK".
    :vartype provisioning_state_values: str or
     ~modelflattening.models.FlattenedProductPropertiesProvisioningStateValues
    :ivar provisioning_state:
    :vartype provisioning_state: str
    """

    _validation = {
        "id": {"readonly": True},
        "type": {"readonly": True},
        "name": {"readonly": True},
        "provisioning_state_values": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "p_name": {"key": "properties.p\\.name", "type": "str"},
        "type_properties_type": {"key": "properties.type", "type": "str"},
        "provisioning_state_values": {"key": "properties.provisioningStateValues", "type": "str"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        location: Optional[str] = None,
        p_name: Optional[str] = None,
        type_properties_type: Optional[str] = None,
        provisioning_state: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword tags: Dictionary of :code:`<string>`.
        :paramtype tags: dict[str, str]
        :keyword location: Resource Location.
        :paramtype location: str
        :keyword p_name:
        :paramtype p_name: str
        :keyword type_properties_type:
        :paramtype type_properties_type: str
        :keyword provisioning_state:
        :paramtype provisioning_state: str
        """
        super().__init__(tags=tags, location=location, **kwargs)
        self.p_name = p_name
        self.type_properties_type = type_properties_type
        self.provisioning_state_values = None
        self.provisioning_state = provisioning_state


class FlattenParameterGroup(_serialization.Model):
    """Parameter group.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Product name with value 'groupproduct'. Required.
    :vartype name: str
    :ivar simple_body_product: Simple body product to put.
    :vartype simple_body_product: ~modelflattening.models.SimpleProduct
    :ivar product_id: Unique identifier representing a specific product for a given latitude &
     longitude. For example, uberX in San Francisco will have a different product_id than uberX in
     Los Angeles. Required.
    :vartype product_id: str
    :ivar description: Description of product.
    :vartype description: str
    :ivar max_product_display_name: Display name of product.
    :vartype max_product_display_name: str
    :ivar capacity: Capacity of product. For example, 4 people. Default value is "Large".
    :vartype capacity: str
    :ivar generic_value: Generic URL value.
    :vartype generic_value: str
    :ivar odata_value: URL value.
    :vartype odata_value: str
    """

    _validation = {
        "name": {"required": True},
        "product_id": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "simple_body_product": {"key": "SimpleBodyProduct", "type": "SimpleProduct"},
        "product_id": {"key": "productId", "type": "str"},
        "description": {"key": "description", "type": "str"},
        "max_product_display_name": {"key": "max_product_display_name", "type": "str"},
        "capacity": {"key": "capacity", "type": "str"},
        "generic_value": {"key": "generic_value", "type": "str"},
        "odata_value": {"key": "@odata\\.value", "type": "str"},
    }

    def __init__(
        self,
        *,
        name: str,
        product_id: str,
        simple_body_product: Optional["_models.SimpleProduct"] = None,
        description: Optional[str] = None,
        max_product_display_name: Optional[str] = None,
        capacity: Optional[Literal["Large"]] = None,
        generic_value: Optional[str] = None,
        odata_value: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword name: Product name with value 'groupproduct'. Required.
        :paramtype name: str
        :keyword simple_body_product: Simple body product to put.
        :paramtype simple_body_product: ~modelflattening.models.SimpleProduct
        :keyword product_id: Unique identifier representing a specific product for a given latitude &
         longitude. For example, uberX in San Francisco will have a different product_id than uberX in
         Los Angeles. Required.
        :paramtype product_id: str
        :keyword description: Description of product.
        :paramtype description: str
        :keyword max_product_display_name: Display name of product.
        :paramtype max_product_display_name: str
        :keyword capacity: Capacity of product. For example, 4 people. Default value is "Large".
        :paramtype capacity: str
        :keyword generic_value: Generic URL value.
        :paramtype generic_value: str
        :keyword odata_value: URL value.
        :paramtype odata_value: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.simple_body_product = simple_body_product
        self.product_id = product_id
        self.description = description
        self.max_product_display_name = max_product_display_name
        self.capacity = capacity
        self.generic_value = generic_value
        self.odata_value = odata_value


class GenericUrl(_serialization.Model):
    """The Generic URL.

    :ivar generic_value: Generic URL value.
    :vartype generic_value: str
    """

    _attribute_map = {
        "generic_value": {"key": "generic_value", "type": "str"},
    }

    def __init__(self, *, generic_value: Optional[str] = None, **kwargs):
        """
        :keyword generic_value: Generic URL value.
        :paramtype generic_value: str
        """
        super().__init__(**kwargs)
        self.generic_value = generic_value


class ProductUrl(GenericUrl):
    """The product URL.

    :ivar generic_value: Generic URL value.
    :vartype generic_value: str
    :ivar odata_value: URL value.
    :vartype odata_value: str
    """

    _attribute_map = {
        "generic_value": {"key": "generic_value", "type": "str"},
        "odata_value": {"key": "@odata\\.value", "type": "str"},
    }

    def __init__(self, *, generic_value: Optional[str] = None, odata_value: Optional[str] = None, **kwargs):
        """
        :keyword generic_value: Generic URL value.
        :paramtype generic_value: str
        :keyword odata_value: URL value.
        :paramtype odata_value: str
        """
        super().__init__(generic_value=generic_value, **kwargs)
        self.odata_value = odata_value


class ProductWrapper(_serialization.Model):
    """The wrapped produc.

    :ivar value: the product value.
    :vartype value: str
    """

    _attribute_map = {
        "value": {"key": "property.value", "type": "str"},
    }

    def __init__(self, *, value: Optional[str] = None, **kwargs):
        """
        :keyword value: the product value.
        :paramtype value: str
        """
        super().__init__(**kwargs)
        self.value = value


class ResourceCollection(_serialization.Model):
    """ResourceCollection.

    :ivar productresource: Flattened product.
    :vartype productresource: ~modelflattening.models.FlattenedProduct
    :ivar arrayofresources:
    :vartype arrayofresources: list[~modelflattening.models.FlattenedProduct]
    :ivar dictionaryofresources: Dictionary of :code:`<FlattenedProduct>`.
    :vartype dictionaryofresources: dict[str, ~modelflattening.models.FlattenedProduct]
    """

    _attribute_map = {
        "productresource": {"key": "productresource", "type": "FlattenedProduct"},
        "arrayofresources": {"key": "arrayofresources", "type": "[FlattenedProduct]"},
        "dictionaryofresources": {"key": "dictionaryofresources", "type": "{FlattenedProduct}"},
    }

    def __init__(
        self,
        *,
        productresource: Optional["_models.FlattenedProduct"] = None,
        arrayofresources: Optional[List["_models.FlattenedProduct"]] = None,
        dictionaryofresources: Optional[Dict[str, "_models.FlattenedProduct"]] = None,
        **kwargs
    ):
        """
        :keyword productresource: Flattened product.
        :paramtype productresource: ~modelflattening.models.FlattenedProduct
        :keyword arrayofresources:
        :paramtype arrayofresources: list[~modelflattening.models.FlattenedProduct]
        :keyword dictionaryofresources: Dictionary of :code:`<FlattenedProduct>`.
        :paramtype dictionaryofresources: dict[str, ~modelflattening.models.FlattenedProduct]
        """
        super().__init__(**kwargs)
        self.productresource = productresource
        self.arrayofresources = arrayofresources
        self.dictionaryofresources = dictionaryofresources


class SimpleProduct(BaseProduct):
    """The product documentation.

    All required parameters must be populated in order to send to Azure.

    :ivar product_id: Unique identifier representing a specific product for a given latitude &
     longitude. For example, uberX in San Francisco will have a different product_id than uberX in
     Los Angeles. Required.
    :vartype product_id: str
    :ivar description: Description of product.
    :vartype description: str
    :ivar max_product_display_name: Display name of product.
    :vartype max_product_display_name: str
    :ivar capacity: Capacity of product. For example, 4 people. Default value is "Large".
    :vartype capacity: str
    :ivar generic_value: Generic URL value.
    :vartype generic_value: str
    :ivar odata_value: URL value.
    :vartype odata_value: str
    """

    _validation = {
        "product_id": {"required": True},
    }

    _attribute_map = {
        "product_id": {"key": "base_product_id", "type": "str"},
        "description": {"key": "base_product_description", "type": "str"},
        "max_product_display_name": {"key": "details.max_product_display_name", "type": "str"},
        "capacity": {"key": "details.max_product_capacity", "type": "str"},
        "generic_value": {"key": "details.max_product_image.generic_value", "type": "str"},
        "odata_value": {"key": "details.max_product_image.@odata\\.value", "type": "str"},
    }

    def __init__(
        self,
        *,
        product_id: str,
        description: Optional[str] = None,
        max_product_display_name: Optional[str] = None,
        capacity: Optional[Literal["Large"]] = None,
        generic_value: Optional[str] = None,
        odata_value: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword product_id: Unique identifier representing a specific product for a given latitude &
         longitude. For example, uberX in San Francisco will have a different product_id than uberX in
         Los Angeles. Required.
        :paramtype product_id: str
        :keyword description: Description of product.
        :paramtype description: str
        :keyword max_product_display_name: Display name of product.
        :paramtype max_product_display_name: str
        :keyword capacity: Capacity of product. For example, 4 people. Default value is "Large".
        :paramtype capacity: str
        :keyword generic_value: Generic URL value.
        :paramtype generic_value: str
        :keyword odata_value: URL value.
        :paramtype odata_value: str
        """
        super().__init__(product_id=product_id, description=description, **kwargs)
        self.max_product_display_name = max_product_display_name
        self.capacity = capacity
        self.generic_value = generic_value
        self.odata_value = odata_value


class WrappedProduct(_serialization.Model):
    """The wrapped produc.

    :ivar value: the product value.
    :vartype value: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "str"},
    }

    def __init__(self, *, value: Optional[str] = None, **kwargs):
        """
        :keyword value: the product value.
        :paramtype value: str
        """
        super().__init__(**kwargs)
        self.value = value
