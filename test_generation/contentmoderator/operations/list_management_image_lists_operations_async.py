# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models
from .list_management_image_lists_operations import ListManagementImageListsOperations as _ListManagementImageListsOperations


class ListManagementImageListsOperations(_ListManagementImageListsOperations):
    """ListManagementImageListsOperations operations."""

    async def get_details_async(
            self, list_id, *, custom_headers=None, raw=False, **operation_config):
        """Returns the details of the image list with list Id equal to list Id
        passed.

        :param list_id: List Id of the image list.
        :type list_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ImageList or ClientRawResponse if raw=true
        :rtype: ~contentmoderator.models.ImageList or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.get_details_async.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'listId': self._serialize.url("list_id", list_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ImageList', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_details_async.metadata = {'url': '/contentmoderator/lists/v1.0/imagelists/{listId}'}

    async def delete_async(
            self, list_id, *, custom_headers=None, raw=False, **operation_config):
        """Deletes image list with the list Id equal to list Id passed.

        :param list_id: List Id of the image list.
        :type list_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: str or ClientRawResponse if raw=true
        :rtype: str or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.delete_async.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'listId': self._serialize.url("list_id", list_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('str', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_async.metadata = {'url': '/contentmoderator/lists/v1.0/imagelists/{listId}'}

    async def update_async(
            self, list_id, content_type, body, *, custom_headers=None, raw=False, **operation_config):
        """Updates an image list with list Id equal to list Id passed.

        :param list_id: List Id of the image list.
        :type list_id: str
        :param content_type: The content type.
        :type content_type: str
        :param body: Schema of the body.
        :type body: ~contentmoderator.models.Body
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ImageList or ClientRawResponse if raw=true
        :rtype: ~contentmoderator.models.ImageList or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.update_async.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'listId': self._serialize.url("list_id", list_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        # Construct body
        body_content = self._serialize.body(body, 'Body')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ImageList', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_async.metadata = {'url': '/contentmoderator/lists/v1.0/imagelists/{listId}'}

    async def create_async(
            self, content_type, body, *, custom_headers=None, raw=False, **operation_config):
        """Creates an image list.

        :param content_type: The content type.
        :type content_type: str
        :param body: Schema of the body.
        :type body: ~contentmoderator.models.Body
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ImageList or ClientRawResponse if raw=true
        :rtype: ~contentmoderator.models.ImageList or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.create_async.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        # Construct body
        body_content = self._serialize.body(body, 'Body')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ImageList', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_async.metadata = {'url': '/contentmoderator/lists/v1.0/imagelists'}

    async def get_all_image_lists_async(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Gets all the Image Lists.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~contentmoderator.models.ImageList] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.get_all_image_lists_async.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('[ImageList]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_all_image_lists_async.metadata = {'url': '/contentmoderator/lists/v1.0/imagelists'}

    async def refresh_index_method_async(
            self, list_id, *, custom_headers=None, raw=False, **operation_config):
        """Refreshes the index of the list with list Id equal to list Id passed.

        :param list_id: List Id of the image list.
        :type list_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: RefreshIndex or ClientRawResponse if raw=true
        :rtype: ~contentmoderator.models.RefreshIndex or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.refresh_index_method_async.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'listId': self._serialize.url("list_id", list_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('RefreshIndex', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    refresh_index_method_async.metadata = {'url': '/contentmoderator/lists/v1.0/imagelists/{listId}/RefreshIndex'}
