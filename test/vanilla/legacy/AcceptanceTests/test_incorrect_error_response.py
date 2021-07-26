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
import pytest
from azure.core.exceptions import HttpResponseError
from incorrecterrorresponse import IncorrectReturnedErrorModel

def test_swallow_deserialization_error_for_error_model():
    client = IncorrectReturnedErrorModel(base_url="http://localhost:3000")
    with pytest.raises(HttpResponseError):
        client.get_incorrect_error_from_server()

def test_operation_groups():
    from incorrecterrorresponse.operations import IncorrectReturnedErrorModelOperationsMixin

    if sys.version_info >= (3, 5):
        from incorrecterrorresponse.operations._incorrect_returned_error_model_operations_py3 import IncorrectReturnedErrorModelOperationsMixin as IncorrectReturnedErrorModelOperationsMixinPy3
        assert IncorrectReturnedErrorModelOperationsMixin == IncorrectReturnedErrorModelOperationsMixinPy3
    else:
        from incorrecterrorresponse.operations._incorrect_returned_error_model_operations import IncorrectReturnedErrorModelOperationsMixin as IncorrectReturnedErrorModelOperationsMixinPy2
        assert IncorrectReturnedErrorModelOperationsMixin == IncorrectReturnedErrorModelOperationsMixinPy2