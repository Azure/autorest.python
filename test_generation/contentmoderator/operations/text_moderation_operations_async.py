# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models
from .text_moderation_operations import TextModerationOperations as _TextModerationOperations


class TextModerationOperations(_TextModerationOperations):
    """TextModerationOperations operations."""

    async def screen_text_async(
            self, text_content_type, text_content, language=None, autocorrect=False, pii=False, list_id=None, classify=False, *, custom_headers=None, raw=False, callback=None, **operation_config):
        """Detect profanity and match against custom and shared blacklists.

        Detects profanity in more than 100 languages and match against custom
        and shared blacklists.

        :param text_content_type: The content type. Possible values include:
         'text/plain', 'text/html', 'text/xml', 'text/markdown'
        :type text_content_type: str
        :param text_content: Content to screen.
        :type text_content: Generator
        :param language: Language of the text.
        :type language: str
        :param autocorrect: Autocorrect text.
        :type autocorrect: bool
        :param pii: Detect personal identifiable information.
        :type pii: bool
        :param list_id: The list Id.
        :type list_id: str
        :param classify: Classify input.
        :type classify: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Screen or ClientRawResponse if raw=true
        :rtype: ~contentmoderator.models.Screen or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.screen_text_async.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if language is not None:
            query_parameters['language'] = self._serialize.query("language", language, 'str')
        if autocorrect is not None:
            query_parameters['autocorrect'] = self._serialize.query("autocorrect", autocorrect, 'bool')
        if pii is not None:
            query_parameters['PII'] = self._serialize.query("pii", pii, 'bool')
        if list_id is not None:
            query_parameters['listId'] = self._serialize.query("list_id", list_id, 'str')
        if classify is not None:
            query_parameters['classify'] = self._serialize.query("classify", classify, 'bool')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'text/plain'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Content-Type'] = self._serialize.header("text_content_type", text_content_type, 'str')

        # Construct body
        body_content = self._client.stream_upload(text_content, callback)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Screen', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    screen_text_async.metadata = {'url': '/contentmoderator/moderate/v1.0/ProcessText/Screen/'}

    async def detect_language_async(
            self, text_content_type, text_content, *, custom_headers=None, raw=False, callback=None, **operation_config):
        """This operation will detect the language of given input content. Returns
        the <a href="http://www-01.sil.org/iso639-3/codes.asp">ISO 639-3
        code</a> for the predominant language comprising the submitted text.
        Over 110 languages supported.

        :param text_content_type: The content type. Possible values include:
         'text/plain', 'text/html', 'text/xml', 'text/markdown'
        :type text_content_type: str
        :param text_content: Content to screen.
        :type text_content: Generator
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DetectedLanguage or ClientRawResponse if raw=true
        :rtype: ~contentmoderator.models.DetectedLanguage or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = self.detect_language_async.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'text/plain'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Content-Type'] = self._serialize.header("text_content_type", text_content_type, 'str')

        # Construct body
        body_content = self._client.stream_upload(text_content, callback)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DetectedLanguage', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    detect_language_async.metadata = {'url': '/contentmoderator/moderate/v1.0/ProcessText/DetectLanguage'}
