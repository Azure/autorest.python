# coding=utf-8
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
import copy
from typing import List
import importlib
import urllib.parse
from ._auto_rest_paging_test_service import AutoRestPagingTestService as AutoRestPagingTestServiceGenerated
from azure.core.pipeline.policies import SansIOHTTPPolicy

class RemoveDuplicateParamsPolicy(SansIOHTTPPolicy):
    def __init__(self, duplicate_param_names):
        # type: (List[str]) -> None
        self.duplicate_param_names = duplicate_param_names

    def on_request(self, request):
        parsed_url = urllib.parse.urlparse(request.http_request.url)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        updated_query_params = copy.copy(query_params)
        for query in query_params:
            if query in self.duplicate_param_names and (isinstance(query_params[query], list) and len(query_params[query]) > 1):
                updated_query_params[query] = [query_params[query][-1]]
        # service returned will be later in the url because of how we format
        request.http_request.url = request.http_request.url.replace(parsed_url.query, "") + urllib.parse.urlencode(updated_query_params, doseq=True)
        return super().on_request(request)

class AutoRestPagingTestService(AutoRestPagingTestServiceGenerated):
    def __init__(self, *args, **kwargs):
        per_call_policies = kwargs.pop("per_call_policies", [])
        params_policy = RemoveDuplicateParamsPolicy(duplicate_param_names=["$filter", "$skiptoken"])
        try:
            per_call_policies.append(params_policy)
        except AttributeError:
            per_call_policies = [per_call_policies, params_policy]
        super().__init__(*args, per_call_policies=per_call_policies, **kwargs)

# This file is used for handwritten extensions to the generated code. Example:
# https://github.com/Azure/azure-sdk-for-python/blob/main/doc/dev/customize_code/how-to-patch-sdk-code.md
def patch_sdk():
    curr_package = importlib.import_module("paging")
    curr_package.AutoRestPagingTestService = AutoRestPagingTestService
