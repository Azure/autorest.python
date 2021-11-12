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

@pytest.mark.skipif(sys.version_info < (3, 0), reason="This is python3 only")
def test_models():
    from bodycomplexpython3only.models import Error
    from bodycomplexpython3only.models._models_py3 import Error as ErrorPy3
    assert Error == ErrorPy3
    ErrorPy3()

    # shouldn't have a py2 model
    with pytest.raises(ImportError):
        from bodycomplexpython3only.models._models import Error

@pytest.mark.skipif(sys.version_info < (3, 0), reason="This is python3 only")
def test_operation_groups():
    from bodycomplexpython3only.operations import ArrayOperations
    from bodycomplexpython3only.operations._array_operations import ArrayOperations as ArrayOperationsPy3
    assert ArrayOperations == ArrayOperationsPy3
    ArrayOperationsPy3(client=None, config=None, serializer=None, deserializer=None)
