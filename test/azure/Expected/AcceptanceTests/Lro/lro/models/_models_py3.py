# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, Union

from msrest.serialization import Model


class OperationResult(Model):
    """OperationResult.

    :param status: The status of the request. Possible values include: 'Succeeded',
	 'Failed', 'canceled', 'Accepted', 'Creating', 'Created', 'Updating', 'Updated',
	 'Deleting', 'Deleted', 'OK'.
    :type status: str or ~lro.models.OperationResultStatus
    :param error:
    :type error: ~lro.models.OperationResultError
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'error': {'key': 'error', 'type': 'OperationResultError'},
    }

    def __init__(self, *, status: Union[str, "OperationResultStatus"]=None, error: "OperationResultError"=None, **kwargs) -> None:
        super(OperationResult, self).__init__(**kwargs)
        self.status = status
        self.error = error


class OperationResultError(Model):
    """OperationResultError.

    :param code: The error code for an operation failure.
    :type code: int
    :param message: The detailed arror message.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code: int=None, message: str=None, **kwargs) -> None:
        super(OperationResultError, self).__init__(**kwargs)
        self.code = code
        self.message = message


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


class Product(Resource):
    """Product.

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
    :type properties: ~lro.models.ProductProperties
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
        'properties': {'key': 'properties', 'type': 'ProductProperties'},
    }

    def __init__(self, *, tags: Dict[str, str]=None, location: str=None, properties: "ProductProperties"=None, **kwargs) -> None:
        super(Product, self).__init__(tags=tags, location=location, **kwargs)
        self.properties = properties


class ProductProperties(Model):
    """ProductProperties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param provisioning_state:
    :type provisioning_state: str
    :ivar provisioning_state_values:  Possible values include: 'Succeeded',
	 'Failed', 'canceled', 'Accepted', 'Creating', 'Created', 'Updating', 'Updated',
	 'Deleting', 'Deleted', 'OK'.
    :vartype provisioning_state_values: str or
	 ~lro.models.ProductPropertiesProvisioningStateValues
    """

    _validation = {
        'provisioning_state_values': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'provisioning_state_values': {'key': 'provisioningStateValues', 'type': 'str'},
    }

    def __init__(self, *, provisioning_state: str=None, **kwargs) -> None:
        super(ProductProperties, self).__init__(**kwargs)
        self.provisioning_state = provisioning_state
        self.provisioning_state_values = None


class Sku(Model):
    """Sku.

    :param name:
    :type name: str
    :param id:
    :type id: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, id: str=None, **kwargs) -> None:
        super(Sku, self).__init__(**kwargs)
        self.name = name
        self.id = id


class SubResource(Model):
    """SubResource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Sub Resource Id.
    :vartype id: str
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(SubResource, self).__init__(**kwargs)
        self.id = None


class SubProduct(SubResource):
    """SubProduct.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Sub Resource Id.
    :vartype id: str
    :param properties:
    :type properties: ~lro.models.SubProductProperties
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'SubProductProperties'},
    }

    def __init__(self, *, properties: "SubProductProperties"=None, **kwargs) -> None:
        super(SubProduct, self).__init__(**kwargs)
        self.properties = properties


class SubProductProperties(Model):
    """SubProductProperties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param provisioning_state:
    :type provisioning_state: str
    :ivar provisioning_state_values:  Possible values include: 'Succeeded',
	 'Failed', 'canceled', 'Accepted', 'Creating', 'Created', 'Updating', 'Updated',
	 'Deleting', 'Deleted', 'OK'.
    :vartype provisioning_state_values: str or
	 ~lro.models.SubProductPropertiesProvisioningStateValues
    """

    _validation = {
        'provisioning_state_values': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'provisioning_state_values': {'key': 'provisioningStateValues', 'type': 'str'},
    }

    def __init__(self, *, provisioning_state: str=None, **kwargs) -> None:
        super(SubProductProperties, self).__init__(**kwargs)
        self.provisioning_state = provisioning_state
        self.provisioning_state_values = None
