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
import pytest
from bodycomplex import models

"""
If users pass in a string to these fields, we want to trust them and not do any silent failing
"""

@pytest.mark.parametrize(
    "model_name,field_name,serialized_field_name", [
        ("DatetimeWrapper", "field", "field"),
        ("DurationWrapper", "field", "field"),
        ("Datetimerfc1123Wrapper", "field", "field"),
        ("DateWrapper", "field", "field"),
        ("IntWrapper", "field1", "field1"),
        ("LongWrapper", "field1", "field1"),
        ("FloatWrapper", "field1", "field1"),
        ("ByteWrapper", "field", "field"),
        ("BooleanWrapper", "field_true", "field_true"),
        ("DictionaryWrapper", "default_program", "defaultProgram"),
        ("ArrayWrapper", "array", "array"),
    ]
)
def test(model_name, field_name, serialized_field_name):
    field = "should be me"
    model = getattr(models, model_name)(**{field_name: field})
    assert model.serialize() == {serialized_field_name: field}
