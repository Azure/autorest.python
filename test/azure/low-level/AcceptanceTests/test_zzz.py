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
import sys
import datetime
import os
import platform
import warnings

from azurereportlowlevel import AutoRestReportServiceForAzure, rest


class TestAcceptance(object):

    def test_ensure_coverage(self):
        client = AutoRestReportServiceForAzure(endpoint="http://localhost:3000")
        request = rest.build_get_report_request(qualifier=platform.python_version())
        report = client.send_request(request).json()

        # Add tests that wont be supported due to the nature of Python here
        not_supported = {
            "LROConstantParameterizedPost": 1,  # involves formatting base url
            "LROConstantParameterizedGet": 1,  # involves formatting base url
            "CustomHeaderPutAsyncSucceded": 1,  # waiting for https://github.com/Azure/azure-sdk-for-python/issues/17757 to be released
            "CustomHeaderPostAsyncSucceded": 1,  # waiting for https://github.com/Azure/azure-sdk-for-python/issues/17757 to be released
            "CustomHeaderPutSucceeded": 1,  # waiting for https://github.com/Azure/azure-sdk-for-python/issues/17757 to be released
            "CustomHeaderPostSucceeded": 1,  # waiting for https://github.com/Azure/azure-sdk-for-python/issues/17757 to be released
            "PagingReturnModelWithXMSClientName": 1,  # not relevant, we don't generate return models in LLC
            "PagingCustomUrlPartialNextLink": 1,  # involves formatting base url
            "PagingCustomUrlPartialOperationNextLink": 1,  # involves formatting base url
            "LROParameterizedEndpoint": 1,  # involves formatting base url
            "LROErrorPutAsyncInvalidJsonPolling": 1, # The reason this fails is bc the convenience layer fails in deserializing the response headers. LLC doesn't do that, so skipping
            "LROErrorPutAsyncInvalidHeader": 1,  # The reason this fails is bc the convenience layer fails in deserializing the response headers. LLC doesn't do that, so skipping
            "LROErrorDelete202RetryInvalidHeader": 1,  # The reason this fails is bc the convenience layer fails in deserializing the response headers. LLC doesn't do that, so skipping
            "LROErrorDeleteAsyncInvalidHeader": 1,  # The reason this fails is bc the convenience layer fails in deserializing the response headers. LLC doesn't do that, so skipping
            "LROErrorDeleteAsyncInvalidJsonPolling": 1, # The reason this fails is bc the convenience layer fails in deserializing the retry-after header /bar as an int. LLC doesn't do that, so skipping
            "LROErrorPost202RetryInvalidHeader": 1,  # The reason this fails is bc the convenience layer fails in deserializing the retry-after header /bar as an int. LLC doesn't do that, so skipping
            "LROErrorPostAsyncInvalidHeader": 1,  # The reason this fails is bc the convenience layer fails in deserializing the retry-after header /bar as an int. LLC doesn't do that, so skipping
            "LROErrorPostAsyncInvalidJsonPolling": 1,   # The reason this fails is bc the convenience layer fails in deserializing. LLC doesn't do that, so skipping
            "LROPatchInlineCompleteIgnoreHeaders": 1,
        }

        # Please add missing features or failing tests here
        missing_features_or_bugs = {
            "PagingMultipleLRO": 1,  # can't quite figure it out, skipping for now bc low pri
        }

        print("Coverage:")
        self._print_report(report, not_supported, missing_features_or_bugs)


    def _print_report(self, report, not_supported=None, missing_features_or_bugs=None):
        if not_supported:
            report.update(not_supported)
            for s in not_supported.keys():
                print("IGNORING {0}".format(s))

        if missing_features_or_bugs:
            report.update(missing_features_or_bugs)
            for s in missing_features_or_bugs.keys():
                print("PENDING {0}".format(s))

        failed = [k for k, v in report.items() if v == 0]
        for s in failed:
            print("FAILED TO EXECUTE {0}".format(s))

        total_tests = len(report)
        warnings.warn ("The test coverage is {0}/{1}.".format(total_tests - len(failed), total_tests))

        assert 0 == len(failed)
