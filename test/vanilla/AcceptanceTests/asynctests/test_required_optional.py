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
import subprocess
import sys
import isodate
import os
from datetime import date, datetime, timedelta
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "RequiredOptional"))

from msrest.exceptions import DeserializationError, SerializationError, ValidationError

from requiredoptional.aio import AutoRestRequiredOptionalTestService
from requiredoptional.models import StringWrapper, ArrayWrapper, ClassWrapper

import pytest


class TestRequiredOptional(object):

    @pytest.mark.asyncio
    async def test_required_optional(self):

        client = AutoRestRequiredOptionalTestService(
            required_global_path="required_path",
            required_global_query="required_query",
            base_url="http://localhost:3000")

        await client.implicit.put_optional_query(None)
        await client.implicit.put_optional_body(None)
        await client.implicit.put_optional_header(None)

        await client.implicit.get_optional_global_query(custom_headers=None)

        await client.explicit.post_optional_integer_parameter(None)
        await client.explicit.post_optional_integer_property(None)
        await client.explicit.post_optional_integer_header(None)

        await client.explicit.post_optional_string_parameter(None)
        await client.explicit.post_optional_string_property(None)
        await client.explicit.post_optional_string_header(None)

        await client.explicit.post_optional_class_parameter(None)
        await client.explicit.post_optional_class_property(None)

        await client.explicit.post_optional_array_parameter(None)
        await client.explicit.post_optional_array_property(None)
        await client.explicit.post_optional_array_header(None)

    @pytest.mark.asyncio
    async def test_required_optional_negative(self):

        client = AutoRestRequiredOptionalTestService(
            required_global_path=None,
            equired_global_query=None,
            base_url="http://localhost:3000")

        with pytest.raises(ValidationError):
            await client.implicit.get_required_path(None)

        with pytest.raises(ValidationError):
            await client.explicit.post_required_string_header(None)

        with pytest.raises(ValidationError):
            await client.explicit.post_required_string_parameter(None)

        with pytest.raises(ValidationError):
            await client.explicit.post_required_string_property(None)

        with pytest.raises(ValidationError):
            await client.explicit.post_required_array_header(None)

        with pytest.raises(ValidationError):
            await client.explicit.post_required_array_parameter(None)

        with pytest.raises(ValidationError):
            await client.explicit.post_required_array_property(None)

        with pytest.raises(ValidationError):
            await client.explicit.post_required_class_parameter(None)

        with pytest.raises(ValidationError):
            await client.explicit.post_required_class_property(None)

        with pytest.raises(ValidationError):
            await client.implicit.get_required_global_path()

        with pytest.raises(ValidationError):
            await client.implicit.get_required_global_query()


if __name__ == '__main__':


    unittest.main()
