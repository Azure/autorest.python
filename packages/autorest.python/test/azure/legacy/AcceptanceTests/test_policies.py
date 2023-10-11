# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
from typing import List
from head import AutoRestHeadTestService
from bodyduration import AutoRestDurationTestService
from azure.core import PipelineClient
from azure.mgmt.core import ARMPipelineClient
import pytest

def get_policy_class_name(client) -> List[str]:
    return [p._policy.__class__.__name__ if hasattr(p, "_policy") else p.__class__.__name__ for p in client._client._pipeline._impl_policies]

@pytest.mark.parametrize(
    "sdk_client,pipeline_client", [
        (AutoRestHeadTestService, ARMPipelineClient),
        (AutoRestDurationTestService, PipelineClient)
])
def test_policies(sdk_client, pipeline_client):
    client = sdk_client(credential="")
    policies_built_in_client = get_policy_class_name(client)

    client._config.request_id_policy = None
    client._client = pipeline_client(base_url="http://localhost:3000", config=client._config)
    policies_built_in_core = get_policy_class_name(client)

    assert policies_built_in_client == policies_built_in_core
