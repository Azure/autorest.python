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
import unittest
import isodate
import subprocess
import sys
import datetime
import os
import platform
from os.path import dirname, pardir, join, realpath
import warnings

from report import AutoRestReportService


class TestAcceptance(object):

    def test_ensure_coverage(self):
        client = AutoRestReportService(base_url="http://localhost:3000")
        report = client.get_report(platform.python_version())
        optional_report = client.get_optional_report(platform.python_version())

        # Add tests that wont be supported due to the nature of Python here
        not_supported = {}

        # Please add missing features or failing tests here
        missing_features_or_bugs = {
            'FileStreamVeryLarge' : 1,
            'ConstantsInBody': 1,  # https://github.com/Azure/autorest.modelerfour/issues/83
            'CustomBaseUriMoreOptions': 1, # https://github.com/Azure/autorest.testserver/issues/97
            'putModelFlattenArray': 1, # https://github.com/Azure/autorest.modelerfour/issues/14
            'putModelFlattenDictionary': 1, # https://github.com/Azure/autorest.modelerfour/issues/14
            'putModelFlattenResourceCollection': 1, # https://github.com/Azure/autorest.modelerfour/issues/14
            'putModelFlattenCustomBase': 1, # https://github.com/Azure/autorest.modelerfour/issues/14
            'postModelFlattenCustomParameter': 1, # https://github.com/Azure/autorest.modelerfour/issues/14
            'putModelFlattenCustomGroupedParameter': 1, # https://github.com/Azure/autorest.modelerfour/issues/10
        }
        for name in report:
            if "XML" in name:
                missing_features_or_bugs[name] = 1; # Skip all XML until XML PR is merged

        print("Coverage:")
        self._print_report(report, not_supported, missing_features_or_bugs)
        print("Optional coverage:")
        self._print_report(optional_report)


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

if __name__ == '__main__':
    unittest.main()
