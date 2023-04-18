# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Mapping, Optional, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field
from azure.core.exceptions import HttpResponseError

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class JobData(_model_base.Model):
    """Data of the job.

    All required parameters must be populated in order to send to Azure.

    :ivar comment: Comment. Required.
    :vartype comment: str
    """

    comment: str = rest_field()
    """Comment. Required."""

    @overload
    def __init__(
        self,
        *,
        comment: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class JobPollResult(_model_base.Model):
    """Result of the poll.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar operation_id: Operation identifier. Required.
    :vartype operation_id: str
    :ivar status: The status of the processing job. Required. Known values are: "InProgress",
     "Succeeded", "Failed", and "Canceled".
    :vartype status: str or ~azure.lro.rpc.models.OperationState
    """

    operation_id: str = rest_field(name="operationId", readonly=True)
    """Operation identifier. Required."""
    status: Union[str, "_models.OperationState"] = rest_field(readonly=True)
    """The status of the processing job. Required. Known values are: \"InProgress\", \"Succeeded\",
     \"Failed\", and \"Canceled\"."""


class JobResult(_model_base.Model):
    """Result of the job.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar job_id: A processing job identifier. Required.
    :vartype job_id: str
    :ivar comment: Comment. Required.
    :vartype comment: str
    :ivar status: The status of the processing job. Required. Known values are: "InProgress",
     "Succeeded", "Failed", and "Canceled".
    :vartype status: str or ~azure.lro.rpc.models.OperationState
    :ivar errors: Error objects that describes the error when status is "Failed".
    :vartype errors: list[~azure.core.exceptions.HttpResponseError]
    :ivar results: The results. Required.
    :vartype results: list[str]
    """

    job_id: str = rest_field(name="jobId", readonly=True)
    """A processing job identifier. Required."""
    comment: str = rest_field(readonly=True)
    """Comment. Required."""
    status: Union[str, "_models.OperationState"] = rest_field(readonly=True)
    """The status of the processing job. Required. Known values are: \"InProgress\", \"Succeeded\",
     \"Failed\", and \"Canceled\"."""
    errors: Optional[List[HttpResponseError]] = rest_field(readonly=True)
    """Error objects that describes the error when status is \"Failed\"."""
    results: List[str] = rest_field(readonly=True)
    """The results. Required."""
