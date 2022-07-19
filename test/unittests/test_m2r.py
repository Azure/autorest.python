# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from autorest.m2r import M2R


_MD_LINK = "[inline link](https://github.com/Azure/autorest.python)"
_RST_LINK = "`inline link <https://github.com/Azure/autorest.python>`_"

def test_m2r_replace_basic():
    yaml_data = {
        'description': _MD_LINK,
        'summary': _MD_LINK,
        'list': [
            'unrelated',
            {
                'description': _MD_LINK,
                'summary': _MD_LINK,
            }
        ],
        'obj': {
            'description': _MD_LINK,
            'summary': _MD_LINK,
        }
    }

    m2r = M2R(output_folder="")
    m2r.update_yaml(yaml_data)

    assert yaml_data['description'] == _RST_LINK
    assert yaml_data['summary'] == _RST_LINK
    assert yaml_data['list'][1]['description'] == _RST_LINK == _RST_LINK
    assert yaml_data['list'][1]['summary'] == _RST_LINK == _RST_LINK
    assert yaml_data['obj']['description'] == _RST_LINK
    assert yaml_data['obj']['summary'] == _RST_LINK

def test_m2r_cycle():
    yaml_data = {
        'description': _MD_LINK,
        'summary': _MD_LINK,
    }
    yaml_data['obj'] = yaml_data
    assert yaml_data['obj']['obj'] is yaml_data

    m2r = M2R(output_folder="")
    m2r.update_yaml(yaml_data)

    assert yaml_data['description'] == _RST_LINK
    assert yaml_data['summary'] == _RST_LINK

def test_inline_html():
    m2r = M2R(output_folder="")
    assert m2r.convert_to_rst("Dictionary of <FlattenedProduct>.") == "Dictionary of :code:`<FlattenedProduct>`."
