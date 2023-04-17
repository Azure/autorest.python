# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from resiliency.servicedriven1 import ResiliencyServiceDrivenClient as V1Client
from resiliency.servicedriven2 import ResiliencyServiceDrivenClient as V2Client

def get_v1_client(service_deployment_version: str, api_version: str = "v1") -> V1Client:
    return V1Client(service_deployment_version=service_deployment_version, api_version=api_version)

def get_v2_client(service_deployment_version: str, api_version: str = "v2") -> V2Client:
    return V2Client(service_deployment_version=service_deployment_version, api_version=api_version)

def test_add_optional_param_from_none():
    # old client to old service with api version v1
    with V1Client(service_deployment_version="v1") as client:
        client.from_none()

    # old client to new service with api version v1
    with V1Client(service_deployment_version="v2") as client:
        client.from_none()

    # new client to new service with api version v1
    with V2Client(service_deployment_version="v2", api_version="v1") as client:
        client.from_none()

    # new client to new service with api version v2
    with V2Client(service_deployment_version="v2") as client:
        client.from_none(new_parameter="new")

def test_add_optional_param_from_one_required():
    # old client to old service with api version v1
    with V1Client(service_deployment_version="v1") as client:
        client.from_one_required(parameter="required")

    # old client to new service with api version v1
    with V1Client(service_deployment_version="v2") as client:
        client.from_one_required(parameter="required")

    # new client to new service with api version v1
    with V2Client(service_deployment_version="v2", api_version="v1") as client:
        client.from_one_required(parameter="required")

    # new client to new service with api version v2
    with V2Client(service_deployment_version="v2") as client:
        client.from_one_required(parameter="required", new_parameter="new")

def test_add_optional_param_from_one_optional():
    # old client to old service with api version v1
    with V1Client(service_deployment_version="v1") as client:
        client.from_one_optional(parameter="optional")

    # old client to new service with api version v1
    with V1Client(service_deployment_version="v2") as client:
        client.from_one_optional(parameter="optional")

    # new client to new service with api version v1
    with V2Client(service_deployment_version="v2", api_version="v1") as client:
        client.from_one_optional(parameter="optional")

    # new client to new service with api version v2
    with V2Client(service_deployment_version="v2") as client:
        client.from_one_optional(parameter="optional", new_parameter="new")
