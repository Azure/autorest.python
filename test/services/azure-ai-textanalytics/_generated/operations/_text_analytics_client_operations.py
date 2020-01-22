# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import warnings

from azure.core.exceptions import map_error

from .. import models


class TextAnalyticsClientOperationsMixin(object):
    
    def detect_language(self, show_stats=None, documents=None, cls=None, **kwargs):
        """Scores close to 1 indicate 100% certainty that the identified language is true. A total of 120 languages are supported..

        FIXME: add operation.summary

        :param show_stats: (optional) if set to true, response will contain input and document level statistics.
        :type show_stats: bool
        :param documents: MISSING·SCHEMA-DESCRIPTION-ARRAYSCHEMA
        :type documents: list[~azure.ai.textanalytics.models.LanguageInput]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: LanguageBatchResult or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.models.LanguageBatchResult
        :raises: ~azure.ai.textanalytics.models.ErrorResponseException:
        """
        error_map = kwargs.pop('error_map', {})
        language_batch_input = models.LanguageBatchInput(documents=documents)

        # Construct URL
        url = self.detect_language.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if show_stats is not None:
            query_parameters['showStats'] = self._serialize.query("show_stats", show_stats, 'bool')


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if language_batch_input is not None:
            body_content = self._serialize.body(language_batch_input, 'LanguageBatchInput')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        deserialized = self._deserialize('LanguageBatchResult', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    detect_language.metadata = {'url': '/languages'}
    
    def entities(self, show_stats=None, documents=None, cls=None, **kwargs):
        """To get even more information on each recognized entity we recommend using the Bing Entity Search API by querying for the recognized entities names. See the :code:`<a href="https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/text-analytics-supported-languages">Supported languages in Text Analytics API</a>` for the list of enabled languages..

        FIXME: add operation.summary

        :param show_stats: (optional) if set to true, response will contain input and document level statistics.
        :type show_stats: bool
        :param documents: MISSING·SCHEMA-DESCRIPTION-ARRAYSCHEMA
        :type documents: list[~azure.ai.textanalytics.models.MultiLanguageInput]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: EntitiesBatchResult or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.models.EntitiesBatchResult
        :raises: ~azure.ai.textanalytics.models.ErrorResponseException:
        """
        error_map = kwargs.pop('error_map', {})
        multi_language_batch_input = models.MultiLanguageBatchInput(documents=documents)

        # Construct URL
        url = self.entities.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if show_stats is not None:
            query_parameters['showStats'] = self._serialize.query("show_stats", show_stats, 'bool')


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if multi_language_batch_input is not None:
            body_content = self._serialize.body(multi_language_batch_input, 'MultiLanguageBatchInput')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        deserialized = self._deserialize('EntitiesBatchResult', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    entities.metadata = {'url': '/entities'}
    
    def key_phrases(self, show_stats=None, documents=None, cls=None, **kwargs):
        """See the :code:`<a href="https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview#supported-languages">Text Analytics Documentation</a>` for details about the languages that are supported by key phrase extraction..

        FIXME: add operation.summary

        :param show_stats: (optional) if set to true, response will contain input and document level statistics.
        :type show_stats: bool
        :param documents: MISSING·SCHEMA-DESCRIPTION-ARRAYSCHEMA
        :type documents: list[~azure.ai.textanalytics.models.MultiLanguageInput]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: KeyPhraseBatchResult or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.models.KeyPhraseBatchResult
        :raises: ~azure.ai.textanalytics.models.ErrorResponseException:
        """
        error_map = kwargs.pop('error_map', {})
        multi_language_batch_input = models.MultiLanguageBatchInput(documents=documents)

        # Construct URL
        url = self.key_phrases.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if show_stats is not None:
            query_parameters['showStats'] = self._serialize.query("show_stats", show_stats, 'bool')


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if multi_language_batch_input is not None:
            body_content = self._serialize.body(multi_language_batch_input, 'MultiLanguageBatchInput')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        deserialized = self._deserialize('KeyPhraseBatchResult', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    key_phrases.metadata = {'url': '/keyPhrases'}
    
    def sentiment(self, show_stats=None, documents=None, cls=None, **kwargs):
        """Scores close to 1 indicate positive sentiment, while scores close to 0 indicate negative sentiment. A score of 0.5 indicates the lack of sentiment (e.g. a factoid statement). See the :code:`<a href="https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview#supported-languages">Text Analytics Documentation</a>` for details about the languages that are supported by sentiment analysis..

        FIXME: add operation.summary

        :param show_stats: (optional) if set to true, response will contain input and document level statistics.
        :type show_stats: bool
        :param documents: MISSING·SCHEMA-DESCRIPTION-ARRAYSCHEMA
        :type documents: list[~azure.ai.textanalytics.models.MultiLanguageInput]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: SentimentBatchResult or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.models.SentimentBatchResult
        :raises: ~azure.ai.textanalytics.models.ErrorResponseException:
        """
        error_map = kwargs.pop('error_map', {})
        multi_language_batch_input = models.MultiLanguageBatchInput(documents=documents)

        # Construct URL
        url = self.sentiment.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if show_stats is not None:
            query_parameters['showStats'] = self._serialize.query("show_stats", show_stats, 'bool')


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if multi_language_batch_input is not None:
            body_content = self._serialize.body(multi_language_batch_input, 'MultiLanguageBatchInput')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        deserialized = self._deserialize('SentimentBatchResult', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    sentiment.metadata = {'url': '/sentiment'}
