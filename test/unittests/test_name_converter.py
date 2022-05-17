# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from autorest.namer.helpers import pad_reserved_words
from autorest.namer.python_mappings import PadType

def test_escaped_reserved_words():
    expected_conversion_model = {
        "Self": "Self",
        "And": "AndModel"
    }
    for name in expected_conversion_model:
        assert pad_reserved_words(name, pad_type=PadType.MODEL) == expected_conversion_model[name]


    expected_conversion_method = {
        "self": "self",
        "and": "and_method",
        "content_type": "content_type"
    }
    for name in expected_conversion_method:
        assert pad_reserved_words(name, pad_type=PadType.METHOD) == expected_conversion_method[name]

    expected_conversion_parameter = {
        "content_type": "content_type_parameter",
        "request_id": "request_id_parameter",
        "elif": "elif_parameter",
        "self": "self_parameter",
        "continuation_token": "continuation_token_parameter"
    }
    for name in expected_conversion_parameter:
        assert pad_reserved_words(name, pad_type=PadType.PARAMETER) == expected_conversion_parameter[name]

    expected_conversion_enum = {
        "self": "self",
        "mro": "mro_enum",
        "continuation_token": "continuation_token"
    }
    for name in expected_conversion_enum:
        assert pad_reserved_words(name, pad_type=PadType.ENUM) == expected_conversion_enum[name]