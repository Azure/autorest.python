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

from azure.core import PipelineClient
from msrest import Serializer, Deserializer

from ._configuration import AzureBlobStorageConfiguration
from .operations import ServiceOperations
from .operations import ContainerOperations
from .operations import BlobOperations
from .operations import PageBlobOperations
from .operations import AppendBlobOperations
from .operations import BlockBlobOperations
from . import models


class AzureBlobStorage(object):
    """AzureBlobStorage


    :ivar service: Service operations
    :vartype service: blob.operations.ServiceOperations
    :ivar container: Container operations
    :vartype container: blob.operations.ContainerOperations
    :ivar blob: Blob operations
    :vartype blob: blob.operations.BlobOperations
    :ivar page_blob: PageBlob operations
    :vartype page_blob: blob.operations.PageBlobOperations
    :ivar append_blob: AppendBlob operations
    :vartype append_blob: blob.operations.AppendBlobOperations
    :ivar block_blob: BlockBlob operations
    :vartype block_blob: blob.operations.BlockBlobOperations

    :param url: The URL of the service account, container, or blob that is the
     targe of the desired operation.
    :type url: str
    """

    def __init__(self, url=None, config=None, **kwargs):

        base_url = '{url}'
        self._config = config or AzureBlobStorageConfiguration(url, **kwargs)
        pipeline = kwargs.get('pipeline', self._config.build_pipeline())
        self._client = PipelineClient(base_url, config=self._config, pipeline=pipeline, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-03-28'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.service = ServiceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.container = ContainerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.blob = BlobOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.page_blob = PageBlobOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.append_blob = AppendBlobOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.block_blob = BlockBlobOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def __enter__(self):
        self._client.pipeline.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.pipeline.__exit__(*exc_details)
