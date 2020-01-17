# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
from msrest.serialization import Model


class AccessPolicy(Model):
    """An Access policy.

    All required parameters must be populated in order to send to Azure.

    :param start: Required. the date-time the policy is active.
    :type start: ~datetime.datetime
    :param expiry: Required. the date-time the policy expires.
    :type expiry: ~datetime.datetime
    :param permission: Required. the permissions for the acl policy.
    :type permission: str
    """

    _validation = {
        'start': {'required': True},
        'expiry': {'required': True},
        'permission': {'required': True},
    }

    _attribute_map = {
        'start': {'key': 'Start', 'type': 'iso-8601'},
        'expiry': {'key': 'Expiry', 'type': 'iso-8601'},
        'permission': {'key': 'Permission', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AccessPolicy, self).__init__(**kwargs)
        self.start = kwargs.get('start', None)
        self.expiry = kwargs.get('expiry', None)
        self.permission = kwargs.get('permission', None)


class AppleBarrel(Model):
    """A barrel of apples..

    :param good_apples:
    :type good_apples: list[str]
    :param bad_apples:
    :type bad_apples: list[str]
    """

    _attribute_map = {
        'good_apples': {'key': 'GoodApples', 'type': '[str]'},
        'bad_apples': {'key': 'BadApples', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(AppleBarrel, self).__init__(**kwargs)
        self.good_apples = kwargs.get('good_apples', None)
        self.bad_apples = kwargs.get('bad_apples', None)


class Banana(Model):
    """A banana..

    :param name:
    :type name: str
    :param flavor:
    :type flavor: str
    :param expiration: The time at which you should reconsider eating this banana.
    :type expiration: ~datetime.datetime
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'flavor': {'key': 'flavor', 'type': 'str'},
        'expiration': {'key': 'expiration', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(Banana, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.flavor = kwargs.get('flavor', None)
        self.expiration = kwargs.get('expiration', None)


class Blob(Model):
    """An Azure Storage blob.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param deleted: Required.
    :type deleted: bool
    :param snapshot: Required.
    :type snapshot: str
    :param properties: Required. Properties of a blob.
    :type properties: ~xmlservice.models.BlobProperties
    :param metadata: Dictionary of <paths·xml-
     headers·get·responses·200·headers·custom_header·schema>.
    :type metadata: dict[str, str]
    """

    _validation = {
        'name': {'required': True},
        'deleted': {'required': True},
        'snapshot': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'deleted': {'key': 'Deleted', 'type': 'bool'},
        'snapshot': {'key': 'Snapshot', 'type': 'str'},
        'properties': {'key': 'Properties', 'type': 'BlobProperties'},
        'metadata': {'key': 'Metadata', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(Blob, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.deleted = kwargs.get('deleted', None)
        self.snapshot = kwargs.get('snapshot', None)
        self.properties = kwargs.get('properties', None)
        self.metadata = kwargs.get('metadata', None)


class BlobPrefix(Model):
    """BlobPrefix.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BlobPrefix, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)


class BlobProperties(Model):
    """Properties of a blob.

    All required parameters must be populated in order to send to Azure.

    :param last_modified: Required.
    :type last_modified: ~datetime.datetime
    :param etag: Required.
    :type etag: str
    :param content_length: Size in bytes.
    :type content_length: long
    :param content_type:
    :type content_type: str
    :param content_encoding:
    :type content_encoding: str
    :param content_language:
    :type content_language: str
    :param content_md5:
    :type content_md5: str
    :param content_disposition:
    :type content_disposition: str
    :param cache_control:
    :type cache_control: str
    :param blob_sequence_number:
    :type blob_sequence_number: int
    :param blob_type:  Possible values include: 'BlockBlob', 'PageBlob',
     'AppendBlob'.
    :type blob_type: str or ~xmlservice.models.BlobType
    :param lease_status:  Possible values include: 'locked', 'unlocked'.
    :type lease_status: str or ~xmlservice.models.LeaseStatusType
    :param lease_state:  Possible values include: 'available', 'leased', 'expired',
     'breaking', 'broken'.
    :type lease_state: str or ~xmlservice.models.LeaseStateType
    :param lease_duration:  Possible values include: 'infinite', 'fixed'.
    :type lease_duration: str or ~xmlservice.models.LeaseDurationType
    :param copy_id:
    :type copy_id: str
    :param copy_status:  Possible values include: 'pending', 'success', 'aborted',
     'failed'.
    :type copy_status: str or ~xmlservice.models.CopyStatusType
    :param copy_source:
    :type copy_source: str
    :param copy_progress:
    :type copy_progress: str
    :param copy_completion_time:
    :type copy_completion_time: ~datetime.datetime
    :param copy_status_description:
    :type copy_status_description: str
    :param server_encrypted:
    :type server_encrypted: bool
    :param incremental_copy:
    :type incremental_copy: bool
    :param destination_snapshot:
    :type destination_snapshot: str
    :param deleted_time:
    :type deleted_time: ~datetime.datetime
    :param remaining_retention_days:
    :type remaining_retention_days: int
    :param access_tier:  Possible values include: 'P4', 'P6', 'P10', 'P20', 'P30',
     'P40', 'P50', 'Hot', 'Cool', 'Archive'.
    :type access_tier: str or ~xmlservice.models.AccessTier
    :param access_tier_inferred:
    :type access_tier_inferred: bool
    :param archive_status:  Possible values include: 'rehydrate-pending-to-hot',
     'rehydrate-pending-to-cool'.
    :type archive_status: str or ~xmlservice.models.ArchiveStatus
    """

    _validation = {
        'last_modified': {'required': True},
        'etag': {'required': True},
    }

    _attribute_map = {
        'last_modified': {'key': 'Last-Modified', 'type': 'rfc-1123'},
        'etag': {'key': 'Etag', 'type': 'str'},
        'content_length': {'key': 'Content-Length', 'type': 'long'},
        'content_type': {'key': 'Content-Type', 'type': 'str'},
        'content_encoding': {'key': 'Content-Encoding', 'type': 'str'},
        'content_language': {'key': 'Content-Language', 'type': 'str'},
        'content_md5': {'key': 'Content-MD5', 'type': 'str'},
        'content_disposition': {'key': 'Content-Disposition', 'type': 'str'},
        'cache_control': {'key': 'Cache-Control', 'type': 'str'},
        'blob_sequence_number': {'key': 'x-ms-blob-sequence-number', 'type': 'int'},
        'blob_type': {'key': 'BlobType', 'type': 'str'},
        'lease_status': {'key': 'LeaseStatus', 'type': 'str'},
        'lease_state': {'key': 'LeaseState', 'type': 'str'},
        'lease_duration': {'key': 'LeaseDuration', 'type': 'str'},
        'copy_id': {'key': 'CopyId', 'type': 'str'},
        'copy_status': {'key': 'CopyStatus', 'type': 'str'},
        'copy_source': {'key': 'CopySource', 'type': 'str'},
        'copy_progress': {'key': 'CopyProgress', 'type': 'str'},
        'copy_completion_time': {'key': 'CopyCompletionTime', 'type': 'rfc-1123'},
        'copy_status_description': {'key': 'CopyStatusDescription', 'type': 'str'},
        'server_encrypted': {'key': 'ServerEncrypted', 'type': 'bool'},
        'incremental_copy': {'key': 'IncrementalCopy', 'type': 'bool'},
        'destination_snapshot': {'key': 'DestinationSnapshot', 'type': 'str'},
        'deleted_time': {'key': 'DeletedTime', 'type': 'rfc-1123'},
        'remaining_retention_days': {'key': 'RemainingRetentionDays', 'type': 'int'},
        'access_tier': {'key': 'AccessTier', 'type': 'str'},
        'access_tier_inferred': {'key': 'AccessTierInferred', 'type': 'bool'},
        'archive_status': {'key': 'ArchiveStatus', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BlobProperties, self).__init__(**kwargs)
        self.last_modified = kwargs.get('last_modified', None)
        self.etag = kwargs.get('etag', None)
        self.content_length = kwargs.get('content_length', None)
        self.content_type = kwargs.get('content_type', None)
        self.content_encoding = kwargs.get('content_encoding', None)
        self.content_language = kwargs.get('content_language', None)
        self.content_md5 = kwargs.get('content_md5', None)
        self.content_disposition = kwargs.get('content_disposition', None)
        self.cache_control = kwargs.get('cache_control', None)
        self.blob_sequence_number = kwargs.get('blob_sequence_number', None)
        self.blob_type = kwargs.get('blob_type', None)
        self.lease_status = kwargs.get('lease_status', None)
        self.lease_state = kwargs.get('lease_state', None)
        self.lease_duration = kwargs.get('lease_duration', None)
        self.copy_id = kwargs.get('copy_id', None)
        self.copy_status = kwargs.get('copy_status', None)
        self.copy_source = kwargs.get('copy_source', None)
        self.copy_progress = kwargs.get('copy_progress', None)
        self.copy_completion_time = kwargs.get('copy_completion_time', None)
        self.copy_status_description = kwargs.get('copy_status_description', None)
        self.server_encrypted = kwargs.get('server_encrypted', None)
        self.incremental_copy = kwargs.get('incremental_copy', None)
        self.destination_snapshot = kwargs.get('destination_snapshot', None)
        self.deleted_time = kwargs.get('deleted_time', None)
        self.remaining_retention_days = kwargs.get('remaining_retention_days', None)
        self.access_tier = kwargs.get('access_tier', None)
        self.access_tier_inferred = kwargs.get('access_tier_inferred', None)
        self.archive_status = kwargs.get('archive_status', None)


class Blobs(Model):
    """Blobs.

    :param blob_prefix:
    :type blob_prefix: list[~xmlservice.models.BlobPrefix]
    :param blob:
    :type blob: list[~xmlservice.models.Blob]
    """

    _attribute_map = {
        'blob_prefix': {'key': 'BlobPrefix', 'type': '[BlobPrefix]'},
        'blob': {'key': 'Blob', 'type': '[Blob]'},
    }

    def __init__(self, **kwargs):
        super(Blobs, self).__init__(**kwargs)
        self.blob_prefix = kwargs.get('blob_prefix', None)
        self.blob = kwargs.get('blob', None)


class ComplexTypeNoMeta(Model):
    """I am a complex type with no XML node.

    :param id: The id of the res.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'ID', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ComplexTypeNoMeta, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)


class ComplexTypeWithMeta(Model):
    """I am a complex type with XML node.

    :param id: The id of the res.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'ID', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ComplexTypeWithMeta, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)


class Container(Model):
    """An Azure Storage container.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param properties: Required. Properties of a container.
    :type properties: ~xmlservice.models.ContainerProperties
    :param metadata: Dictionary of <paths·xml-
     headers·get·responses·200·headers·custom_header·schema>.
    :type metadata: dict[str, str]
    """

    _validation = {
        'name': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'properties': {'key': 'Properties', 'type': 'ContainerProperties'},
        'metadata': {'key': 'Metadata', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.properties = kwargs.get('properties', None)
        self.metadata = kwargs.get('metadata', None)


class ContainerProperties(Model):
    """Properties of a container.

    All required parameters must be populated in order to send to Azure.

    :param last_modified: Required.
    :type last_modified: ~datetime.datetime
    :param etag: Required.
    :type etag: str
    :param lease_status:  Possible values include: 'locked', 'unlocked'.
    :type lease_status: str or ~xmlservice.models.LeaseStatusType
    :param lease_state:  Possible values include: 'available', 'leased', 'expired',
     'breaking', 'broken'.
    :type lease_state: str or ~xmlservice.models.LeaseStateType
    :param lease_duration:  Possible values include: 'infinite', 'fixed'.
    :type lease_duration: str or ~xmlservice.models.LeaseDurationType
    :param public_access:  Possible values include: 'container', 'blob'.
    :type public_access: str or ~xmlservice.models.PublicAccessType
    """

    _validation = {
        'last_modified': {'required': True},
        'etag': {'required': True},
    }

    _attribute_map = {
        'last_modified': {'key': 'Last-Modified', 'type': 'rfc-1123'},
        'etag': {'key': 'Etag', 'type': 'str'},
        'lease_status': {'key': 'LeaseStatus', 'type': 'str'},
        'lease_state': {'key': 'LeaseState', 'type': 'str'},
        'lease_duration': {'key': 'LeaseDuration', 'type': 'str'},
        'public_access': {'key': 'PublicAccess', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ContainerProperties, self).__init__(**kwargs)
        self.last_modified = kwargs.get('last_modified', None)
        self.etag = kwargs.get('etag', None)
        self.lease_status = kwargs.get('lease_status', None)
        self.lease_state = kwargs.get('lease_state', None)
        self.lease_duration = kwargs.get('lease_duration', None)
        self.public_access = kwargs.get('public_access', None)


class CorsRule(Model):
    """CORS is an HTTP feature that enables a web application running under one domain to access resources in another domain. Web browsers implement a security restriction known as same-origin policy that prevents a web page from calling APIs in a different domain; CORS provides a secure way to allow one domain (the origin domain) to call APIs in another domain.

    All required parameters must be populated in order to send to Azure.

    :param allowed_origins: Required. The origin domains that are permitted to make
     a request against the storage service via CORS. The origin domain is the domain
     from which the request originates. Note that the origin must be an exact case-
     sensitive match with the origin that the user age sends to the service. You can
     also use the wildcard character '*' to allow all origin domains to make requests
     via CORS.
    :type allowed_origins: str
    :param allowed_methods: Required. The methods (HTTP request verbs) that the
     origin domain may use for a CORS request. (comma separated).
    :type allowed_methods: str
    :param allowed_headers: Required. the request headers that the origin domain may
     specify on the CORS request.
    :type allowed_headers: str
    :param exposed_headers: Required. The response headers that may be sent in the
     response to the CORS request and exposed by the browser to the request issuer.
    :type exposed_headers: str
    :param max_age_in_seconds: Required. The maximum amount time that a browser
     should cache the preflight OPTIONS request.
    :type max_age_in_seconds: int
    """

    _validation = {
        'allowed_origins': {'required': True},
        'allowed_methods': {'required': True},
        'allowed_headers': {'required': True},
        'exposed_headers': {'required': True},
        'max_age_in_seconds': {'required': True, 'minimum': 0},
    }

    _attribute_map = {
        'allowed_origins': {'key': 'AllowedOrigins', 'type': 'str'},
        'allowed_methods': {'key': 'AllowedMethods', 'type': 'str'},
        'allowed_headers': {'key': 'AllowedHeaders', 'type': 'str'},
        'exposed_headers': {'key': 'ExposedHeaders', 'type': 'str'},
        'max_age_in_seconds': {'key': 'MaxAgeInSeconds', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(CorsRule, self).__init__(**kwargs)
        self.allowed_origins = kwargs.get('allowed_origins', None)
        self.allowed_methods = kwargs.get('allowed_methods', None)
        self.allowed_headers = kwargs.get('allowed_headers', None)
        self.exposed_headers = kwargs.get('exposed_headers', None)
        self.max_age_in_seconds = kwargs.get('max_age_in_seconds', None)


class ErrorException(HttpResponseError):
    """Server responded with exception of type: 'Error'.

    :param response: Server response to be deserialized.
    :param error_model: A deserialized model of the response body as model.
    """

    def __init__(self, response, error_model):
        self.error = error_model
        super(ErrorException, self).__init__(response=response, error_model=error_model)

    @classmethod
    def from_response(cls, response, deserialize):
        """Deserialize this response as this exception, or a subclass of this exception.

        :param response: Server response to be deserialized.
        :param deserialize: A deserializer
        """
        model_name = 'Error'
        error = deserialize(model_name, response)
        if error is None:
            error = deserialize.dependencies[model_name]()
        return error._EXCEPTION_TYPE(response, error)


class Error(Model):
    """Error.

    :param status:
    :type status: int
    :param message:
    :type message: str
    """
    _EXCEPTION_TYPE = ErrorException

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.message = kwargs.get('message', None)


class JSONInput(Model):
    """JSONInput.

    :param id:
    :type id: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(JSONInput, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)


class JSONOutput(Model):
    """JSONOutput.

    :param id:
    :type id: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(JSONOutput, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)


class ListBlobsResponse(Model):
    """An enumeration of blobs.

    All required parameters must be populated in order to send to Azure.

    :param service_endpoint: Required.
    :type service_endpoint: str
    :param container_name: Required.
    :type container_name: str
    :param prefix: Required.
    :type prefix: str
    :param marker: Required.
    :type marker: str
    :param max_results: Required.
    :type max_results: int
    :param delimiter: Required.
    :type delimiter: str
    :param blobs: Required.
    :type blobs: ~xmlservice.models.Blobs
    :param next_marker: Required.
    :type next_marker: str
    """

    _validation = {
        'service_endpoint': {'required': True},
        'container_name': {'required': True},
        'prefix': {'required': True},
        'marker': {'required': True},
        'max_results': {'required': True},
        'delimiter': {'required': True},
        'blobs': {'required': True},
        'next_marker': {'required': True},
    }

    _attribute_map = {
        'service_endpoint': {'key': 'ServiceEndpoint', 'type': 'str'},
        'container_name': {'key': 'ContainerName', 'type': 'str'},
        'prefix': {'key': 'Prefix', 'type': 'str'},
        'marker': {'key': 'Marker', 'type': 'str'},
        'max_results': {'key': 'MaxResults', 'type': 'int'},
        'delimiter': {'key': 'Delimiter', 'type': 'str'},
        'blobs': {'key': 'Blobs', 'type': 'Blobs'},
        'next_marker': {'key': 'NextMarker', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ListBlobsResponse, self).__init__(**kwargs)
        self.service_endpoint = kwargs.get('service_endpoint', None)
        self.container_name = kwargs.get('container_name', None)
        self.prefix = kwargs.get('prefix', None)
        self.marker = kwargs.get('marker', None)
        self.max_results = kwargs.get('max_results', None)
        self.delimiter = kwargs.get('delimiter', None)
        self.blobs = kwargs.get('blobs', None)
        self.next_marker = kwargs.get('next_marker', None)


class ListContainersResponse(Model):
    """An enumeration of containers.

    All required parameters must be populated in order to send to Azure.

    :param service_endpoint: Required.
    :type service_endpoint: str
    :param prefix: Required.
    :type prefix: str
    :param marker:
    :type marker: str
    :param max_results: Required.
    :type max_results: int
    :param containers:
    :type containers: list[~xmlservice.models.Container]
    :param next_marker: Required.
    :type next_marker: str
    """

    _validation = {
        'service_endpoint': {'required': True},
        'prefix': {'required': True},
        'max_results': {'required': True},
        'next_marker': {'required': True},
    }

    _attribute_map = {
        'service_endpoint': {'key': 'ServiceEndpoint', 'type': 'str'},
        'prefix': {'key': 'Prefix', 'type': 'str'},
        'marker': {'key': 'Marker', 'type': 'str'},
        'max_results': {'key': 'MaxResults', 'type': 'int'},
        'containers': {'key': 'Containers', 'type': '[Container]'},
        'next_marker': {'key': 'NextMarker', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ListContainersResponse, self).__init__(**kwargs)
        self.service_endpoint = kwargs.get('service_endpoint', None)
        self.prefix = kwargs.get('prefix', None)
        self.marker = kwargs.get('marker', None)
        self.max_results = kwargs.get('max_results', None)
        self.containers = kwargs.get('containers', None)
        self.next_marker = kwargs.get('next_marker', None)


class Logging(Model):
    """Azure Analytics Logging settings..

    All required parameters must be populated in order to send to Azure.

    :param version: Required. The version of Storage Analytics to configure.
    :type version: str
    :param delete: Required. Indicates whether all delete requests should be logged.
    :type delete: bool
    :param read: Required. Indicates whether all read requests should be logged.
    :type read: bool
    :param write: Required. Indicates whether all write requests should be logged.
    :type write: bool
    :param retention_policy: Required. the retention policy.
    :type retention_policy: ~xmlservice.models.RetentionPolicy
    """

    _validation = {
        'version': {'required': True},
        'delete': {'required': True},
        'read': {'required': True},
        'write': {'required': True},
        'retention_policy': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'Version', 'type': 'str'},
        'delete': {'key': 'Delete', 'type': 'bool'},
        'read': {'key': 'Read', 'type': 'bool'},
        'write': {'key': 'Write', 'type': 'bool'},
        'retention_policy': {'key': 'RetentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(self, **kwargs):
        super(Logging, self).__init__(**kwargs)
        self.version = kwargs.get('version', None)
        self.delete = kwargs.get('delete', None)
        self.read = kwargs.get('read', None)
        self.write = kwargs.get('write', None)
        self.retention_policy = kwargs.get('retention_policy', None)


class Metrics(Model):
    """Metrics.

    All required parameters must be populated in order to send to Azure.

    :param version: The version of Storage Analytics to configure.
    :type version: str
    :param enabled: Required. Indicates whether metrics are enabled for the Blob
     service.
    :type enabled: bool
    :param include_apis: Indicates whether metrics should generate summary
     statistics for called API operations.
    :type include_apis: bool
    :param retention_policy: the retention policy.
    :type retention_policy: ~xmlservice.models.RetentionPolicy
    """

    _validation = {
        'enabled': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'Version', 'type': 'str'},
        'enabled': {'key': 'Enabled', 'type': 'bool'},
        'include_apis': {'key': 'IncludeAPIs', 'type': 'bool'},
        'retention_policy': {'key': 'RetentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(self, **kwargs):
        super(Metrics, self).__init__(**kwargs)
        self.version = kwargs.get('version', None)
        self.enabled = kwargs.get('enabled', None)
        self.include_apis = kwargs.get('include_apis', None)
        self.retention_policy = kwargs.get('retention_policy', None)


class RetentionPolicy(Model):
    """the retention policy.

    All required parameters must be populated in order to send to Azure.

    :param enabled: Required. Indicates whether a retention policy is enabled for
     the storage service.
    :type enabled: bool
    :param days: Indicates the number of days that metrics or logging or soft-
     deleted data should be retained. All data older than this value will be deleted.
    :type days: int
    """

    _validation = {
        'enabled': {'required': True},
        'days': {'minimum': 1},
    }

    _attribute_map = {
        'enabled': {'key': 'Enabled', 'type': 'bool'},
        'days': {'key': 'Days', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(RetentionPolicy, self).__init__(**kwargs)
        self.enabled = kwargs.get('enabled', None)
        self.days = kwargs.get('days', None)


class RootWithRefAndMeta(Model):
    """I am root, and I ref a model WITH meta.

    :param ref_to_model: I am a complex type with XML node.
    :type ref_to_model: ~xmlservice.models.ComplexTypeWithMeta
    :param something: Something else (just to avoid flattening).
    :type something: str
    """

    _attribute_map = {
        'ref_to_model': {'key': 'RefToModel', 'type': 'ComplexTypeWithMeta'},
        'something': {'key': 'Something', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RootWithRefAndMeta, self).__init__(**kwargs)
        self.ref_to_model = kwargs.get('ref_to_model', None)
        self.something = kwargs.get('something', None)


class RootWithRefAndNoMeta(Model):
    """I am root, and I ref a model with no meta.

    :param ref_to_model: I am a complex type with no XML node.
    :type ref_to_model: ~xmlservice.models.ComplexTypeNoMeta
    :param something: Something else (just to avoid flattening).
    :type something: str
    """

    _attribute_map = {
        'ref_to_model': {'key': 'RefToModel', 'type': 'ComplexTypeNoMeta'},
        'something': {'key': 'Something', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RootWithRefAndNoMeta, self).__init__(**kwargs)
        self.ref_to_model = kwargs.get('ref_to_model', None)
        self.something = kwargs.get('something', None)


class SignedIdentifier(Model):
    """signed identifier.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. a unique id.
    :type id: str
    :param access_policy: Required. An Access policy.
    :type access_policy: ~xmlservice.models.AccessPolicy
    """

    _validation = {
        'id': {'required': True},
        'access_policy': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str'},
        'access_policy': {'key': 'AccessPolicy', 'type': 'AccessPolicy'},
    }

    def __init__(self, **kwargs):
        super(SignedIdentifier, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.access_policy = kwargs.get('access_policy', None)


class Slide(Model):
    """A slide in a slideshow.

    :param type:
    :type type: str
    :param title:
    :type title: str
    :param items:
    :type items: list[str]
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'items': {'key': 'items', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(Slide, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.title = kwargs.get('title', None)
        self.items = kwargs.get('items', None)


class Slideshow(Model):
    """Data about a slideshow.

    :param title:
    :type title: str
    :param date_property:
    :type date_property: str
    :param author:
    :type author: str
    :param slides:
    :type slides: list[~xmlservice.models.Slide]
    """

    _attribute_map = {
        'title': {'key': 'title', 'type': 'str'},
        'date_property': {'key': 'date', 'type': 'str'},
        'author': {'key': 'author', 'type': 'str'},
        'slides': {'key': 'slides', 'type': '[Slide]'},
    }

    def __init__(self, **kwargs):
        super(Slideshow, self).__init__(**kwargs)
        self.title = kwargs.get('title', None)
        self.date_property = kwargs.get('date_property', None)
        self.author = kwargs.get('author', None)
        self.slides = kwargs.get('slides', None)


class StorageServiceProperties(Model):
    """Storage Service Properties..

    :param logging: Azure Analytics Logging settings.
    :type logging: ~xmlservice.models.Logging
    :param hour_metrics:
    :type hour_metrics: ~xmlservice.models.Metrics
    :param minute_metrics:
    :type minute_metrics: ~xmlservice.models.Metrics
    :param cors: The set of CORS rules.
    :type cors: list[~xmlservice.models.CorsRule]
    :param default_service_version: The default version to use for requests to the
     Blob service if an incoming request's version is not specified. Possible values
     include version 2008-10-27 and all more recent versions.
    :type default_service_version: str
    :param delete_retention_policy: the retention policy.
    :type delete_retention_policy: ~xmlservice.models.RetentionPolicy
    """

    _attribute_map = {
        'logging': {'key': 'Logging', 'type': 'Logging'},
        'hour_metrics': {'key': 'HourMetrics', 'type': 'Metrics'},
        'minute_metrics': {'key': 'MinuteMetrics', 'type': 'Metrics'},
        'cors': {'key': 'Cors', 'type': '[CorsRule]'},
        'default_service_version': {'key': 'DefaultServiceVersion', 'type': 'str'},
        'delete_retention_policy': {'key': 'DeleteRetentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(self, **kwargs):
        super(StorageServiceProperties, self).__init__(**kwargs)
        self.logging = kwargs.get('logging', None)
        self.hour_metrics = kwargs.get('hour_metrics', None)
        self.minute_metrics = kwargs.get('minute_metrics', None)
        self.cors = kwargs.get('cors', None)
        self.default_service_version = kwargs.get('default_service_version', None)
        self.delete_retention_policy = kwargs.get('delete_retention_policy', None)
