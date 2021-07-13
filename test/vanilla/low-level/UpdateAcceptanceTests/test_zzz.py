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
import platform
import warnings

from reportlowlevel import AutoRestReportService, rest


class TestAcceptance(object):

    def test_ensure_coverage(self):
        client = AutoRestReportService(base_url="http://localhost:3000")
        request = rest.build_get_report_request(qualifier=platform.python_version())
        report = client.send_request(request).json()

        # we only care about coverage for the following tests in the update section of the tests
        coverage_we_care_about = ['LLCRequiredToOptional']

        print("Coverage:")
        self._print_report(report, coverage_we_care_about)

    def _print_report(self, report, coverage_we_care_about):

        failed = [k for k, v in report.items() if v == 0 and k in coverage_we_care_about]
        for s in failed:
            print("FAILED TO EXECUTE {0}".format(s))

        total_tests = len(coverage_we_care_about)
        warnings.warn ("The test coverage is {0}/{1}.".format(total_tests - len(failed), total_tests))

        assert 0 == len(failed)
