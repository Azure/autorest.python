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

from .base_product import BaseProduct


class SimpleProduct(BaseProduct):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param product_id: Unique identifier representing a specific product for a
     given latitude & longitude. For example, uberX in San Francisco will have
     a different product_id than uberX in Los Angeles.
    :type product_id: str
    :param description: Description of product.
    :type description: str
    :param max_product_display_name: Display name of product.
    :type max_product_display_name: str
    :ivar capacity: Capacity of product. For example, 4 people. Default value:
     "Large" .
    :vartype capacity: str
    :param generic_value: Generic URL value.
    :type generic_value: str
    :param odatavalue: URL value.
    :type odatavalue: str
    """

    _validation = {
        'product_id': {'required': True},
        'max_product_display_name': {'required': True},
        'capacity': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'product_id': {'key': 'base_product_id', 'type': 'str'},
        'description': {'key': 'base_product_description', 'type': 'str'},
        'max_product_display_name': {'key': 'details.max_product_display_name', 'type': 'str'},
        'capacity': {'key': 'details.max_product_capacity', 'type': 'str'},
        'generic_value': {'key': 'details.max_product_image.generic_value', 'type': 'str'},
        'odatavalue': {'key': 'details.max_product_image.@odata\\.value', 'type': 'str'},
    }

    capacity = "Large"

    def __init__(self, **kwargs):
        super(SimpleProduct, self).__init__(**kwargs)
        self.max_product_display_name = kwargs.get('max_product_display_name', None)
        self.generic_value = kwargs.get('generic_value', None)
        self.odatavalue = kwargs.get('odatavalue', None)
