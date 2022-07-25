# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from autorest.jsonrpc.localapi import LocalAutorestAPI

def test_get_bool():
    api = LocalAutorestAPI()

    api.values = {
        'bool': True,
        'boolfalse': False,
        'strtrue': 'true',
        'strfalse': 'boo',
        'inttrue': 1,
        'intfalse': 42,
        'dashdash': {}
    }

    assert api.get_boolean_value('nothere') is None
    assert api.get_boolean_value('nothere', True) is True

    assert api.get_boolean_value('bool') is True
    assert api.get_boolean_value('bool', False) is True

    assert api.get_boolean_value('boolfalse') is False
    assert api.get_boolean_value('boolfalse', True) is False

    assert api.get_boolean_value('strtrue') is True
    assert api.get_boolean_value('strtrue', False) is True

    assert api.get_boolean_value('strfalse') is False
    assert api.get_boolean_value('strfalse', True) is False

    assert api.get_boolean_value('inttrue') is True
    assert api.get_boolean_value('inttrue', False) is True

    assert api.get_boolean_value('intfalse') is False
    assert api.get_boolean_value('intfalse', True) is False

    assert api.get_boolean_value('dashdash') is True
    assert api.get_boolean_value('dashdash', False) is True
