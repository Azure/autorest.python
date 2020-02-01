# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from msrest.serialization import Model

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class AutoRestResourceFlatteningTestServiceOperationsMixin(object):

    @distributed_trace
    def put_array(
        self,
        resource_array=None,  # type: Optional[List["Resource"]]
        cls=None,  # type: ClsType[None]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put External Resource as an Array.

        :param resource_array: External Resource as an Array to put.
        :type resource_array: list[~modelflattening.models.Resource]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~modelflattening.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_array.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if resource_array is not None:
            body_content = self._serialize.body(resource_array, '[Resource]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_array.metadata = {'url': '/model-flatten/array'}

    @distributed_trace
    def get_array(
        self,
        cls=None,  # type: ClsType[List["FlattenedProduct"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> List["FlattenedProduct"]
        """Get External Resource as an Array.

        :param callable cls: A custom type or function that will be passed the direct response
        :return: list or the result of cls(response)
        :rtype: list[~modelflattening.models.FlattenedProduct]
        :raises: ~modelflattening.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_array.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('[FlattenedProduct]', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_array.metadata = {'url': '/model-flatten/array'}

    @distributed_trace
    def put_wrapped_array(
        self,
        resource_array=None,  # type: Optional[List["WrappedProduct"]]
        cls=None,  # type: ClsType[None]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """No need to have a route in Express server for this operation. Used to verify the type flattened is not removed if it's referenced in an array.

        :param resource_array: External Resource as an Array to put.
        :type resource_array: list[~modelflattening.models.WrappedProduct]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~modelflattening.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_wrapped_array.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if resource_array is not None:
            body_content = self._serialize.body(resource_array, '[WrappedProduct]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_wrapped_array.metadata = {'url': '/model-flatten/wrappedarray'}

    @distributed_trace
    def get_wrapped_array(
        self,
        cls=None,  # type: ClsType[List["ProductWrapper"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> List["ProductWrapper"]
        """No need to have a route in Express server for this operation. Used to verify the type flattened is not removed if it's referenced in an array.

        :param callable cls: A custom type or function that will be passed the direct response
        :return: list or the result of cls(response)
        :rtype: list[~modelflattening.models.ProductWrapper]
        :raises: ~modelflattening.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_wrapped_array.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('[ProductWrapper]', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_wrapped_array.metadata = {'url': '/model-flatten/wrappedarray'}

    @distributed_trace
    def put_dictionary(
        self,
        resource_dictionary=None,  # type: Optional[Dict[str, "FlattenedProduct"]]
        cls=None,  # type: ClsType[None]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put External Resource as a Dictionary.

        :param resource_dictionary: External Resource as a Dictionary to put.
        :type resource_dictionary: dict[str, ~modelflattening.models.FlattenedProduct]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~modelflattening.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_dictionary.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if resource_dictionary is not None:
            body_content = self._serialize.body(resource_dictionary, '{FlattenedProduct}')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_dictionary.metadata = {'url': '/model-flatten/dictionary'}

    @distributed_trace
    def get_dictionary(
        self,
        cls=None,  # type: ClsType[Dict[str, "FlattenedProduct"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Dict[str, "FlattenedProduct"]
        """Get External Resource as a Dictionary.

        :param callable cls: A custom type or function that will be passed the direct response
        :return: dict or the result of cls(response)
        :rtype: dict[str, ~modelflattening.models.FlattenedProduct]
        :raises: ~modelflattening.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_dictionary.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('{FlattenedProduct}', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_dictionary.metadata = {'url': '/model-flatten/dictionary'}

    @distributed_trace
    def put_resource_collection(
        self,
        resource_complex_object=None,  # type: Optional["models.ResourceCollection"]
        cls=None,  # type: ClsType[None]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put External Resource as a ResourceCollection.

        :param resource_complex_object: External Resource as a ResourceCollection to put.
        :type resource_complex_object: ~modelflattening.models.ResourceCollection
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~modelflattening.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_resource_collection.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if resource_complex_object is not None:
            body_content = self._serialize.body(resource_complex_object, 'ResourceCollection')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_resource_collection.metadata = {'url': '/model-flatten/resourcecollection'}

    @distributed_trace
    def get_resource_collection(
        self,
        cls=None,  # type: ClsType["models.ResourceCollection"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ResourceCollection"
        """Get External Resource as a ResourceCollection.

        :param callable cls: A custom type or function that will be passed the direct response
        :return: ResourceCollection or the result of cls(response)
        :rtype: ~modelflattening.models.ResourceCollection
        :raises: ~modelflattening.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_resource_collection.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('ResourceCollection', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_resource_collection.metadata = {'url': '/model-flatten/resourcecollection'}

    @distributed_trace
    def put_simple_product(
        self,
        simple_body_product=None,  # type: Optional["models.SimpleProduct"]
        cls=None,  # type: ClsType["models.SimpleProduct"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SimpleProduct"
        """Put Simple Product with client flattening true on the model.

        :param simple_body_product: Simple body product to put.
        :type simple_body_product: ~modelflattening.models.SimpleProduct
        :param callable cls: A custom type or function that will be passed the direct response
        :return: SimpleProduct or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises: ~modelflattening.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_simple_product.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if simple_body_product is not None:
            body_content = self._serialize.body(simple_body_product, 'SimpleProduct')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('SimpleProduct', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    put_simple_product.metadata = {'url': '/model-flatten/customFlattening'}

    @distributed_trace
    def post_flattened_simple_product(
        self,
        product_id,  # type: str
        description=None,  # type: Optional[str]
        max_product_display_name=None,  # type: Optional[str]
        generic_value=None,  # type: Optional[str]
        odatavalue=None,  # type: Optional[str]
        cls=None,  # type: ClsType["models.SimpleProduct"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SimpleProduct"
        """Put Flattened Simple Product with client flattening true on the parameter.

        :param product_id: Unique identifier representing a specific product for a given latitude &
         longitude. For example, uberX in San Francisco will have a different product_id than uberX in
         Los Angeles.
        :type product_id: str
        :param description: Description of product.
        :type description: str
        :param max_product_display_name: Display name of product.
        :type max_product_display_name: str
        :param generic_value: Generic URL value.
        :type generic_value: str
        :param odatavalue: URL value.
        :type odatavalue: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: SimpleProduct or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises: ~modelflattening.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        simple_body_product = models.SimpleProduct(product_id=product_id, description=description, max_product_display_name=max_product_display_name, generic_value=generic_value, odatavalue=odatavalue)

        # Construct URL
        url = self.post_flattened_simple_product.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if simple_body_product is not None:
            body_content = self._serialize.body(simple_body_product, 'SimpleProduct')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('SimpleProduct', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    post_flattened_simple_product.metadata = {'url': '/model-flatten/customFlattening'}

    @distributed_trace
    def put_simple_product_with_grouping(
        self,
        flatten_parameter_group,  # type: "models.FlattenParameterGroup"
        cls=None,  # type: ClsType["models.SimpleProduct"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SimpleProduct"
        """Put Simple Product with client flattening true on the model.

        :param flatten_parameter_group: Parameter group.
        :type flatten_parameter_group: ~modelflattening.models.FlattenParameterGroup
        :param callable cls: A custom type or function that will be passed the direct response
        :return: SimpleProduct or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises: ~modelflattening.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        
        name = None
        simple_body_product = None
        product_id = None
        description = None
        max_product_display_name = None
        capacity = None
        generic_value = None
        odatavalue = None
        if flatten_parameter_group is not None:
            name = flatten_parameter_group.name
            simple_body_product = flatten_parameter_group.simple_body_product
            product_id = flatten_parameter_group.product_id
            description = flatten_parameter_group.description
            max_product_display_name = flatten_parameter_group.max_product_display_name
            capacity = flatten_parameter_group.capacity
            generic_value = flatten_parameter_group.generic_value
            odatavalue = flatten_parameter_group.odatavalue

        simple_body_product = models.SimpleProduct(product_id=product_id, description=description, max_product_display_name=max_product_display_name, generic_value=generic_value, odatavalue=odatavalue, flatten_parameter_group=flatten_parameter_group)

        # Construct URL
        url = self.put_simple_product_with_grouping.metadata['url']
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if simple_body_product is not None:
            body_content = self._serialize.body(simple_body_product, 'SimpleProduct')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('SimpleProduct', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    put_simple_product_with_grouping.metadata = {'url': '/model-flatten/customFlattening/parametergrouping/{name}/'}
