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

from ... import models
import uuid


class AutoRestResourceFlatteningTestServiceOperationsMixin:

    async def put_array(self, resource_array=None, *, cls=None, **operation_config):
        """Put External Resource as an Array.

        :param resource_array: External Resource as an Array to put
        :type resource_array: list[~modelflattening.models.Resource]
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.put_array.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        if resource_array is not None:
            body_content = self._serialize.body(resource_array, '[Resource]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_array.metadata = {'url': '/model-flatten/array'}

    async def get_array(self, *, cls=None, **operation_config):
        """Get External Resource as an Array.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or the result of cls(response)
        :rtype: list[~modelflattening.models.FlattenedProduct]
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.get_array.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('[FlattenedProduct]', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_array.metadata = {'url': '/model-flatten/array'}

    async def put_wrapped_array(self, resource_array=None, *, cls=None, **operation_config):
        """No need to have a route in Express server for this operation. Used to
        verify the type flattened is not removed if it's referenced in an
        array.

        :param resource_array: External Resource as an Array to put
        :type resource_array: list[~modelflattening.models.WrappedProduct]
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.put_wrapped_array.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        if resource_array is not None:
            body_content = self._serialize.body(resource_array, '[WrappedProduct]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_wrapped_array.metadata = {'url': '/model-flatten/wrappedarray'}

    async def get_wrapped_array(self, *, cls=None, **operation_config):
        """No need to have a route in Express server for this operation. Used to
        verify the type flattened is not removed if it's referenced in an
        array.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or the result of cls(response)
        :rtype: list[~modelflattening.models.ProductWrapper]
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.get_wrapped_array.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('[ProductWrapper]', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_wrapped_array.metadata = {'url': '/model-flatten/wrappedarray'}

    async def put_dictionary(self, resource_dictionary=None, *, cls=None, **operation_config):
        """Put External Resource as a Dictionary.

        :param resource_dictionary: External Resource as a Dictionary to put
        :type resource_dictionary: dict[str,
         ~modelflattening.models.FlattenedProduct]
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.put_dictionary.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        if resource_dictionary is not None:
            body_content = self._serialize.body(resource_dictionary, '{FlattenedProduct}')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_dictionary.metadata = {'url': '/model-flatten/dictionary'}

    async def get_dictionary(self, *, cls=None, **operation_config):
        """Get External Resource as a Dictionary.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: dict or the result of cls(response)
        :rtype: dict[str, ~modelflattening.models.FlattenedProduct]
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.get_dictionary.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('{FlattenedProduct}', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_dictionary.metadata = {'url': '/model-flatten/dictionary'}

    async def put_resource_collection(self, resource_complex_object=None, *, cls=None, **operation_config):
        """Put External Resource as a ResourceCollection.

        :param resource_complex_object: External Resource as a
         ResourceCollection to put
        :type resource_complex_object:
         ~modelflattening.models.ResourceCollection
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.put_resource_collection.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        if resource_complex_object is not None:
            body_content = self._serialize.body(resource_complex_object, 'ResourceCollection')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_resource_collection.metadata = {'url': '/model-flatten/resourcecollection'}

    async def get_resource_collection(self, *, cls=None, **operation_config):
        """Get External Resource as a ResourceCollection.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceCollection or the result of cls(response)
        :rtype: ~modelflattening.models.ResourceCollection
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.get_resource_collection.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ResourceCollection', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_resource_collection.metadata = {'url': '/model-flatten/resourcecollection'}

    async def put_simple_product(self, simple_body_product=None, *, cls=None, **operation_config):
        """Put Simple Product with client flattening true on the model.

        :param simple_body_product: Simple body product to put
        :type simple_body_product: ~modelflattening.models.SimpleProduct
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SimpleProduct or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.put_simple_product.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        if simple_body_product is not None:
            body_content = self._serialize.body(simple_body_product, 'SimpleProduct')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SimpleProduct', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    put_simple_product.metadata = {'url': '/model-flatten/customFlattening'}

    async def post_flattened_simple_product(self, product_id, max_product_display_name, description=None, generic_value=None, odatavalue=None, *, cls=None, **operation_config):
        """Put Flattened Simple Product with client flattening true on the
        parameter.

        :param product_id: Unique identifier representing a specific product
         for a given latitude & longitude. For example, uberX in San Francisco
         will have a different product_id than uberX in Los Angeles.
        :type product_id: str
        :param max_product_display_name: Display name of product.
        :type max_product_display_name: str
        :param description: Description of product.
        :type description: str
        :param generic_value: Generic URL value.
        :type generic_value: str
        :param odatavalue: URL value.
        :type odatavalue: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SimpleProduct or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        simple_body_product = None
        if product_id is not None or description is not None or max_product_display_name is not None or generic_value is not None or odatavalue is not None:
            simple_body_product = models.SimpleProduct(product_id=product_id, description=description, max_product_display_name=max_product_display_name, generic_value=generic_value, odatavalue=odatavalue)

        # Construct URL
        url = self.post_flattened_simple_product.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        if simple_body_product is not None:
            body_content = self._serialize.body(simple_body_product, 'SimpleProduct')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SimpleProduct', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    post_flattened_simple_product.metadata = {'url': '/model-flatten/customFlattening'}

    async def put_simple_product_with_grouping(self, flatten_parameter_group, *, cls=None, **operation_config):
        """Put Simple Product with client flattening true on the model.

        :param flatten_parameter_group: Additional parameters for the
         operation
        :type flatten_parameter_group:
         ~modelflattening.models.FlattenParameterGroup
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SimpleProduct or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        name = None
        if flatten_parameter_group is not None:
            name = flatten_parameter_group.name
        product_id = None
        if flatten_parameter_group is not None:
            product_id = flatten_parameter_group.product_id
        description = None
        if flatten_parameter_group is not None:
            description = flatten_parameter_group.description
        max_product_display_name = None
        if flatten_parameter_group is not None:
            max_product_display_name = flatten_parameter_group.max_product_display_name
        generic_value = None
        if flatten_parameter_group is not None:
            generic_value = flatten_parameter_group.generic_value
        odatavalue = None
        if flatten_parameter_group is not None:
            odatavalue = flatten_parameter_group.odatavalue
        simple_body_product = None
        if product_id is not None or description is not None or max_product_display_name is not None or generic_value is not None or odatavalue is not None:
            simple_body_product = models.SimpleProduct(product_id=product_id, description=description, max_product_display_name=max_product_display_name, generic_value=generic_value, odatavalue=odatavalue)

        # Construct URL
        url = self.put_simple_product_with_grouping.metadata['url']
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        if simple_body_product is not None:
            body_content = self._serialize.body(simple_body_product, 'SimpleProduct')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SimpleProduct', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    put_simple_product_with_grouping.metadata = {'url': '/model-flatten/customFlattening/parametergrouping/{name}/'}
