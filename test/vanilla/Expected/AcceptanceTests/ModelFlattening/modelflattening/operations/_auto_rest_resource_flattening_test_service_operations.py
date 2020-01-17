# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Dict, List, Optional
import warnings

from azure.core.exceptions import map_error
from azure.core.tracing.decorator import distributed_trace
from msrest.serialization import Model

from .. import models


class AutoRestResourceFlatteningTestServiceOperationsMixin(object):
    @distributed_trace
    def put_array(self, resource_array=None, cls=None, **kwargs):

        # type: (Optional[List["Resource"]], Optional[Any], **Any) -> None
        """Put External Resource as an Array.

        FIXME: add operation.summary

        :param resource_array: External Resource as an Array to put
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
          return cls(response, None, {})

    put_array.metadata = {'url': '/model-flatten/array'}
    @distributed_trace
    def get_array(self, cls=None, **kwargs):

        # type: (Optional[Any], **Any) -> List["FlattenedProduct"]
        """Get External Resource as an Array.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return:  or the result of cls(response)
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

        deserialized = self._deserialize('[FlattenedProduct]', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_array.metadata = {'url': '/model-flatten/array'}
    @distributed_trace
    def put_wrapped_array(self, resource_array=None, cls=None, **kwargs):

        # type: (Optional[List["WrappedProduct"]], Optional[Any], **Any) -> None
        """No need to have a route in Express server for this operation. Used to verify the type flattened is not removed if it's referenced in an array.

        FIXME: add operation.summary

        :param resource_array: External Resource as an Array to put
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
          return cls(response, None, {})

    put_wrapped_array.metadata = {'url': '/model-flatten/wrappedarray'}
    @distributed_trace
    def get_wrapped_array(self, cls=None, **kwargs):

        # type: (Optional[Any], **Any) -> List["ProductWrapper"]
        """No need to have a route in Express server for this operation. Used to verify the type flattened is not removed if it's referenced in an array.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return:  or the result of cls(response)
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

        deserialized = self._deserialize('[ProductWrapper]', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_wrapped_array.metadata = {'url': '/model-flatten/wrappedarray'}
    @distributed_trace
    def put_dictionary(self, resource_dictionary=None, cls=None, **kwargs):

        # type: (Optional[Dict[str, "FlattenedProduct"]], Optional[Any], **Any) -> None
        """Put External Resource as a Dictionary.

        FIXME: add operation.summary

        :param resource_dictionary: External Resource as a Dictionary to put
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
          return cls(response, None, {})

    put_dictionary.metadata = {'url': '/model-flatten/dictionary'}
    @distributed_trace
    def get_dictionary(self, cls=None, **kwargs):

        # type: (Optional[Any], **Any) -> Dict[str, "FlattenedProduct"]
        """Get External Resource as a Dictionary.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return:  or the result of cls(response)
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

        deserialized = self._deserialize('{FlattenedProduct}', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_dictionary.metadata = {'url': '/model-flatten/dictionary'}
    @distributed_trace
    def put_resource_collection(self, resource_complex_object=None, cls=None, **kwargs):

        # type: (Optional["ResourceCollection"], Optional[Any], **Any) -> None
        """Put External Resource as a ResourceCollection.

        FIXME: add operation.summary

        :param resource_complex_object: External Resource as a ResourceCollection to put
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
          return cls(response, None, {})

    put_resource_collection.metadata = {'url': '/model-flatten/resourcecollection'}
    @distributed_trace
    def get_resource_collection(self, cls=None, **kwargs):

        # type: (Optional[Any], **Any) -> "ResourceCollection"
        """Get External Resource as a ResourceCollection.

        FIXME: add operation.summary

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

        deserialized = self._deserialize('ResourceCollection', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_resource_collection.metadata = {'url': '/model-flatten/resourcecollection'}
    @distributed_trace
    def put_simple_product(self, simple_body_product=None, cls=None, **kwargs):

        # type: (Optional["SimpleProduct"], Optional[Any], **Any) -> "SimpleProduct"
        """Put Simple Product with client flattening true on the model.

        FIXME: add operation.summary

        :param simple_body_product: Simple body product to put
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

        deserialized = self._deserialize('SimpleProduct', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    put_simple_product.metadata = {'url': '/model-flatten/customFlattening'}
    @distributed_trace
    def post_flattened_simple_product(self, simple_body_product=None, cls=None, **kwargs):

        # type: (Optional["SimpleProduct"], Optional[Any], **Any) -> "SimpleProduct"
        """Put Flattened Simple Product with client flattening true on the parameter.

        FIXME: add operation.summary

        :param simple_body_product: Simple body product to post
        :type simple_body_product: ~modelflattening.models.SimpleProduct
        :param callable cls: A custom type or function that will be passed the direct response
        :return: SimpleProduct or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises: ~modelflattening.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

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

        deserialized = self._deserialize('SimpleProduct', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    post_flattened_simple_product.metadata = {'url': '/model-flatten/customFlattening'}
    @distributed_trace
    def put_simple_product_with_grouping(self, name, simple_body_product=None, cls=None, **kwargs):

        # type: (str, Optional["SimpleProduct"], Optional[Any], **Any) -> "SimpleProduct"
        """Put Simple Product with client flattening true on the model.

        FIXME: add operation.summary

        :param name: Product name with value 'groupproduct'
        :type name: str
        :param simple_body_product: Simple body product to put
        :type simple_body_product: ~modelflattening.models.SimpleProduct
        :param callable cls: A custom type or function that will be passed the direct response
        :return: SimpleProduct or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises: ~modelflattening.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

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

        deserialized = self._deserialize('SimpleProduct', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    put_simple_product_with_grouping.metadata = {'url': '/model-flatten/customFlattening/parametergrouping/{name}/'}
