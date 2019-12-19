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

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class AccessPolicy(Model):
    """An Access policy.

    All required parameters must be populated in order to send to Azure.

    :param start: Required. the date-time the policy is active
    :type start: datetime
    :param expiry: Required. the date-time the policy expires
    :type expiry: datetime
    :param permission: Required. the permissions for the acl policy
    :type permission: str
    """

    _validation = {
        'start': {'required': True},
        'expiry': {'required': True},
        'permission': {'required': True},
    }

    _attribute_map = {
        'start': {'key': 'Start', 'type': 'iso-8601', 'xml': {'name': 'Start'}},
        'expiry': {'key': 'Expiry', 'type': 'iso-8601', 'xml': {'name': 'Expiry'}},
        'permission': {'key': 'Permission', 'type': 'str', 'xml': {'name': 'Permission'}},
    }
    _xml_map = {
    }

    def __init__(self, *, start, expiry, permission: str, **kwargs) -> None:
        super(AccessPolicy, self).__init__(**kwargs)
        self.start = start
        self.expiry = expiry
        self.permission = permission


class AppleBarrel(Model):
    """A barrel of apples.

    :param good_apples:
    :type good_apples: list[str]
    :param bad_apples:
    :type bad_apples: list[str]
    """

    _attribute_map = {
        'good_apples': {'key': 'GoodApples', 'type': '[str]', 'xml': {'name': 'GoodApples', 'itemsName': 'Apple', 'wrapped': True}},
        'bad_apples': {'key': 'BadApples', 'type': '[str]', 'xml': {'name': 'BadApples', 'itemsName': 'Apple', 'wrapped': True}},
    }
    _xml_map = {
    }

    def __init__(self, *, good_apples=None, bad_apples=None, **kwargs) -> None:
        super(AppleBarrel, self).__init__(**kwargs)
        self.good_apples = good_apples
        self.bad_apples = bad_apples


class Banana(Model):
    """A banana.

    :param name:
    :type name: str
    :param flavor:
    :type flavor: str
    :param expiration: The time at which you should reconsider eating this
     banana
    :type expiration: datetime
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str', 'xml': {'name': 'name'}},
        'flavor': {'key': 'flavor', 'type': 'str', 'xml': {'name': 'flavor'}},
        'expiration': {'key': 'expiration', 'type': 'iso-8601', 'xml': {'name': 'expiration'}},
    }
    _xml_map = {
        'name': 'banana'
    }

    def __init__(self, *, name: str=None, flavor: str=None, expiration=None, **kwargs) -> None:
        super(Banana, self).__init__(**kwargs)
        self.name = name
        self.flavor = flavor
        self.expiration = expiration


class Blob(Model):
    """An Azure Storage blob.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param deleted: Required.
    :type deleted: bool
    :param snapshot: Required.
    :type snapshot: str
    :param properties: Required.
    :type properties: ~xmlservice.models.BlobProperties
    :param metadata:
    :type metadata: dict[str, str]
    """

    _validation = {
        'name': {'required': True},
        'deleted': {'required': True},
        'snapshot': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str', 'xml': {'name': 'Name'}},
        'deleted': {'key': 'Deleted', 'type': 'bool', 'xml': {'name': 'Deleted'}},
        'snapshot': {'key': 'Snapshot', 'type': 'str', 'xml': {'name': 'Snapshot'}},
        'properties': {'key': 'Properties', 'type': 'BlobProperties', 'xml': {'name': 'Properties'}},
        'metadata': {'key': 'Metadata', 'type': '{str}', 'xml': {'name': 'Metadata'}},
    }
    _xml_map = {
        'name': 'Blob'
    }

    def __init__(self, *, name: str, deleted: bool, snapshot: str, properties, metadata=None, **kwargs) -> None:
        super(Blob, self).__init__(**kwargs)
        self.name = name
        self.deleted = deleted
        self.snapshot = snapshot
        self.properties = properties
        self.metadata = metadata


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
        'name': {'key': 'Name', 'type': 'str', 'xml': {'name': 'Name'}},
    }
    _xml_map = {
    }

    def __init__(self, *, name: str, **kwargs) -> None:
        super(BlobPrefix, self).__init__(**kwargs)
        self.name = name


class BlobProperties(Model):
    """Properties of a blob.

    All required parameters must be populated in order to send to Azure.

    :param last_modified: Required.
    :type last_modified: datetime
    :param etag: Required.
    :type etag: str
    :param content_length: Size in bytes
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
    :param blob_type: Possible values include: 'BlockBlob', 'PageBlob',
     'AppendBlob'
    :type blob_type: str or ~xmlservice.models.BlobType
    :param lease_status: Possible values include: 'locked', 'unlocked'
    :type lease_status: str or ~xmlservice.models.LeaseStatusType
    :param lease_state: Possible values include: 'available', 'leased',
     'expired', 'breaking', 'broken'
    :type lease_state: str or ~xmlservice.models.LeaseStateType
    :param lease_duration: Possible values include: 'infinite', 'fixed'
    :type lease_duration: str or ~xmlservice.models.LeaseDurationType
    :param copy_id:
    :type copy_id: str
    :param copy_status: Possible values include: 'pending', 'success',
     'aborted', 'failed'
    :type copy_status: str or ~xmlservice.models.CopyStatusType
    :param copy_source:
    :type copy_source: str
    :param copy_progress:
    :type copy_progress: str
    :param copy_completion_time:
    :type copy_completion_time: datetime
    :param copy_status_description:
    :type copy_status_description: str
    :param server_encrypted:
    :type server_encrypted: bool
    :param incremental_copy:
    :type incremental_copy: bool
    :param destination_snapshot:
    :type destination_snapshot: str
    :param deleted_time:
    :type deleted_time: datetime
    :param remaining_retention_days:
    :type remaining_retention_days: int
    :param access_tier: Possible values include: 'P4', 'P6', 'P10', 'P20',
     'P30', 'P40', 'P50', 'Hot', 'Cool', 'Archive'
    :type access_tier: str or ~xmlservice.models.AccessTier
    :param access_tier_inferred:
    :type access_tier_inferred: bool
    :param archive_status: Possible values include:
     'rehydrate-pending-to-hot', 'rehydrate-pending-to-cool'
    :type archive_status: str or ~xmlservice.models.ArchiveStatus
    """

    _validation = {
        'last_modified': {'required': True},
        'etag': {'required': True},
    }

    _attribute_map = {
        'last_modified': {'key': 'Last-Modified', 'type': 'rfc-1123', 'xml': {'name': 'Last-Modified'}},
        'etag': {'key': 'Etag', 'type': 'str', 'xml': {'name': 'Etag'}},
        'content_length': {'key': 'Content-Length', 'type': 'long', 'xml': {'name': 'Content-Length'}},
        'content_type': {'key': 'Content-Type', 'type': 'str', 'xml': {'name': 'Content-Type'}},
        'content_encoding': {'key': 'Content-Encoding', 'type': 'str', 'xml': {'name': 'Content-Encoding'}},
        'content_language': {'key': 'Content-Language', 'type': 'str', 'xml': {'name': 'Content-Language'}},
        'content_md5': {'key': 'Content-MD5', 'type': 'str', 'xml': {'name': 'Content-MD5'}},
        'content_disposition': {'key': 'Content-Disposition', 'type': 'str', 'xml': {'name': 'Content-Disposition'}},
        'cache_control': {'key': 'Cache-Control', 'type': 'str', 'xml': {'name': 'Cache-Control'}},
        'blob_sequence_number': {'key': 'x-ms-blob-sequence-number', 'type': 'int', 'xml': {'name': 'x-ms-blob-sequence-number'}},
        'blob_type': {'key': 'BlobType', 'type': 'BlobType', 'xml': {'name': 'BlobType'}},
        'lease_status': {'key': 'LeaseStatus', 'type': 'LeaseStatusType', 'xml': {'name': 'LeaseStatus'}},
        'lease_state': {'key': 'LeaseState', 'type': 'LeaseStateType', 'xml': {'name': 'LeaseState'}},
        'lease_duration': {'key': 'LeaseDuration', 'type': 'LeaseDurationType', 'xml': {'name': 'LeaseDuration'}},
        'copy_id': {'key': 'CopyId', 'type': 'str', 'xml': {'name': 'CopyId'}},
        'copy_status': {'key': 'CopyStatus', 'type': 'CopyStatusType', 'xml': {'name': 'CopyStatus'}},
        'copy_source': {'key': 'CopySource', 'type': 'str', 'xml': {'name': 'CopySource'}},
        'copy_progress': {'key': 'CopyProgress', 'type': 'str', 'xml': {'name': 'CopyProgress'}},
        'copy_completion_time': {'key': 'CopyCompletionTime', 'type': 'rfc-1123', 'xml': {'name': 'CopyCompletionTime'}},
        'copy_status_description': {'key': 'CopyStatusDescription', 'type': 'str', 'xml': {'name': 'CopyStatusDescription'}},
        'server_encrypted': {'key': 'ServerEncrypted', 'type': 'bool', 'xml': {'name': 'ServerEncrypted'}},
        'incremental_copy': {'key': 'IncrementalCopy', 'type': 'bool', 'xml': {'name': 'IncrementalCopy'}},
        'destination_snapshot': {'key': 'DestinationSnapshot', 'type': 'str', 'xml': {'name': 'DestinationSnapshot'}},
        'deleted_time': {'key': 'DeletedTime', 'type': 'rfc-1123', 'xml': {'name': 'DeletedTime'}},
        'remaining_retention_days': {'key': 'RemainingRetentionDays', 'type': 'int', 'xml': {'name': 'RemainingRetentionDays'}},
        'access_tier': {'key': 'AccessTier', 'type': 'str', 'xml': {'name': 'AccessTier'}},
        'access_tier_inferred': {'key': 'AccessTierInferred', 'type': 'bool', 'xml': {'name': 'AccessTierInferred'}},
        'archive_status': {'key': 'ArchiveStatus', 'type': 'str', 'xml': {'name': 'ArchiveStatus'}},
    }
    _xml_map = {
    }

    def __init__(self, *, last_modified, etag: str, content_length: int=None, content_type: str=None, content_encoding: str=None, content_language: str=None, content_md5: str=None, content_disposition: str=None, cache_control: str=None, blob_sequence_number: int=None, blob_type=None, lease_status=None, lease_state=None, lease_duration=None, copy_id: str=None, copy_status=None, copy_source: str=None, copy_progress: str=None, copy_completion_time=None, copy_status_description: str=None, server_encrypted: bool=None, incremental_copy: bool=None, destination_snapshot: str=None, deleted_time=None, remaining_retention_days: int=None, access_tier=None, access_tier_inferred: bool=None, archive_status=None, **kwargs) -> None:
        super(BlobProperties, self).__init__(**kwargs)
        self.last_modified = last_modified
        self.etag = etag
        self.content_length = content_length
        self.content_type = content_type
        self.content_encoding = content_encoding
        self.content_language = content_language
        self.content_md5 = content_md5
        self.content_disposition = content_disposition
        self.cache_control = cache_control
        self.blob_sequence_number = blob_sequence_number
        self.blob_type = blob_type
        self.lease_status = lease_status
        self.lease_state = lease_state
        self.lease_duration = lease_duration
        self.copy_id = copy_id
        self.copy_status = copy_status
        self.copy_source = copy_source
        self.copy_progress = copy_progress
        self.copy_completion_time = copy_completion_time
        self.copy_status_description = copy_status_description
        self.server_encrypted = server_encrypted
        self.incremental_copy = incremental_copy
        self.destination_snapshot = destination_snapshot
        self.deleted_time = deleted_time
        self.remaining_retention_days = remaining_retention_days
        self.access_tier = access_tier
        self.access_tier_inferred = access_tier_inferred
        self.archive_status = archive_status


class Blobs(Model):
    """Blobs.

    :param blob_prefix:
    :type blob_prefix: list[~xmlservice.models.BlobPrefix]
    :param blob:
    :type blob: list[~xmlservice.models.Blob]
    """

    _attribute_map = {
        'blob_prefix': {'key': 'BlobPrefix', 'type': '[BlobPrefix]', 'xml': {'name': 'BlobPrefix', 'itemsName': 'BlobPrefix'}},
        'blob': {'key': 'Blob', 'type': '[Blob]', 'xml': {'name': 'Blob', 'itemsName': 'Blob'}},
    }
    _xml_map = {
    }

    def __init__(self, *, blob_prefix=None, blob=None, **kwargs) -> None:
        super(Blobs, self).__init__(**kwargs)
        self.blob_prefix = blob_prefix
        self.blob = blob


class ComplexTypeNoMeta(Model):
    """I am a complex type with no XML node.

    :param id: The id of the res
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'ID', 'type': 'str', 'xml': {'name': 'ID'}},
    }
    _xml_map = {
    }

    def __init__(self, *, id: str=None, **kwargs) -> None:
        super(ComplexTypeNoMeta, self).__init__(**kwargs)
        self.id = id


class ComplexTypeWithMeta(Model):
    """I am a complex type with XML node.

    :param id: The id of the res
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'ID', 'type': 'str', 'xml': {'name': 'ID'}},
    }
    _xml_map = {
        'name': 'XMLComplexTypeWithMeta'
    }

    def __init__(self, *, id: str=None, **kwargs) -> None:
        super(ComplexTypeWithMeta, self).__init__(**kwargs)
        self.id = id


class Container(Model):
    """An Azure Storage container.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param properties: Required.
    :type properties: ~xmlservice.models.ContainerProperties
    :param metadata:
    :type metadata: dict[str, str]
    """

    _validation = {
        'name': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str', 'xml': {'name': 'Name'}},
        'properties': {'key': 'Properties', 'type': 'ContainerProperties', 'xml': {'name': 'Properties'}},
        'metadata': {'key': 'Metadata', 'type': '{str}', 'xml': {'name': 'Metadata'}},
    }
    _xml_map = {
    }

    def __init__(self, *, name: str, properties, metadata=None, **kwargs) -> None:
        super(Container, self).__init__(**kwargs)
        self.name = name
        self.properties = properties
        self.metadata = metadata


class ContainerProperties(Model):
    """Properties of a container.

    All required parameters must be populated in order to send to Azure.

    :param last_modified: Required.
    :type last_modified: datetime
    :param etag: Required.
    :type etag: str
    :param lease_status: Possible values include: 'locked', 'unlocked'
    :type lease_status: str or ~xmlservice.models.LeaseStatusType
    :param lease_state: Possible values include: 'available', 'leased',
     'expired', 'breaking', 'broken'
    :type lease_state: str or ~xmlservice.models.LeaseStateType
    :param lease_duration: Possible values include: 'infinite', 'fixed'
    :type lease_duration: str or ~xmlservice.models.LeaseDurationType
    :param public_access: Possible values include: 'container', 'blob'
    :type public_access: str or ~xmlservice.models.PublicAccessType
    """

    _validation = {
        'last_modified': {'required': True},
        'etag': {'required': True},
    }

    _attribute_map = {
        'last_modified': {'key': 'Last-Modified', 'type': 'rfc-1123', 'xml': {'name': 'Last-Modified'}},
        'etag': {'key': 'Etag', 'type': 'str', 'xml': {'name': 'Etag'}},
        'lease_status': {'key': 'LeaseStatus', 'type': 'LeaseStatusType', 'xml': {'name': 'LeaseStatus'}},
        'lease_state': {'key': 'LeaseState', 'type': 'LeaseStateType', 'xml': {'name': 'LeaseState'}},
        'lease_duration': {'key': 'LeaseDuration', 'type': 'LeaseDurationType', 'xml': {'name': 'LeaseDuration'}},
        'public_access': {'key': 'PublicAccess', 'type': 'str', 'xml': {'name': 'PublicAccess'}},
    }
    _xml_map = {
    }

    def __init__(self, *, last_modified, etag: str, lease_status=None, lease_state=None, lease_duration=None, public_access=None, **kwargs) -> None:
        super(ContainerProperties, self).__init__(**kwargs)
        self.last_modified = last_modified
        self.etag = etag
        self.lease_status = lease_status
        self.lease_state = lease_state
        self.lease_duration = lease_duration
        self.public_access = public_access


class CorsRule(Model):
    """CORS is an HTTP feature that enables a web application running under one
    domain to access resources in another domain. Web browsers implement a
    security restriction known as same-origin policy that prevents a web page
    from calling APIs in a different domain; CORS provides a secure way to
    allow one domain (the origin domain) to call APIs in another domain.

    All required parameters must be populated in order to send to Azure.

    :param allowed_origins: Required. The origin domains that are permitted to
     make a request against the storage service via CORS. The origin domain is
     the domain from which the request originates. Note that the origin must be
     an exact case-sensitive match with the origin that the user age sends to
     the service. You can also use the wildcard character '*' to allow all
     origin domains to make requests via CORS.
    :type allowed_origins: str
    :param allowed_methods: Required. The methods (HTTP request verbs) that
     the origin domain may use for a CORS request. (comma separated)
    :type allowed_methods: str
    :param allowed_headers: Required. the request headers that the origin
     domain may specify on the CORS request.
    :type allowed_headers: str
    :param exposed_headers: Required. The response headers that may be sent in
     the response to the CORS request and exposed by the browser to the request
     issuer
    :type exposed_headers: str
    :param max_age_in_seconds: Required. The maximum amount time that a
     browser should cache the preflight OPTIONS request.
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
        'allowed_origins': {'key': 'AllowedOrigins', 'type': 'str', 'xml': {'name': 'AllowedOrigins'}},
        'allowed_methods': {'key': 'AllowedMethods', 'type': 'str', 'xml': {'name': 'AllowedMethods'}},
        'allowed_headers': {'key': 'AllowedHeaders', 'type': 'str', 'xml': {'name': 'AllowedHeaders'}},
        'exposed_headers': {'key': 'ExposedHeaders', 'type': 'str', 'xml': {'name': 'ExposedHeaders'}},
        'max_age_in_seconds': {'key': 'MaxAgeInSeconds', 'type': 'int', 'xml': {'name': 'MaxAgeInSeconds'}},
    }
    _xml_map = {
        'name': 'CorsRule'
    }

    def __init__(self, *, allowed_origins: str, allowed_methods: str, allowed_headers: str, exposed_headers: str, max_age_in_seconds: int, **kwargs) -> None:
        super(CorsRule, self).__init__(**kwargs)
        self.allowed_origins = allowed_origins
        self.allowed_methods = allowed_methods
        self.allowed_headers = allowed_headers
        self.exposed_headers = exposed_headers
        self.max_age_in_seconds = max_age_in_seconds


class Error(Model):
    """Error.

    :param status:
    :type status: int
    :param message:
    :type message: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int', 'xml': {'name': 'status'}},
        'message': {'key': 'message', 'type': 'str', 'xml': {'name': 'message'}},
    }
    _xml_map = {
    }

    def __init__(self, *, status: int=None, message: str=None, **kwargs) -> None:
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message


class ErrorException(HttpOperationError):
    """Server responsed with exception of type: 'Error'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorException, self).__init__(deserialize, response, 'Error', *args)


class JSONInput(Model):
    """JSONInput.

    :param id:
    :type id: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int', 'xml': {'name': 'id'}},
    }
    _xml_map = {
    }

    def __init__(self, *, id: int=None, **kwargs) -> None:
        super(JSONInput, self).__init__(**kwargs)
        self.id = id


class JSONOutput(Model):
    """JSONOutput.

    :param id:
    :type id: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int', 'xml': {'name': 'id'}},
    }
    _xml_map = {
    }

    def __init__(self, *, id: int=None, **kwargs) -> None:
        super(JSONOutput, self).__init__(**kwargs)
        self.id = id


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
        'service_endpoint': {'key': 'ServiceEndpoint', 'type': 'str', 'xml': {'name': 'ServiceEndpoint', 'attr': True}},
        'container_name': {'key': 'ContainerName', 'type': 'str', 'xml': {'name': 'ContainerName', 'attr': True}},
        'prefix': {'key': 'Prefix', 'type': 'str', 'xml': {'name': 'Prefix'}},
        'marker': {'key': 'Marker', 'type': 'str', 'xml': {'name': 'Marker'}},
        'max_results': {'key': 'MaxResults', 'type': 'int', 'xml': {'name': 'MaxResults'}},
        'delimiter': {'key': 'Delimiter', 'type': 'str', 'xml': {'name': 'Delimiter'}},
        'blobs': {'key': 'Blobs', 'type': 'Blobs', 'xml': {'name': 'Blobs'}},
        'next_marker': {'key': 'NextMarker', 'type': 'str', 'xml': {'name': 'NextMarker'}},
    }
    _xml_map = {
        'name': 'EnumerationResults'
    }

    def __init__(self, *, service_endpoint: str, container_name: str, prefix: str, marker: str, max_results: int, delimiter: str, blobs, next_marker: str, **kwargs) -> None:
        super(ListBlobsResponse, self).__init__(**kwargs)
        self.service_endpoint = service_endpoint
        self.container_name = container_name
        self.prefix = prefix
        self.marker = marker
        self.max_results = max_results
        self.delimiter = delimiter
        self.blobs = blobs
        self.next_marker = next_marker


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
        'service_endpoint': {'key': 'ServiceEndpoint', 'type': 'str', 'xml': {'name': 'ServiceEndpoint', 'attr': True}},
        'prefix': {'key': 'Prefix', 'type': 'str', 'xml': {'name': 'Prefix'}},
        'marker': {'key': 'Marker', 'type': 'str', 'xml': {'name': 'Marker'}},
        'max_results': {'key': 'MaxResults', 'type': 'int', 'xml': {'name': 'MaxResults'}},
        'containers': {'key': 'Containers', 'type': '[Container]', 'xml': {'name': 'Containers', 'itemsName': 'Container', 'wrapped': True}},
        'next_marker': {'key': 'NextMarker', 'type': 'str', 'xml': {'name': 'NextMarker'}},
    }
    _xml_map = {
        'name': 'EnumerationResults'
    }

    def __init__(self, *, service_endpoint: str, prefix: str, max_results: int, next_marker: str, marker: str=None, containers=None, **kwargs) -> None:
        super(ListContainersResponse, self).__init__(**kwargs)
        self.service_endpoint = service_endpoint
        self.prefix = prefix
        self.marker = marker
        self.max_results = max_results
        self.containers = containers
        self.next_marker = next_marker


class Logging(Model):
    """Azure Analytics Logging settings.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. The version of Storage Analytics to configure.
    :type version: str
    :param delete: Required. Indicates whether all delete requests should be
     logged.
    :type delete: bool
    :param read: Required. Indicates whether all read requests should be
     logged.
    :type read: bool
    :param write: Required. Indicates whether all write requests should be
     logged.
    :type write: bool
    :param retention_policy: Required.
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
        'version': {'key': 'Version', 'type': 'str', 'xml': {'name': 'Version'}},
        'delete': {'key': 'Delete', 'type': 'bool', 'xml': {'name': 'Delete'}},
        'read': {'key': 'Read', 'type': 'bool', 'xml': {'name': 'Read'}},
        'write': {'key': 'Write', 'type': 'bool', 'xml': {'name': 'Write'}},
        'retention_policy': {'key': 'RetentionPolicy', 'type': 'RetentionPolicy', 'xml': {'name': 'RetentionPolicy'}},
    }
    _xml_map = {
    }

    def __init__(self, *, version: str, delete: bool, read: bool, write: bool, retention_policy, **kwargs) -> None:
        super(Logging, self).__init__(**kwargs)
        self.version = version
        self.delete = delete
        self.read = read
        self.write = write
        self.retention_policy = retention_policy


class Metrics(Model):
    """Metrics.

    All required parameters must be populated in order to send to Azure.

    :param version: The version of Storage Analytics to configure.
    :type version: str
    :param enabled: Required. Indicates whether metrics are enabled for the
     Blob service.
    :type enabled: bool
    :param include_ap_is: Indicates whether metrics should generate summary
     statistics for called API operations.
    :type include_ap_is: bool
    :param retention_policy:
    :type retention_policy: ~xmlservice.models.RetentionPolicy
    """

    _validation = {
        'enabled': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'Version', 'type': 'str', 'xml': {'name': 'Version'}},
        'enabled': {'key': 'Enabled', 'type': 'bool', 'xml': {'name': 'Enabled'}},
        'include_ap_is': {'key': 'IncludeAPIs', 'type': 'bool', 'xml': {'name': 'IncludeAPIs'}},
        'retention_policy': {'key': 'RetentionPolicy', 'type': 'RetentionPolicy', 'xml': {'name': 'RetentionPolicy'}},
    }
    _xml_map = {
    }

    def __init__(self, *, enabled: bool, version: str=None, include_ap_is: bool=None, retention_policy=None, **kwargs) -> None:
        super(Metrics, self).__init__(**kwargs)
        self.version = version
        self.enabled = enabled
        self.include_ap_is = include_ap_is
        self.retention_policy = retention_policy


class RetentionPolicy(Model):
    """the retention policy.

    All required parameters must be populated in order to send to Azure.

    :param enabled: Required. Indicates whether a retention policy is enabled
     for the storage service
    :type enabled: bool
    :param days: Indicates the number of days that metrics or logging or
     soft-deleted data should be retained. All data older than this value will
     be deleted
    :type days: int
    """

    _validation = {
        'enabled': {'required': True},
        'days': {'minimum': 1},
    }

    _attribute_map = {
        'enabled': {'key': 'Enabled', 'type': 'bool', 'xml': {'name': 'Enabled'}},
        'days': {'key': 'Days', 'type': 'int', 'xml': {'name': 'Days'}},
    }
    _xml_map = {
    }

    def __init__(self, *, enabled: bool, days: int=None, **kwargs) -> None:
        super(RetentionPolicy, self).__init__(**kwargs)
        self.enabled = enabled
        self.days = days


class RootWithRefAndMeta(Model):
    """I am root, and I ref a model WITH meta.

    :param ref_to_model: XML will use XMLComplexTypeWithMeta
    :type ref_to_model: ~xmlservice.models.ComplexTypeWithMeta
    :param something: Something else (just to avoid flattening)
    :type something: str
    """

    _attribute_map = {
        'ref_to_model': {'key': 'RefToModel', 'type': 'ComplexTypeWithMeta', 'xml': {'name': 'RefToModel'}},
        'something': {'key': 'Something', 'type': 'str', 'xml': {'name': 'Something'}},
    }
    _xml_map = {
    }

    def __init__(self, *, ref_to_model=None, something: str=None, **kwargs) -> None:
        super(RootWithRefAndMeta, self).__init__(**kwargs)
        self.ref_to_model = ref_to_model
        self.something = something


class RootWithRefAndNoMeta(Model):
    """I am root, and I ref a model with no meta.

    :param ref_to_model: XML will use RefToModel
    :type ref_to_model: ~xmlservice.models.ComplexTypeNoMeta
    :param something: Something else (just to avoid flattening)
    :type something: str
    """

    _attribute_map = {
        'ref_to_model': {'key': 'RefToModel', 'type': 'ComplexTypeNoMeta', 'xml': {'name': 'RefToModel'}},
        'something': {'key': 'Something', 'type': 'str', 'xml': {'name': 'Something'}},
    }
    _xml_map = {
    }

    def __init__(self, *, ref_to_model=None, something: str=None, **kwargs) -> None:
        super(RootWithRefAndNoMeta, self).__init__(**kwargs)
        self.ref_to_model = ref_to_model
        self.something = something


class SignedIdentifier(Model):
    """signed identifier.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. a unique id
    :type id: str
    :param access_policy: Required. The access policy
    :type access_policy: ~xmlservice.models.AccessPolicy
    """

    _validation = {
        'id': {'required': True},
        'access_policy': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str', 'xml': {'name': 'Id'}},
        'access_policy': {'key': 'AccessPolicy', 'type': 'AccessPolicy', 'xml': {'name': 'AccessPolicy'}},
    }
    _xml_map = {
        'name': 'SignedIdentifier'
    }

    def __init__(self, *, id: str, access_policy, **kwargs) -> None:
        super(SignedIdentifier, self).__init__(**kwargs)
        self.id = id
        self.access_policy = access_policy


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
        'type': {'key': 'type', 'type': 'str', 'xml': {'name': 'type', 'attr': True}},
        'title': {'key': 'title', 'type': 'str', 'xml': {'name': 'title'}},
        'items': {'key': 'items', 'type': '[str]', 'xml': {'name': 'items', 'itemsName': 'item'}},
    }
    _xml_map = {
        'name': 'slide'
    }

    def __init__(self, *, type: str=None, title: str=None, items=None, **kwargs) -> None:
        super(Slide, self).__init__(**kwargs)
        self.type = type
        self.title = title
        self.items = items


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
        'title': {'key': 'title', 'type': 'str', 'xml': {'name': 'title', 'attr': True}},
        'date_property': {'key': 'date', 'type': 'str', 'xml': {'name': 'date', 'attr': True}},
        'author': {'key': 'author', 'type': 'str', 'xml': {'name': 'author', 'attr': True}},
        'slides': {'key': 'slides', 'type': '[Slide]', 'xml': {'name': 'slides', 'itemsName': 'slide'}},
    }
    _xml_map = {
        'name': 'slideshow'
    }

    def __init__(self, *, title: str=None, date_property: str=None, author: str=None, slides=None, **kwargs) -> None:
        super(Slideshow, self).__init__(**kwargs)
        self.title = title
        self.date_property = date_property
        self.author = author
        self.slides = slides


class StorageServiceProperties(Model):
    """Storage Service Properties.

    :param logging: Azure Analytics Logging settings
    :type logging: ~xmlservice.models.Logging
    :param hour_metrics: A summary of request statistics grouped by API in
     hourly aggregates for blobs
    :type hour_metrics: ~xmlservice.models.Metrics
    :param minute_metrics: a summary of request statistics grouped by API in
     minute aggregates for blobs
    :type minute_metrics: ~xmlservice.models.Metrics
    :param cors: The set of CORS rules.
    :type cors: list[~xmlservice.models.CorsRule]
    :param default_service_version: The default version to use for requests to
     the Blob service if an incoming request's version is not specified.
     Possible values include version 2008-10-27 and all more recent versions
    :type default_service_version: str
    :param delete_retention_policy: The Delete Retention Policy for the
     service
    :type delete_retention_policy: ~xmlservice.models.RetentionPolicy
    """

    _attribute_map = {
        'logging': {'key': 'Logging', 'type': 'Logging', 'xml': {'name': 'Logging'}},
        'hour_metrics': {'key': 'HourMetrics', 'type': 'Metrics', 'xml': {'name': 'HourMetrics'}},
        'minute_metrics': {'key': 'MinuteMetrics', 'type': 'Metrics', 'xml': {'name': 'MinuteMetrics'}},
        'cors': {'key': 'Cors', 'type': '[CorsRule]', 'xml': {'name': 'Cors', 'itemsName': 'CorsRule', 'wrapped': True}},
        'default_service_version': {'key': 'DefaultServiceVersion', 'type': 'str', 'xml': {'name': 'DefaultServiceVersion'}},
        'delete_retention_policy': {'key': 'DeleteRetentionPolicy', 'type': 'RetentionPolicy', 'xml': {'name': 'DeleteRetentionPolicy'}},
    }
    _xml_map = {
    }

    def __init__(self, *, logging=None, hour_metrics=None, minute_metrics=None, cors=None, default_service_version: str=None, delete_retention_policy=None, **kwargs) -> None:
        super(StorageServiceProperties, self).__init__(**kwargs)
        self.logging = logging
        self.hour_metrics = hour_metrics
        self.minute_metrics = minute_metrics
        self.cors = cors
        self.default_service_version = default_service_version
        self.delete_retention_policy = delete_retention_policy
