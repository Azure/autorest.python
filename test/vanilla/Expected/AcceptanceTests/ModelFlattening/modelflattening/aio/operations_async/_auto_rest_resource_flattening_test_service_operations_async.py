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
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class AutoRestResourceFlatteningTestServiceOperationsMixin:

    @distributed_trace_async
    async def put_array(
        self,
        resource_array: Optional[List["Resource"]] = None,
        *,
        content_type: Optional[str] = None,
        **kwargs
    ) -> None:
        """Put External Resource as an Array.

        :param resource_array: External Resource as an Array to put.
        :type resource_array: list[~modelflattening.models.Resource]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_array.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = content_type or 'application/json'

        # Construct and send request
        __body_content_kwargs = {}
        if header_parameters['Content-Type'] in ['application/json']:
            if resource_array is not None:
                body_content = self._serialize.body(resource_array, '[Resource]')
            else:
                body_content = None
            __body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **__body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_array.metadata = {'url': '/model-flatten/array'}

    @distributed_trace_async
    async def get_array(
        self,
        **kwargs
    ) -> List["FlattenedProduct"]:
        """Get External Resource as an Array.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list or the result of cls(response)
        :rtype: list[~modelflattening.models.FlattenedProduct]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[List["FlattenedProduct"]] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_array.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('[FlattenedProduct]', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_array.metadata = {'url': '/model-flatten/array'}

    @distributed_trace_async
    async def put_wrapped_array(
        self,
        resource_array: Optional[List["WrappedProduct"]] = None,
        *,
        content_type: Optional[str] = None,
        **kwargs
    ) -> None:
        """No need to have a route in Express server for this operation. Used to verify the type flattened is not removed if it's referenced in an array.

        :param resource_array: External Resource as an Array to put.
        :type resource_array: list[~modelflattening.models.WrappedProduct]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_wrapped_array.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = content_type or 'application/json'

        # Construct and send request
        __body_content_kwargs = {}
        if header_parameters['Content-Type'] in ['application/json']:
            if resource_array is not None:
                body_content = self._serialize.body(resource_array, '[WrappedProduct]')
            else:
                body_content = None
            __body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **__body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_wrapped_array.metadata = {'url': '/model-flatten/wrappedarray'}

    @distributed_trace_async
    async def get_wrapped_array(
        self,
        **kwargs
    ) -> List["ProductWrapper"]:
        """No need to have a route in Express server for this operation. Used to verify the type flattened is not removed if it's referenced in an array.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list or the result of cls(response)
        :rtype: list[~modelflattening.models.ProductWrapper]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[List["ProductWrapper"]] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_wrapped_array.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('[ProductWrapper]', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_wrapped_array.metadata = {'url': '/model-flatten/wrappedarray'}

    @distributed_trace_async
    async def put_dictionary(
        self,
        resource_dictionary: Optional[Dict[str, "FlattenedProduct"]] = None,
        *,
        content_type: Optional[str] = None,
        **kwargs
    ) -> None:
        """Put External Resource as a Dictionary.

        :param resource_dictionary: External Resource as a Dictionary to put.
        :type resource_dictionary: dict[str, ~modelflattening.models.FlattenedProduct]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_dictionary.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = content_type or 'application/json'

        # Construct and send request
        __body_content_kwargs = {}
        if header_parameters['Content-Type'] in ['application/json']:
            if resource_dictionary is not None:
                body_content = self._serialize.body(resource_dictionary, '{FlattenedProduct}')
            else:
                body_content = None
            __body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **__body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_dictionary.metadata = {'url': '/model-flatten/dictionary'}

    @distributed_trace_async
    async def get_dictionary(
        self,
        **kwargs
    ) -> Dict[str, "FlattenedProduct"]:
        """Get External Resource as a Dictionary.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: dict or the result of cls(response)
        :rtype: dict[str, ~modelflattening.models.FlattenedProduct]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[Dict[str, "FlattenedProduct"]] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_dictionary.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('{FlattenedProduct}', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_dictionary.metadata = {'url': '/model-flatten/dictionary'}

    @distributed_trace_async
    async def put_resource_collection(
        self,
        resource_complex_object: Optional["models.ResourceCollection"] = None,
        *,
        content_type: Optional[str] = None,
        **kwargs
    ) -> None:
        """Put External Resource as a ResourceCollection.

        :param resource_complex_object: External Resource as a ResourceCollection to put.
        :type resource_complex_object: ~modelflattening.models.ResourceCollection
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[None] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_resource_collection.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = content_type or 'application/json'

        # Construct and send request
        __body_content_kwargs = {}
        if header_parameters['Content-Type'] in ['application/json']:
            if resource_complex_object is not None:
                body_content = self._serialize.body(resource_complex_object, 'ResourceCollection')
            else:
                body_content = None
            __body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **__body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_resource_collection.metadata = {'url': '/model-flatten/resourcecollection'}

    @distributed_trace_async
    async def get_resource_collection(
        self,
        **kwargs
    ) -> "models.ResourceCollection":
        """Get External Resource as a ResourceCollection.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ResourceCollection or the result of cls(response)
        :rtype: ~modelflattening.models.ResourceCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType["models.ResourceCollection"] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_resource_collection.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('ResourceCollection', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_resource_collection.metadata = {'url': '/model-flatten/resourcecollection'}

    @distributed_trace_async
    async def put_simple_product(
        self,
        simple_body_product: Optional["models.SimpleProduct"] = None,
        *,
        content_type: Optional[str] = None,
        **kwargs
    ) -> "models.SimpleProduct":
        """Put Simple Product with client flattening true on the model.

        :param simple_body_product: Simple body product to put.
        :type simple_body_product: ~modelflattening.models.SimpleProduct
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SimpleProduct or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType["models.SimpleProduct"] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_simple_product.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = content_type or 'application/json'

        # Construct and send request
        __body_content_kwargs = {}
        if header_parameters['Content-Type'] in ['application/json']:
            if simple_body_product is not None:
                body_content = self._serialize.body(simple_body_product, 'SimpleProduct')
            else:
                body_content = None
            __body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **__body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('SimpleProduct', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    put_simple_product.metadata = {'url': '/model-flatten/customFlattening'}

    @distributed_trace_async
    async def post_flattened_simple_product(
        self,
        product_id: str,
        description: Optional[str] = None,
        max_product_display_name: Optional[str] = None,
        generic_value: Optional[str] = None,
        odata_value: Optional[str] = None,
        *,
        content_type: Optional[str] = None,
        **kwargs
    ) -> "models.SimpleProduct":
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
        :param odata_value: URL value.
        :type odata_value: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SimpleProduct or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType["models.SimpleProduct"] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})

        _simple_body_product = models.SimpleProduct(product_id=product_id, description=description, max_product_display_name=max_product_display_name, generic_value=generic_value, odata_value=odata_value)

        # Construct URL
        url = self.post_flattened_simple_product.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = content_type or 'application/json'

        # Construct and send request
        __body_content_kwargs = {}
        if header_parameters['Content-Type'] in ['application/json']:
            if _simple_body_product is not None:
                body_content = self._serialize.body(_simple_body_product, 'SimpleProduct')
            else:
                body_content = None
            __body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **__body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('SimpleProduct', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    post_flattened_simple_product.metadata = {'url': '/model-flatten/customFlattening'}

    @distributed_trace_async
    async def put_simple_product_with_grouping(
        self,
        flatten_parameter_group: "models.FlattenParameterGroup",
        *,
        content_type: Optional[str] = None,
        **kwargs
    ) -> "models.SimpleProduct":
        """Put Simple Product with client flattening true on the model.

        :param flatten_parameter_group: Parameter group.
        :type flatten_parameter_group: ~modelflattening.models.FlattenParameterGroup
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SimpleProduct or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType["models.SimpleProduct"] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})
        
        _name = None
        _simple_body_product = None
        _product_id = None
        _description = None
        _max_product_display_name = None
        _generic_value = None
        _odata_value = None
        if flatten_parameter_group is not None:
            _name = flatten_parameter_group.name
            _simple_body_product = flatten_parameter_group.simple_body_product
            _product_id = flatten_parameter_group.product_id
            _description = flatten_parameter_group.description
            _max_product_display_name = flatten_parameter_group.max_product_display_name
            _generic_value = flatten_parameter_group.generic_value
            _odata_value = flatten_parameter_group.odata_value

        _simple_body_product = models.SimpleProduct(product_id=_product_id, description=_description, max_product_display_name=_max_product_display_name, generic_value=_generic_value, odata_value=_odata_value)

        # Construct URL
        url = self.put_simple_product_with_grouping.metadata['url']
        path_format_arguments = {
            'name': self._serialize.url("name", _name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = content_type or 'application/json'

        # Construct and send request
        __body_content_kwargs = {}
        if header_parameters['Content-Type'] in ['application/json']:
            if _simple_body_product is not None:
                body_content = self._serialize.body(_simple_body_product, 'SimpleProduct')
            else:
                body_content = None
            __body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **__body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('SimpleProduct', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    put_simple_product_with_grouping.metadata = {'url': '/model-flatten/customFlattening/parametergrouping/{name}/'}
