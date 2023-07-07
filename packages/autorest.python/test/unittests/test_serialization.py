# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#--------------------------------------------------------------------------

from decimal import Decimal
import sys
import json
import isodate
import logging
import pickle
from enum import Enum
from datetime import datetime, timedelta, date, time
import unittest

import xml.etree.ElementTree as ET

from requests import Response

from storage_models.serialization import Model, last_restapi_key_transformer, full_restapi_key_transformer, rest_key_extractor
from storage_models.serialization import Serializer, Deserializer
# from azure.core.exceptions import ValidationError
from azure.core.exceptions import SerializationError, DeserializationError
from azure.core.exceptions import SerializationError as AzureCoreSerializationError, DeserializationError as AzureCoreDeserializationError

import storage_models

import pytest

class Resource(Model):
    """Resource

    :param str id: Resource Id
    :param str name: Resource name
    :param str type: Resource type
    :param str location: Resource location
    :param dict tags: Resource tags
    """

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, location, id=None, name=None, type=None, tags=None, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.type = type
        self.location = location
        self.tags = tags


class GenericResource(Resource):
    """
    Resource information.

    :param str id: Resource Id
    :param str name: Resource name
    :param str type: Resource type
    :param str location: Resource location
    :param dict tags: Resource tags
    :param Plan plan: Gets or sets the plan of the resource.
    :param object properties: Gets or sets the resource properties.
    """

    _validation = {}

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'plan': {'key': 'plan', 'type': 'Plan'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(self, location, id=None, name=None, type=None, tags=None, plan=None, properties=None):
        super(GenericResource, self).__init__(location, id=id, name=name, type=type, tags=tags)
        self.plan = plan
        self.properties = properties

class TestModelDeserialization(unittest.TestCase):

    def setUp(self):
        self.d = Deserializer({'Resource':Resource, 'GenericResource':GenericResource})
        return super(TestModelDeserialization, self).setUp()

    def test_model_kwargs(self):

        class MyModel(Model):
            _validation = {
                'id': {'readonly': True},
                'name': {'required': True},
            }
            _attribute_map = {
                'id': {'key': 'id', 'type': 'str'},
                'name': {'key': 'name', 'type': 'str'},
                'location': {'key': 'location', 'type': 'str'},
            }
            def __init__(self, **kwargs):
                super(MyModel, self).__init__(**kwargs)
                self.id = None
                self.name = kwargs.get('name', None)
                self.location = kwargs.get('location', None)

        # validation = MyModel().validate()
        # self.assertEqual(str(validation[0]), "Parameter 'MyModel.name' can not be None.")

    @unittest.skipIf(sys.version_info < (3,4), "assertLogs not supported before 3.4")
    def test_model_kwargs_logs(self):

        class MyModel(Model):
            _validation = {
                'id': {'readonly': True},
                'name': {'required': True},
            }
            _attribute_map = {
                'id': {'key': 'id', 'type': 'str'},
                'name': {'key': 'name', 'type': 'str'},
                'location': {'key': 'location', 'type': 'str'},
            }
            def __init__(self, **kwargs):
                super(MyModel, self).__init__(**kwargs)
                self.id = None
                self.name = kwargs.get('name', None)
                self.location = kwargs.get('location', None)

        with self.assertLogs('storage_models.serialization', level='WARNING') as cm:
            MyModel(name="test", id="123") # Should log that id is readonly
        self.assertEqual(len(cm.output), 1)
        self.assertIn("attribute id", cm.output[0])
        self.assertIn("Readonly", cm.output[0])

        with self.assertLogs('storage_models.serialization', level='WARNING') as cm:
            MyModel(something="ioprez") # Should log that this is unknown
        self.assertEqual(len(cm.output), 1)
        self.assertIn("not a known attribute", cm.output[0])

    @unittest.skipIf(sys.version_info < (3,4), "assertLogs not supported before 3.4")
    def test_empty_enum_logs(self):
        class StatusType(str, Enum):
            success = "success"
            failed = "failed"

        d = Deserializer({"StatusType": StatusType})

        with self.assertRaises(AssertionError):
            with self.assertLogs('storage_models.serialization', level='WARNING') as cm:
                result = d(StatusType, "failed")
        self.assertEqual(len(cm.output), 0)
        self.assertEqual(result, StatusType.failed)

        with self.assertRaises(AssertionError):
            with self.assertLogs('storage_models.serialization', level='WARNING') as cm:
                result = d(StatusType, None)
        self.assertEqual(len(cm.output), 0)
        self.assertEqual(result, None)

        with self.assertLogs('storage_models.serialization', level='WARNING') as cm:
            result = d(StatusType, "aborted")
        self.assertEqual(result, 'aborted')
        self.assertEqual(len(cm.output), 1)
        self.assertTrue("Deserializer is not able to find aborted as valid enum" in cm.output[0])

    def test_response(self):

        data = {
          "properties": {
            "platformUpdateDomainCount": 5,
            "platformFaultDomainCount": 3,
            "virtualMachines": []
          },
          "id": "/subscriptions/abc-def-ghi-jklmnop/resourceGroups/test_mgmt_resource_test_resourcesea/providers/Microsoft.Compute/availabilitySets/pytest",
          "name": "pytest",
          "type": "Microsoft.Compute/availabilitySets",
          "location": "westus"
        }

        model = self.d('GenericResource', json.dumps(data), 'application/json')
        self.assertEqual(model.properties['platformFaultDomainCount'], 3)
        self.assertEqual(model.location, 'westus')

class TestRuntimeSerialized(unittest.TestCase):

    class TestObj(Model):

        _attribute_map = {
            'attr_a': {'key':'id', 'type':'str'},
            'attr_b': {'key':'AttrB', 'type':'int'},
            'attr_c': {'key':'Key_C', 'type': 'bool'},
            'attr_d': {'key':'AttrD', 'type':'[int]'},
            'attr_e': {'key':'AttrE', 'type': '{float}'},
            'attr_f': {'key':'AttrF', 'type': 'duration'},
            'attr_g': {'key':'properties.AttrG', 'type':'str'},
        }

        def __init__(self,
                attr_a=None,
                attr_b=None,
                attr_c=None,
                attr_d=None,
                attr_e=None,
                attr_f=None,
                attr_g=None):

            self.attr_a = attr_a
            self.attr_b = attr_b
            self.attr_c = attr_c
            self.attr_d = attr_d
            self.attr_e = attr_e
            self.attr_f = attr_f
            self.attr_g = attr_g

        def __str__(self):
            return "Test_Object"

    def setUp(self):
        self.s = Serializer({'TestObj': self.TestObj})
        return super(TestRuntimeSerialized, self).setUp()

    def test_validation_type(self):
        # https://github.com/Azure/msrest-for-python/issues/85
        s = Serializer()

        s.query("filter", 186, "int", maximum=666)
        s.query("filter", "186", "int", maximum=666)

        class TestValidationObj(Model):

            _attribute_map = {
                'attr_a': {'key':'id', 'type':'int'},
            }
            _validation = {
                'attr_a': {'maximum': 4294967295, 'minimum': 1},
            }


        # test_obj = TestValidationObj()
        # test_obj.attr_a = 186
        # errors_found = test_obj.validate()
        # assert not errors_found

        # test_obj.attr_a = '186'
        # errors_found = test_obj.validate()
        # assert not errors_found

    def test_validation_flag(self):
        s = Serializer()
        s.client_side_validation = True

        # with self.assertRaises(ValidationError):
        #     s.query("filter", "", "str", min_length=666)
        # with self.assertRaises(ValidationError):
        #     s.url("filter", "", "str", min_length=666)
        # with self.assertRaises(ValidationError):
        #     s.header("filter", "", "str", min_length=666)

        test_obj = self.TestObj()
        self.TestObj._validation = {
            'attr_b': {'required': True},
        }
        test_obj.attr_b = None

        # with self.assertRaises(ValidationError):
        #     self.s.body(test_obj, 'TestObj')

        s.client_side_validation = False
        s.query("filter", "", "str", min_length=666)
        s.url("filter", "", "str", min_length=666)
        s.header("filter", "", "str", min_length=666)
        s.body(test_obj, 'TestObj')

    def test_serialize_query(self):
        s = Serializer()

        assert s.query("filter", "boo", "str") == "boo"
        assert s.query("filter", "boo,bar", "str", skip_quote=True) == "boo,bar"
        assert s.query("filter", 12, "int") == "12"

        assert s.query("filter", [1, 2, 3], "[int]", div=",") == "1,2,3"

        assert s.query("filter", ['a', 'b', 'c'], "[str]", div=",") == "a,b,c"
        assert s.query("filter", ['a', None, 'c'], "[str]", div=",") == "a,,c"
        assert s.query("filter", [',', ',', ','], "[str]", div=",") == "%2C,%2C,%2C"
        assert s.query("filter", [',', ',', ','], "[str]", div="|", skip_quote=True) == ",|,|,"

    def test_serialize_custom_model(self):

        class CustomSample(Model):
            _validation = {
                    'a': {'required': True},
            }

            _attribute_map = {
                'a': {'key': 'a', 'type': 'str'},
            }

            def __init__(self, a):
                self.a = a

        s = Serializer()
        model = CustomSample("helloworld")
        serialized = s._serialize(model)

        assert serialized is not None
        assert isinstance(serialized, dict)
        assert serialized['a'] == "helloworld"

    def test_serialize_direct_model(self):
        testobj = self.TestObj()
        testobj.attr_a = "myid"
        testobj.attr_b = 42
        testobj.attr_c = True
        testobj.attr_d = [1,2,3]
        testobj.attr_e = {"pi": 3.14}
        testobj.attr_f = timedelta(1)
        testobj.attr_g = "RecursiveObject"

        serialized = testobj.serialize()
        expected = {
            "id": "myid",
            "AttrB": 42,
            "Key_C": True,
            "AttrD": [1,2,3],
            "AttrE": {"pi": 3.14},
            "AttrF": "P1D",
            "properties": {
                "AttrG": "RecursiveObject"
            }
        }
        self.assertDictEqual(expected, serialized)

        jsonable = json.dumps(testobj.as_dict())
        expected = {
            "attr_a": "myid",
            "attr_b": 42,
            "attr_c": True,
            "attr_d": [1,2,3],
            "attr_e": {"pi": 3.14},
            "attr_f": "P1D",
            "attr_g": "RecursiveObject"
        }
        self.assertDictEqual(expected, json.loads(jsonable))

        jsonable = json.dumps(testobj.as_dict(key_transformer=last_restapi_key_transformer))
        expected = {
            "id": "myid",
            "AttrB": 42,
            "Key_C": True,
            "AttrD": [1,2,3],
            "AttrE": {"pi": 3.14},
            "AttrF": "P1D",
            "AttrG": "RecursiveObject"
        }
        self.assertDictEqual(expected, json.loads(jsonable))

        jsonable = json.dumps(testobj.as_dict(key_transformer=lambda x,y,z: (x+"XYZ", z)))
        expected = {
            "attr_aXYZ": "myid",
            "attr_bXYZ": 42,
            "attr_cXYZ": True,
            "attr_dXYZ": [1,2,3],
            "attr_eXYZ": {"pi": 3.14},
            "attr_fXYZ": "P1D",
            "attr_gXYZ": "RecursiveObject"
        }
        self.assertDictEqual(expected, json.loads(jsonable))

        def value_override(attr, attr_desc, value):
            key, value = last_restapi_key_transformer(attr, attr_desc, value)
            if key == "AttrB":
                value += 1
            return key, value

        jsonable = json.dumps(testobj.as_dict(key_transformer=value_override))
        expected = {
            "id": "myid",
            "AttrB": 43,
            "Key_C": True,
            "AttrD": [1,2,3],
            "AttrE": {"pi": 3.14},
            "AttrF": "P1D",
            "AttrG": "RecursiveObject"
        }
        self.assertDictEqual(expected, json.loads(jsonable))


    # def test_validate(self):
    #     # Assert not necessary, should not raise exception
    #     self.s.validate("simplestring", "StringForLog", pattern="^[a-z]+$")
    #     self.s.validate(u"UTF8ééééé", "StringForLog", pattern=r"^[\w]+$")

    def test_model_validate(self):

        class TestObj(Model):

            _validation = {
                'name': {'min_length': 3},
                'display_names': {'min_items': 2},
            }
            _attribute_map = {
                'name': {'key':'name', 'type':'str'},
                'rec_list': {'key':'rec_list', 'type':'[[TestObj]]'},
                'rec_dict': {'key':'rec_dict', 'type':'{{TestObj}}'},
                'display_names': {'key': 'display_names', 'type': '[str]'},
                'obj': {'key':'obj', 'type':'TestObj'},
            }

            def __init__(self, name):
                self.name = name
                self.rec_list = None
                self.rec_dict = None
                self.display_names = None
                self.obj = None

        obj = TestObj("ab")
        obj.rec_list = [[TestObj("bc")]]
        obj.rec_dict = {"key": {"key": TestObj("bc")}}
        obj.display_names = ["ab"]
        obj.obj = TestObj("ab")

        # broken_rules = obj.validate()
        # self.assertEqual(5, len(broken_rules))
        # str_broken_rules = [str(v) for v in broken_rules]
        # self.assertIn(
        #     "Parameter 'TestObj.name' must have length greater than 3.",
        #     str_broken_rules
        # )
        # self.assertIn(
        #     "Parameter 'TestObj.display_names' must contain at least 2 items.",
        #     str_broken_rules
        # )

    def test_obj_serialize_none(self):
        """Test that serialize None in object is still None.
        """
        obj = self.s.serialize_object({'test': None})
        self.assertIsNone(obj['test'])

    def test_obj_with_malformed_map(self):
        """
        Test serializing an object with a malformed attribute_map.
        """
        test_obj = type("BadTestObj", (Model,), {"_attribute_map":None})

        with self.assertRaises(SerializationError):
            self.s._serialize(test_obj)

        test_obj._attribute_map = {"attr":"val"}

        with self.assertRaises(SerializationError):
            self.s._serialize(test_obj)

        test_obj._attribute_map = {"attr":{"val":1}}

        with self.assertRaises(SerializationError):
            self.s._serialize(test_obj)

    def test_obj_with_mismatched_map(self):
        """
        Test serializing an object with mismatching attributes and map.
        """
        test_obj = type("BadTestObj", (Model,), {"_attribute_map":None})
        test_obj._attribute_map = {"abc":{"key":"ABC", "type":"str"}}

        with self.assertRaises(SerializationError):
            self.s._serialize(test_obj)

    def test_attr_enum(self):
        """
        Test serializing with Enum.
        """

        test_obj = type("TestEnumObj", (Model,), {"_attribute_map":None})
        test_obj._attribute_map = {
            "abc":{"key":"ABC", "type":"TestEnum"}
        }
        class TestEnum(Enum):
            val = "Value"

        t = test_obj()
        t.abc = TestEnum.val

        serialized = self.s._serialize(t)
        expected = {
            "ABC": "Value"
        }

        self.assertEqual(expected, serialized)

        class TestEnum2(Enum):
            val2 = "Value2"
        t.abc = TestEnum2.val2

        serializer = Serializer({
            'TestEnum': TestEnum,
            'TestEnum2': TestEnum2
        })
        with self.assertRaises(SerializationError):
            serializer._serialize(t)

        serializer = Serializer({
            'TestEnumObj': test_obj,
            'TestEnum': TestEnum
        })
        serialized = serializer.body({
            'abc': TestEnum.val
        }, 'TestEnumObj')
        expected = {
            'ABC': 'Value'
        }
        self.assertEqual(expected, serialized)

        # model-as-string=True
        test_obj._attribute_map = {
            "abc":{"key":"ABC", "type":"str"}
        }
        serialized = serializer.body({
            'abc': TestEnum.val
        }, 'TestEnumObj')
        expected = {
            'ABC': 'Value'
        }
        self.assertEqual(expected, serialized)


    def test_attr_none(self):
        """
        Test serializing an object with None attributes.
        """
        test_obj = self.TestObj()
        message = self.s._serialize(test_obj)

        self.assertIsInstance(message, dict)
        self.assertFalse('id' in message)

    def test_attr_int(self):
        """
        Test serializing an object with Int attributes.
        """
        test_obj = self.TestObj()
        self.TestObj._validation = {
            'attr_b': {'required': True},
        }
        test_obj.attr_b = None

        # with self.assertRaises(ValidationError):
        #     self.s.body(test_obj, 'TestObj')

        # validation_errors = test_obj.validate()
        # self.assertEqual(len(validation_errors), 1)

        test_obj.attr_b = 25

        message = self.s._serialize(test_obj)
        self.assertEqual(message['AttrB'], int(test_obj.attr_b))

        test_obj.attr_b = "34534"

        message = self.s._serialize(test_obj)
        self.assertEqual(message['AttrB'], int(test_obj.attr_b))

        test_obj.attr_b = "NotANumber"

        with self.assertRaises(SerializationError):
            self.s._serialize(test_obj)

        self.TestObj._validation = {}

    def test_attr_str(self):
        """
        Test serializing an object with Str attributes.
        """
        test_obj = self.TestObj()
        self.TestObj._validation = {
            'attr_a': {'required': True},
        }
        test_obj.attr_a = None

        # with self.assertRaises(ValidationError):
        #     self.s.body(test_obj, 'TestObj')

        # validation_errors = test_obj.validate()
        # self.assertEqual(len(validation_errors), 1)

        self.TestObj._validation = {}
        test_obj.attr_a = "TestString"

        message = self.s._serialize(test_obj)
        self.assertEqual(message['id'], str(test_obj.attr_a))

        test_obj.attr_a = 1234

        message = self.s._serialize(test_obj)
        self.assertEqual(message['id'], str(test_obj.attr_a))

        test_obj.attr_a = list()

        message = self.s._serialize(test_obj)
        self.assertEqual(message['id'], str(test_obj.attr_a))

        test_obj.attr_a = [1]

        message = self.s._serialize(test_obj)
        self.assertEqual(message['id'], str(test_obj.attr_a))

    def test_attr_bool(self):
        """
        Test serializing an object with bool attributes.
        """
        test_obj = self.TestObj()
        test_obj.attr_c = True

        message = self.s._serialize(test_obj)
        self.assertEqual(message['Key_C'], True)

        test_obj.attr_c = ""

        message = self.s._serialize(test_obj)
        self.assertTrue('Key_C' in message)

        test_obj.attr_c = None

        message = self.s._serialize(test_obj)
        self.assertFalse('Key_C' in message)

        test_obj.attr_c = "NotEmpty"

        message = self.s._serialize(test_obj)
        self.assertEqual(message['Key_C'], True)

    def test_attr_sequence(self):
        """
        Test serializing a sequence.
        """

        test_obj = ["A", "B", "C"]
        output = self.s._serialize(test_obj, '[str]', div='|')
        self.assertEqual(output, "|".join(test_obj))

        test_obj = [1,2,3]
        output = self.s._serialize(test_obj, '[str]', div=',')
        self.assertEqual(output, ",".join([str(i) for i in test_obj]))

    def test_attr_duration(self):
        """
        Test serializing a duration
        """
        test_obj = self.TestObj()
        test_obj.attr_f = timedelta(days=1)

        message = self.s._serialize(test_obj)
        self.assertEqual("P1D", message["AttrF"])

        test_obj = self.TestObj()
        test_obj.attr_f = isodate.parse_duration("P3Y6M4DT12H30M5S")

        message = self.s.body({
            "attr_f": isodate.parse_duration("P3Y6M4DT12H30M5S")},
            'TestObj')
        self.assertEqual("P3Y6M4DT12H30M5S", message["AttrF"])

    def test_attr_list_simple(self):
        """
        Test serializing an object with simple-typed list attributes
        """
        test_obj = self.TestObj()
        test_obj.attr_d = []

        message = self.s._serialize(test_obj)
        self.assertEqual(message['AttrD'], test_obj.attr_d)

        test_obj.attr_d = [1,2,3]

        message = self.s._serialize(test_obj)
        self.assertEqual(message['AttrD'], test_obj.attr_d)

        test_obj.attr_d = ["1","2","3"]

        message = self.s._serialize(test_obj)
        self.assertEqual(message['AttrD'], [int(i) for i in test_obj.attr_d])

        test_obj.attr_d = ["test","test2","test3"]

        with self.assertRaises(SerializationError):
            self.s._serialize(test_obj)

        test_obj.attr_d = "NotAList"

        with self.assertRaises(SerializationError):
            self.s._serialize(test_obj)

    def test_empty_list(self):

        input = []
        output = self.s._serialize(input, '[str]')
        self.assertEqual(output, input)

    def test_attr_list_complex(self):
        """
        Test serializing an object with a list of complex objects as an attribute.
        """
        list_obj = type("ListObj", (Model,), {"_attribute_map":None,
                                        "_validation":{},
                                        "abc":None})
        list_obj._attribute_map = {"abc":{"key":"ABC", "type":"int"}}
        list_obj.abc = "123"

        test_obj = type("CmplxTestObj", (Model,), {"_attribute_map":None,
                                             "_validation":{},
                                             "test_list":None})

        test_obj._attribute_map = {"test_list":{"key":"_list", "type":"[ListObj]"}}
        test_obj.test_list = [list_obj]

        message = self.s._serialize(test_obj)
        self.assertEqual(message, {'_list':[{'ABC':123}]})

        list_obj = type("BadListObj", (Model,), {"map":None})
        test_obj._attribute_map = {"test_list":{"key":"_list", "type":"[BadListObj]"}}
        test_obj.test_list = [list_obj]

        s = self.s._serialize(test_obj)
        self.assertEqual(s, {'_list':[{}]})

    def test_attr_dict_simple(self):
        """
        Test serializing an object with a simple dictionary attribute.
        """

        test_obj = self.TestObj()
        test_obj.attr_e = {"value": 3.14}

        message = self.s._serialize(test_obj)
        self.assertEqual(message['AttrE']['value'], float(test_obj.attr_e["value"]))

        test_obj.attr_e = {1: "3.14"}

        message = self.s._serialize(test_obj)
        self.assertEqual(message['AttrE']['1'], float(test_obj.attr_e[1]))

        test_obj.attr_e = "NotADict"

        with self.assertRaises(SerializationError):
            self.s._serialize(test_obj)

        # with pytest.raises(ValidationError) as err:
        #     test_obj.validate()
        # assert "Parameter 'attr_e' must be of type 'dict[str, float]'" in str(err.value)

        test_obj.attr_e = {"value": "NotAFloat"}

        with self.assertRaises(SerializationError):
            self.s._serialize(test_obj)

    def test_serialize_datetime(self):

        date_obj = isodate.parse_datetime('2015-01-01T00:00:00')
        date_str = Serializer.serialize_iso(date_obj)

        self.assertEqual(date_str, '2015-01-01T00:00:00.000Z')

        date_obj = isodate.parse_datetime('1999-12-31T23:59:59-12:00')
        date_str = Serializer.serialize_iso(date_obj)

        self.assertEqual(date_str, '2000-01-01T11:59:59.000Z')

        with self.assertRaises(SerializationError):
            date_obj = isodate.parse_datetime('9999-12-31T23:59:59-12:00')
            date_str = Serializer.serialize_iso(date_obj)

        with self.assertRaises(SerializationError):
            date_obj = isodate.parse_datetime('0001-01-01T00:00:00+23:59')
            date_str = Serializer.serialize_iso(date_obj)


        date_obj = isodate.parse_datetime("2015-06-01T16:10:08.0121-07:00")
        date_str = Serializer.serialize_iso(date_obj)

        self.assertEqual(date_str, '2015-06-01T23:10:08.0121Z')

        date_obj = datetime.min
        date_str = Serializer.serialize_iso(date_obj)
        self.assertEqual(date_str, '0001-01-01T00:00:00.000Z')

        date_obj = datetime.max
        date_str = Serializer.serialize_iso(date_obj)
        self.assertEqual(date_str, '9999-12-31T23:59:59.999999Z')

        date_obj = isodate.parse_datetime('2012-02-24T00:53:52.000001Z')
        date_str = Serializer.serialize_iso(date_obj)
        assert date_str == '2012-02-24T00:53:52.000001Z'

        date_obj = isodate.parse_datetime('2012-02-24T00:53:52.780Z')
        date_str = Serializer.serialize_iso(date_obj)
        assert date_str == '2012-02-24T00:53:52.780Z'

    def test_serialize_time(self):

        time_str = Serializer.serialize_time(time(11,22,33))
        assert time_str == "11:22:33"

        time_str = Serializer.serialize_time(time(11,22,33,444))
        assert time_str == "11:22:33.444"

    def test_serialize_primitive_types(self):

        a = self.s.serialize_data(1, 'int')
        self.assertEqual(a, 1)

        b = self.s.serialize_data(True, 'bool')
        self.assertEqual(b, True)

        c = self.s.serialize_data('True', 'str')
        self.assertEqual(c, 'True')

        d = self.s.serialize_data(100.0123, 'float')
        self.assertEqual(d, 100.0123)

    def test_serialize_object(self):

        a = self.s.body(1, 'object')
        self.assertEqual(a, 1)

        b = self.s.body(True, 'object')
        self.assertEqual(b, True)

        c = self.s.serialize_data('True', 'object')
        self.assertEqual(c, 'True')

        d = self.s.serialize_data(100.0123, 'object')
        self.assertEqual(d, 100.0123)

        e = self.s.serialize_data({}, 'object')
        self.assertEqual(e, {})

        f = self.s.body({"test":"data"}, 'object')
        self.assertEqual(f, {"test":"data"})

        g = self.s.body({"test":{"value":"data"}}, 'object')
        self.assertEqual(g, {"test":{"value":"data"}})

        h = self.s.serialize_data({"test":self.TestObj('id')}, 'object')
        self.assertEqual(h, {"test":{'id': 'id'}})

        i =  self.s.serialize_data({"test":[1,2,3,4,5]}, 'object')
        self.assertEqual(i, {"test":[1,2,3,4,5]})

    def test_serialize_empty_iter(self):

        a = self.s.serialize_dict({}, 'int')
        self.assertEqual(a, {})

        b = self.s.serialize_iter([], 'int')
        self.assertEqual(b, [])

    def test_serialize_str_as_iter(self):
        with self.assertRaises(SerializationError):
            self.s.serialize_iter("I am a string", 'str')

    def test_serialize_int_as_iter_with_div(self):
        # https://github.com/Azure/azure-sdk-for-python/issues/4501
        assert self.s.serialize_iter([1,2,3,4], "int", ",") == "1,2,3,4"

    def test_serialize_from_dict_datetime(self):
        class DateTimeTest(Model):
            _attribute_map = {
                'birthday':{'key':'birthday','type':'iso-8601'},
            }
            def __init__(self, birthday):
                self.birthday = birthday

        serializer = Serializer({
            'DateTimeTest': DateTimeTest
        })

        mydate = serializer.body(
            {'birthday': datetime(1980, 12, 27)},
            'DateTimeTest'
        )
        assert mydate["birthday"] == "1980-12-27T00:00:00.000Z"

    def test_serialize_json_obj(self):

        class ComplexId(Model):

            _validation = {}
            _attribute_map = {'id':{'key':'id','type':'int'},
                              'name':{'key':'name','type':'str'},
                              'age':{'key':'age','type':'float'},
                              'male':{'key':'male','type':'bool'},
                              'birthday':{'key':'birthday','type':'iso-8601'},
                              'anniversary':{'key':'anniversary', 'type':'iso-8601'}}

            id = 1
            name = "Joey"
            age = 23.36
            male = True
            birthday = '1992-01-01T00:00:00.000Z'
            anniversary = isodate.parse_datetime('2013-12-08T00:00:00')

        class ComplexJson(Model):

            _validation = {}
            _attribute_map = {'p1':{'key':'p1','type':'str'},
                              'p2':{'key':'p2','type':'str'},
                              'top_date':{'key':'top_date', 'type':'iso-8601'},
                              'top_dates':{'key':'top_dates', 'type':'[iso-8601]'},
                              'insider':{'key':'insider','type':'{iso-8601}'},
                              'top_complex':{'key':'top_complex','type':'ComplexId'}}

            p1 = 'value1'
            p2 = 'value2'
            top_date = isodate.parse_datetime('2014-01-01T00:00:00')
            top_dates = [isodate.parse_datetime('1900-01-01T00:00:00'), isodate.parse_datetime('1901-01-01T00:00:00')]
            insider = {
                'k1': isodate.parse_datetime('2015-01-01T00:00:00'),
                'k2': isodate.parse_datetime('2016-01-01T00:00:00'),
                'k3': isodate.parse_datetime('2017-01-01T00:00:00')}
            top_complex = ComplexId()

        message =self.s._serialize(ComplexJson())

        output = {
            'p1': 'value1',
            'p2': 'value2',
            'top_date': '2014-01-01T00:00:00.000Z',
            'top_dates': [
                '1900-01-01T00:00:00.000Z',
                '1901-01-01T00:00:00.000Z'
            ],
            'insider': {
                'k1': '2015-01-01T00:00:00.000Z',
                'k2': '2016-01-01T00:00:00.000Z',
                'k3': '2017-01-01T00:00:00.000Z'
            },
            'top_complex': {
                'id': 1,
                'name': 'Joey',
                'age': 23.36,
                'male': True,
                'birthday': '1992-01-01T00:00:00.000Z',
                'anniversary': '2013-12-08T00:00:00.000Z',
            }
        }
        self.maxDiff = None
        self.assertEqual(message, output)

        message = ComplexJson().serialize()
        self.assertEqual(message, output)

    def test_polymorphic_serialization(self):

        self.maxDiff = None
        class Zoo(Model):

            _attribute_map = {
                "animals":{"key":"Animals", "type":"[Animal]"},
            }

            def __init__(self, animals=None):
                self.animals = animals

        class Animal(Model):

            _attribute_map = {
                "name":{"key":"Name", "type":"str"},
                "d_type":{"key":"dType", "type":"str"}
            }

            _subtype_map = {
                'd_type': {"cat":"Cat", "dog":"Dog"}
            }

            def __init__(self, name=None):
                self.name = name

        class Dog(Animal):

            _attribute_map = {
                "name":{"key":"Name", "type":"str"},
                "likes_dog_food":{"key":"likesDogFood","type":"bool"},
                "d_type":{"key":"dType", "type":"str"}
                }

            def __init__(self, name=None, likes_dog_food=None):
                self.likes_dog_food = likes_dog_food
                super(Dog, self).__init__(name)
                self.d_type = 'dog'

        class Cat(Animal):

            _attribute_map = {
                "name":{"key":"Name", "type":"str"},
                "likes_mice":{"key":"likesMice","type":"bool"},
                "dislikes":{"key":"dislikes","type":"Animal"},
                "d_type":{"key":"dType", "type":"str"}
                }

            _subtype_map = {
                "d_type":{"siamese":"Siamese"}
                }

            def __init__(self, name=None, likes_mice=None, dislikes = None):
                self.likes_mice = likes_mice
                self.dislikes = dislikes
                super(Cat, self).__init__(name)
                self.d_type = 'cat'

        class Siamese(Cat):

            _attribute_map = {
                "name":{"key":"Name", "type":"str"},
                "likes_mice":{"key":"likesMice","type":"bool"},
                "dislikes":{"key":"dislikes","type":"Animal"},
                "color":{"key":"Color", "type":"str"},
                "d_type":{"key":"dType", "type":"str"}
                }

            def __init__(self, name=None, likes_mice=None, dislikes = None, color=None):
                self.color = color
                super(Siamese, self).__init__(name, likes_mice, dislikes)
                self.d_type = 'siamese'

        message = {
            "Animals": [
            {
            "dType": "dog",
            "likesDogFood": True,
            "Name": "Fido"
            },
            {
            "dType": "cat",
            "likesMice": False,
            "dislikes": {
            "dType": "dog",
            "likesDogFood": True,
            "Name": "Angry"
            },
            "Name": "Felix"
            },
            {
            "dType": "siamese",
            "Color": "grey",
            "likesMice": True,
            "Name": "Finch"
            }]}

        zoo = Zoo()
        angry = Dog()
        angry.name = "Angry"
        angry.likes_dog_food = True

        fido = Dog()
        fido.name = "Fido"
        fido.likes_dog_food = True

        felix = Cat()
        felix.name = "Felix"
        felix.likes_mice = False
        felix.dislikes = angry

        finch = Siamese()
        finch.name = "Finch"
        finch.color = "grey"
        finch.likes_mice = True

        zoo.animals = [fido, felix, finch]

        serialized = self.s._serialize(zoo)
        self.assertEqual(serialized, message)

        old_dependencies = self.s.dependencies
        self.s.dependencies = {
            'Zoo': Zoo,
            'Animal': Animal,
            'Dog': Dog,
            'Cat': Cat,
            'Siamese': Siamese
        }

        serialized = self.s.body({
            "animals": [{
                "dType": "dog",
                "likes_dog_food": True,
                "name": "Fido"
            },{
                "dType": "cat",
                "likes_mice": False,
                "dislikes": {
                    "dType": "dog",
                    "likes_dog_food": True,
                    "name": "Angry"
                },
                "name": "Felix"
            },{
                "dType": "siamese",
                "color": "grey",
                "likes_mice": True,
                "name": "Finch"
            }]
        }, "Zoo")
        self.assertEqual(serialized, message)

        self.s.dependencies = old_dependencies

    def test_key_type(self):

        class TestKeyTypeObj(Model):

            _validation = {}
            _attribute_map = {
                'attr_a': {'key':'attr_a', 'type':'int'},
                'attr_b': {'key':'id', 'type':'int'},
                'attr_c': {'key':'KeyC', 'type': 'int'},
                'attr_d': {'key':'properties.KeyD', 'type': 'int'},
            }

        old_dependencies = self.s.dependencies
        self.s.dependencies = {
            'TestKeyTypeObj': TestKeyTypeObj,
        }

        serialized = self.s.body({
            "attr_a": 1,
            "id": 2,
            "keyc": 3,
            "keyd": 4
        }, "TestKeyTypeObj")

        message = {
            "attr_a": 1,
            "id": 2,
            "KeyC": 3,
            "properties": {
                "KeyD": 4
            }
        }

        self.assertEqual(serialized, message)

        self.s.dependencies = old_dependencies

    def test_additional_properties_no_send(self):

        class AdditionalTest(Model):

            _attribute_map = {
                "name": {"key":"Name", "type":"str"}
            }

            def __init__(self, name=None):
                self.name = name

        o = AdditionalTest(
            name='test'
        )
        o.additional_properties={
            "PropInt": 2,
            "PropStr": "AdditionalProperty",
            "PropArray": [1,2,3],
            "PropDict": {"a": "b"}
        }

        expected_message = {
            "Name": "test"
        }

        s = Serializer({'AdditionalTest': AdditionalTest})

        serialized = s.body(o, 'AdditionalTest')

        self.assertEqual(serialized, expected_message)


    def test_additional_properties_manual(self):

        class AdditionalTest(Model):

            _attribute_map = {
                "name": {"key":"Name", "type":"str"}
            }

            def __init__(self, name=None):
                self.name = name
        AdditionalTest.enable_additional_properties_sending()

        o = AdditionalTest(
            name='test'
        )
        o.additional_properties={
            "PropInt": 2,
            "PropStr": "AdditionalProperty",
            "PropArray": [1,2,3],
            "PropDict": {"a": "b"}
        }

        expected_message = {
            "Name": "test",
            "PropInt": 2,
            "PropStr": "AdditionalProperty",
            "PropArray": [1,2,3],
            "PropDict": {"a": "b"}
        }

        s = Serializer({'AdditionalTest': AdditionalTest})

        serialized = s.body(o, 'AdditionalTest')

        self.assertEqual(serialized, expected_message)


    def test_additional_properties(self):

        class AdditionalTest(Model):

            _attribute_map = {
                "name": {"key":"Name", "type":"str"},
                'additional_properties': {'key': '', 'type': '{object}'}
            }

            def __init__(self, name=None, additional_properties=None):
                self.name = name
                self.additional_properties = additional_properties

        o = AdditionalTest(
            name='test',
            additional_properties={
                "PropInt": 2,
                "PropStr": "AdditionalProperty",
                "PropArray": [1,2,3],
                "PropDict": {"a": "b"}
            }
        )

        expected_message = {
            "Name": "test",
            "PropInt": 2,
            "PropStr": "AdditionalProperty",
            "PropArray": [1,2,3],
            "PropDict": {"a": "b"}
        }

        s = Serializer({'AdditionalTest': AdditionalTest})

        serialized = s.body(o, 'AdditionalTest')

        self.assertEqual(serialized, expected_message)


    def test_additional_properties_with_auto_model(self):

        class AdditionalTest(Model):

            _attribute_map = {
                "name": {"key":"Name", "type":"str"},
                "display_name": {"key":"DisplayName", "type":"str"},
                'additional_properties': {'key': '', 'type': '{object}'}
            }

        o = {
            'name': 'test',
            'display_name': "display_name"
        }

        expected_message = {
            "Name": "test",
            "DisplayName": "display_name",
        }

        s = Serializer({'AdditionalTest': AdditionalTest})

        serialized = s.body(o, 'AdditionalTest')

        self.assertEqual(serialized, expected_message)

    def test_additional_properties_declared(self):

        class AdditionalTest(Model):

            _attribute_map = {
                "name": {"key":"Name", "type":"str"},
                'additional_properties': {'key': 'AddProp', 'type': '{object}'}
            }

            def __init__(self, name=None, additional_properties=None):
                self.name = name
                self.additional_properties = additional_properties

        o = AdditionalTest(
            name='test',
            additional_properties={
                "PropInt": 2,
                "PropStr": "AdditionalProperty",
                "PropArray": [1,2,3],
                "PropDict": {"a": "b"}
            }
        )

        expected_message = {
            "Name": "test",
            "AddProp": {
                "PropInt": 2,
                "PropStr": "AdditionalProperty",
                "PropArray": [1,2,3],
                "PropDict": {"a": "b"}
            }
        }

        s = Serializer({'AdditionalTest': AdditionalTest})

        serialized = s.body(o, 'AdditionalTest')

        self.assertEqual(serialized, expected_message)

        # Make it declared as a property AND readonly
        AdditionalTest._validation = {
            'additional_properties': {'readonly': True}
        }

        expected_message = {
            "Name": "test"
        }

        s = Serializer({'AdditionalTest': AdditionalTest})

        serialized = s.body(o, 'AdditionalTest')

        self.assertEqual(serialized, expected_message)

    def test_long_as_type_object(self):
        """Test irrelevant on Python 3. But still doing it to test regression.
            https://github.com/Azure/msrest-for-python/pull/121
        """

        try:
            long_type = long
        except NameError:
            long_type = int

        s = Serializer()
        assert s.serialize_data(long_type(1), 'object') == long_type(1)

        class TestModel(Model):
            _attribute_map = {'data': {'key': 'data', 'type': 'object'}}

        m = TestModel(data = {'id': long_type(1)})
        serialized = m.serialize()
        assert serialized == {
            'data': {'id': long_type(1)}
        }

    def test_unicode_as_type_object(self):
        """Test irrelevant on Python 3. But still doing it to test regression.
            https://github.com/Azure/msrest-for-python/issue/221
        """

        s = Serializer()
        assert s.serialize_data(u"\ua015", 'object') == u"\ua015"

        class TestModel(Model):
            _attribute_map = {'data': {'key': 'data', 'type': 'object'}}

        m = TestModel(data = {'id': u"\ua015"})
        serialized = m.serialize()
        assert serialized == {
            'data': {'id': u"\ua015"}
        }

    def test_datetime_types_as_type_object(self):
        """https://github.com/Azure/msrest-for-python/issues/223
        """

        class TestModel(Model):
            _attribute_map = {'data': {'key': 'data', 'type': 'object'}}

        m = TestModel(data = {
            'datetime': isodate.parse_datetime('2012-02-24T00:53:52.780Z'),
            'date': date(2019,5,1),
            'time': time(11,12,13),
            'timedelta': timedelta(56)
        })
        serialized = m.serialize()
        assert serialized['data'] == {
            'datetime': '2012-02-24T00:53:52.780Z',
            'date': '2019-05-01',
            'time': '11:12:13',
            'timedelta': 'P56D'
        }

    def test_decimal_types_as_type_object(self):
        """https://github.com/Azure/msrest-for-python/issues/223
        """

        class TestModel(Model):
            _attribute_map = {'data': {'key': 'data', 'type': 'object'}}

        m = TestModel(data = {
            'decimal': Decimal('1.1'),
        })
        serialized = m.serialize()
        assert serialized['data'] == {
            'decimal': 1.1
        }

    def test_json_with_xml_map(self):
        basic_json = {'age': 37, 'country': 'france'}

        class XmlModel(Model):
            _attribute_map = {
                'age': {'key': 'age', 'type': 'int', 'xml':{'name': 'Age'}},
                'country': {'key': 'country', 'type': 'str', 'xml':{'name': 'country', 'attr': True}},
            }
            _xml_map = {
                'name': 'Data'
            }

        mymodel = XmlModel(
            age=37,
            country="france",
        )

        s = Serializer({"XmlModel": XmlModel})
        rawxml = s.body(mymodel, 'XmlModel', is_xml=False)

        assert rawxml==basic_json

class TestRuntimeDeserialized(unittest.TestCase):

    class TestObj(Model):

        _validation = {}
        _attribute_map = {
            'attr_a': {'key':'id', 'type':'str'},
            'attr_b': {'key':'AttrB', 'type':'int'},
            'attr_c': {'key':'Key_C', 'type': 'bool'},
            'attr_d': {'key':'AttrD', 'type':'[int]'},
            'attr_e': {'key':'AttrE', 'type': '{float}'},
            'attr_f': {'key':'AttrF', 'type': '[[str]]'}
            }

        _header_map = {
            'client_request_id': {'key': 'client-request-id', 'type':'str'},
            'e_tag': {'key': 'etag', 'type':'str'},
            }

        _response_map = {
            'status_code': {'key':'status_code', 'type':'str'}
            }


    def setUp(self):
        self.d = Deserializer()
        return super(TestRuntimeDeserialized, self).setUp()

    def test_cls_method_deserialization(self):
        json_data = {
            'id': 'myid',
            'AttrB': 42,
            'Key_C': True,
            'AttrD': [1,2,3],
            'AttrE': {'pi': 3.14},
            'AttrF': [['internal', 'list', 'of', 'strings']]
        }

        def assert_model(inst):
            self.assertEqual(inst.attr_a, 'myid')
            self.assertEqual(inst.attr_b, 42)
            self.assertEqual(inst.attr_c, True)
            self.assertEqual(inst.attr_d, [1,2,3])
            self.assertEqual(inst.attr_e, {'pi': 3.14})
            self.assertEqual(inst.attr_f, [['internal', 'list', 'of', 'strings']])

        model_instance = self.TestObj.from_dict(json_data)
        assert_model(model_instance)

        # Get an attribute version of  this model
        attr_data = {
            'attr_a': 'myid',
            'attr_b': 42,
            'attr_c': True,
            'attr_d': [1,2,3],
            'attr_e': {'pi': 3.14},
            'attr_f': [['internal', 'list', 'of', 'strings']]
        }
        self.TestObj.from_dict(attr_data)
        assert_model(model_instance)

    def test_twice_key_scenario(self):
        # To reproduce the initial bug, you need a attribute named after the last part
        # of a flattening JSON from another attribute (here type)
        # https://github.com/Azure/azure-sdk-for-python/issues/11422
        # Issue happened where searching for "type2", since we found a match in both "type2" and "type" keys

        class LocalModel(Model):
            _attribute_map = {
                'id': {'key': 'id', 'type': 'int'},
                'type': {'key': 'type_dont_matter_not_used', 'type': 'str'},
                'type2': {'key': 'properties.type', 'type': 'str'},
            }

            def __init__(self, **kwargs):
                super(LocalModel, self).__init__(**kwargs)

        raw = {
            'id': 42,
            'type': "type",
            'type2': "type2"
        }

        m = LocalModel.from_dict(raw)
        assert m.id == 42
        assert m.type == "type"
        assert m.type2 == "type2"

    def test_array_deserialize(self):
        result = self.d('[str]', ["a","b"])
        assert result == ['a','b']

    def test_personalize_deserialization(self):

        class TestDurationObj(Model):
            _attribute_map = {
                'attr_a': {'key':'attr_a', 'type':'duration'},
            }

        with self.assertRaises(DeserializationError):
            obj = TestDurationObj.from_dict({
                "attr_a": "00:00:10"
            })

        def duration_rest_key_extractor(attr, attr_desc, data):
            value = rest_key_extractor(attr, attr_desc, data)
            if attr == "attr_a":
                # Stupid parsing, this is just a test
                return "PT"+value[-2:]+"S"

        obj = TestDurationObj.from_dict(
            {"attr_a": "00:00:10"},
            key_extractors=[duration_rest_key_extractor]
        )
        self.assertEqual(timedelta(seconds=10), obj.attr_a)


    def test_robust_deserialization(self):

        class TestKeyTypeObj(Model):

            _validation = {}
            _attribute_map = {
                'attr_a': {'key':'attr_a', 'type':'int'},
                'attr_b': {'key':'id', 'type':'int'},
                'attr_c': {'key':'KeyC', 'type': 'int'},
                'attr_d': {'key':'properties.KeyD', 'type': 'int'},
            }

        obj = TestKeyTypeObj.from_dict({
            "attr_a": 1,
            "id": 2,
            "keyc": 3,
            "keyd": 4
        })

        self.assertEqual(1, obj.attr_a)
        self.assertEqual(2, obj.attr_b)
        self.assertEqual(3, obj.attr_c)
        self.assertEqual(4, obj.attr_d)

        obj = TestKeyTypeObj.from_dict({
            "attr_a": 1,
            "id": 2,
            "keyc": 3,
            "properties": {
                "KeyD": 4
            }
        })

        self.assertEqual(1, obj.attr_a)
        self.assertEqual(2, obj.attr_b)
        self.assertEqual(3, obj.attr_c)
        self.assertEqual(4, obj.attr_d)

        # This one used to raise an exception, but after https://github.com/Azure/msrest-for-python/pull/204
        # we decide to accept it with log warning

        obj = TestKeyTypeObj.from_dict({
            "attr_a": 1,
            "attr_b": 12, # Conflict with "id"
            "id": 14, # Conflict with "attr_b"
            "keyc": 3,
            "keyd": 4
        })

        self.assertEqual(1, obj.attr_a)
        self.assertEqual(12, obj.attr_b)  # from_dict will prioritize attribute syntax
        self.assertEqual(3, obj.attr_c)
        self.assertEqual(4, obj.attr_d)

    def test_basic_deserialization(self):
        class TestObj(Model):

            _validation = {
                'name': {'min_length': 3},
            }
            _attribute_map = {
                'name': {'key':'RestName', 'type':'str'},
            }

            def __init__(self, name):
                self.name = name

        obj = TestObj.from_dict({'name': 'ab'})
        self.assertEqual('ab', obj.name)

    def test_deserialize_flattening(self):
        # https://github.com/Azure/msrest-for-python/issues/197

        json_body = {
            "properties" : {
                "properties": None
            }
        }

        class ComputeResource(Model):

            _attribute_map = {
                'properties': {'key': 'properties', 'type': 'VirtualMachine'},
            }

            def __init__(self, properties=None, **kwargs):
                self.properties = properties

        class VirtualMachine(Model):

            _attribute_map = {
                'virtual_machine_size': {'key': 'properties.virtualMachineSize', 'type': 'str'},
                'ssh_port': {'key': 'properties.sshPort', 'type': 'int'},
                'address': {'key': 'properties.address', 'type': 'str'},
                'administrator_account': {'key': 'properties.administratorAccount', 'type': 'VirtualMachineSshCredentials'},
            }

            def __init__(self, **kwargs):
                super(VirtualMachine, self).__init__(**kwargs)
                self.virtual_machine_size = kwargs.get('virtual_machine_size', None)
                self.ssh_port = kwargs.get('ssh_port', None)
                self.address = kwargs.get('address', None)
                self.administrator_account = kwargs.get('administrator_account', None)

        d = Deserializer({
            'ComputeResource': ComputeResource,
            'VirtualMachine': VirtualMachine,
        })
        response = d(ComputeResource, json.dumps(json_body), 'application/json')

    def test_deserialize_storage(self):
        StorageAccount = storage_models.StorageAccount
        json_storage = {
            'id': '/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/test_mgmt_storage_test_storage_accounts43b8102a/providers/Microsoft.Storage/storageAccounts/pyarmstorage43b8102a',
            'kind': 'Storage',
            'location': 'westus',
            'name': 'pyarmstorage43b8102a',
            'properties': {
                'creationTime': '2017-07-19T23:19:21.7640412Z',
                'primaryEndpoints': {'blob': 'https://pyarmstorage43b8102a.blob.core.windows.net/',
                    'file': 'https://pyarmstorage43b8102a.file.core.windows.net/',
                    'queue': 'https://pyarmstorage43b8102a.queue.core.windows.net/',
                    'table': 'https://pyarmstorage43b8102a.table.core.windows.net/'},
                'primaryLocation': 'westus',
                'provisioningState': 'Succeeded',
                'statusOfPrimary': 'available',
                'supportsHttpsTrafficOnly': False},
            'sku': {'name': 'Standard_LRS', 'tier': 'Standard'},
            'tags': {},
            'type': 'Microsoft.Storage/storageAccounts'}

        storage_account = StorageAccount.deserialize(json_storage)

        self.assertEqual(storage_account.id, json_storage['id']) # basic
        self.assertEqual(storage_account.sku.name, storage_models.SkuName(json_storage['sku']['name'])) # Nested + enum
        self.assertEqual(storage_account.primary_location, json_storage['properties']['primaryLocation']) # Flatten

        json_storage_output = storage_account.serialize()
        self.assertEqual(len(json_storage_output), 3) # Only 3 keys are not readonly

        json_storage_output = storage_account.as_dict(key_transformer=full_restapi_key_transformer)
        self.assertListEqual(
            sorted(list(json_storage_output.keys())),
            sorted(list(json_storage.keys()))
        )

        json_storage_output = storage_account.as_dict(keep_readonly=False, key_transformer=full_restapi_key_transformer)
        self.assertListEqual(
            sorted(list(json_storage_output.keys())),
            ['location', 'properties', 'tags']
        )

    def test_invalid_json(self):
        """
        Test invalid JSON
        """
        with self.assertRaises(DeserializationError):
            self.d("[str]", '["tata"]]', 'application/json')


    def test_non_obj_deserialization(self):
        """
        Test direct deserialization of simple types.
        """
        with self.assertRaises(DeserializationError):
            self.d("[str]", '', 'application/json')

        with self.assertRaises(DeserializationError):
            self.d("[str]", json.dumps(''), 'application/json')

        with self.assertRaises(DeserializationError):
            self.d("[str]", json.dumps({}), 'application/json')

        message = ["a","b","b"]
        response = self.d("[str]", json.dumps(message), 'application/json')
        self.assertEqual(response, message)

        with self.assertRaises(DeserializationError):
            self.d("[str]", json.dumps(12345), 'application/json')

        response = self.d('bool', json.dumps('true'), 'application/json')
        self.assertEqual(response, True)

        response = self.d('bool', json.dumps(1), 'application/json')
        self.assertEqual(response, True)

        with self.assertRaises(DeserializationError):
            self.d('bool', json.dumps("true1"), 'application/json')


    def test_obj_with_no_attr(self):
        """
        Test deserializing an object with no attributes.
        """
        class EmptyResponse(Model):
            _attribute_map = {}
            _header_map = {}


        deserialized = self.d(EmptyResponse, json.dumps({"a":"b"}), 'application/json')
        self.assertIsInstance(deserialized, EmptyResponse)

    def test_obj_with_malformed_map(self):
        """
        Test deserializing an object with a malformed attributes_map.
        """
        class BadResponse(Model):
            _attribute_map = None

            def __init__(*args, **kwargs):
                pass

        with self.assertRaises(DeserializationError):
            self.d(BadResponse, json.dumps({"a":"b"}), 'application/json')

        class BadResponse(Model):
            _attribute_map = {"attr":"val"}

            def __init__(*args, **kwargs):
                pass

        with self.assertRaises(DeserializationError):
            self.d(BadResponse, json.dumps({"a":"b"}), 'application/json')

        class BadResponse(Model):
            _attribute_map = {"attr":{"val":1}}

            def __init__(*args, **kwargs):
                pass

        with self.assertRaises(DeserializationError):
            self.d(BadResponse, json.dumps({"a":"b"}), 'application/json')

    def test_attr_none(self):
        """
        Test serializing an object with None attributes.
        """
        response = self.d(self.TestObj, 'null', 'application/json')
        self.assertIsNone(response)

    def test_attr_int(self):
        """
        Test deserializing an object with Int attributes.
        """
        message = {'AttrB':'1234'}
        response = self.d(self.TestObj, json.dumps(message), 'application/json')
        self.assertTrue(hasattr(response, 'attr_b'))
        self.assertEqual(response.attr_b, int(message['AttrB']))

        with self.assertRaises(DeserializationError):
            response = self.d(self.TestObj, json.dumps({'AttrB':'NotANumber'}), 'application/json')

    def test_attr_str(self):
        """
        Test deserializing an object with Str attributes.
        """
        message = {'id':'InterestingValue'}

        response = self.d(self.TestObj, json.dumps(message), 'application/json')
        self.assertTrue(hasattr(response, 'attr_a'))
        self.assertEqual(response.attr_a, message['id'])

        message = {'id':1234}
        response = self.d(self.TestObj, json.dumps(message), 'application/json')
        self.assertEqual(response.attr_a, str(message['id']))

        message = {'id':list()}
        response = self.d(self.TestObj, json.dumps(message), 'application/json')
        self.assertEqual(response.attr_a, str(message['id']))

        response = self.d(self.TestObj, json.dumps({'id':None}), 'application/json')
        self.assertEqual(response.attr_a, None)

    def test_attr_bool(self):
        """
        Test deserializing an object with bool attributes.
        """
        response = self.d(self.TestObj, json.dumps({'Key_C':True}), 'application/json')
        self.assertTrue(hasattr(response, 'attr_c'))
        self.assertEqual(response.attr_c, True)

        with self.assertRaises(DeserializationError):
            response = self.d(self.TestObj, json.dumps({'Key_C':[]}), 'application/json')

        response = self.d(self.TestObj, json.dumps({'Key_C':0}), 'application/json')
        self.assertEqual(response.attr_c, False)

        with self.assertRaises(DeserializationError):
            response = self.d(self.TestObj, json.dumps({'Key_C':"value"}), 'application/json')

    def test_attr_list_simple(self):
        """
        Test deserializing an object with simple-typed list attributes
        """
        response = self.d(self.TestObj, json.dumps({'AttrD': []}), 'application/json')
        deserialized_list = [d for d in response.attr_d]
        self.assertEqual(deserialized_list, [])

        message = {'AttrD': [1,2,3]}
        response = self.d(self.TestObj, json.dumps(message), 'application/json')
        deserialized_list = [d for d in response.attr_d]
        self.assertEqual(deserialized_list, message['AttrD'])

        message = {'AttrD': ["1","2","3"]}
        response = self.d(self.TestObj, json.dumps(message), 'application/json')
        deserialized_list = [d for d in response.attr_d]
        self.assertEqual(deserialized_list, [int(i) for i in message['AttrD']])

        with self.assertRaises(DeserializationError):
            response = self.d(self.TestObj, json.dumps({'AttrD': ["test","test2","test3"]}), 'application/json')
            deserialized_list = [d for d in response.attr_d]

        with self.assertRaises(DeserializationError):
            response = self.d(self.TestObj, json.dumps({'AttrD': "NotAList"}), 'application/json')
            deserialized_list = [d for d in response.attr_d]

        self.assertListEqual(sorted(self.d("[str]", ["a", "b", "c"])), ["a", "b", "c"])
        self.assertListEqual(sorted(self.d("[str]", {"a", "b", "c"})), ["a", "b", "c"])

    def test_attr_list_in_list(self):
        """
        Test deserializing a list of lists
        """
        response = self.d(self.TestObj, json.dumps({'AttrF':[]}), 'application/json')
        self.assertTrue(hasattr(response, 'attr_f'))
        self.assertEqual(response.attr_f, [])

        response = self.d(self.TestObj, json.dumps({'AttrF':None}), 'application/json')
        self.assertTrue(hasattr(response, 'attr_f'))
        self.assertEqual(response.attr_f, None)

        response = self.d(self.TestObj, json.dumps({}), 'application/json')
        self.assertTrue(hasattr(response, 'attr_f'))
        self.assertEqual(response.attr_f, None)

        message = {'AttrF':[[]]}
        response = self.d(self.TestObj, json.dumps(message), 'application/json')
        self.assertTrue(hasattr(response, 'attr_f'))
        self.assertEqual(response.attr_f, message['AttrF'])

        message = {'AttrF':[[1,2,3], ['a','b','c']]}
        response = self.d(self.TestObj, json.dumps(message), 'application/json')
        self.assertTrue(hasattr(response, 'attr_f'))
        self.assertEqual(response.attr_f, [[str(i) for i in k] for k in message['AttrF']])

        with self.assertRaises(DeserializationError):
            response = self.d(self.TestObj, json.dumps({'AttrF':[1,2,3]}), 'application/json')

    def test_attr_list_complex(self):
        """
        Test deserializing an object with a list of complex objects as an attribute.
        """
        class ListObj(Model):
            _attribute_map = {"abc":{"key":"ABC", "type":"int"}}

        class CmplxTestObj(Model):
            _response_map = {}
            _attribute_map = {'attr_a': {'key':'id', 'type':'[ListObj]'}}


        d = Deserializer({'ListObj':ListObj})
        response = d(CmplxTestObj, json.dumps({"id":[{"ABC": "123"}]}), 'application/json')
        deserialized_list = list(response.attr_a)

        self.assertIsInstance(deserialized_list[0], ListObj)
        self.assertEqual(deserialized_list[0].abc, 123)

    def test_deserialize_object(self):

        a = self.d('object', 1)
        self.assertEqual(a, 1)

        b = self.d('object', True)
        self.assertEqual(b, True)

        c = self.d('object', 'True')
        self.assertEqual(c, 'True')

        d = self.d('object', 100.0123)
        self.assertEqual(d, 100.0123)

        e = self.d('object', {})
        self.assertEqual(e, {})

        f = self.d('object', {"test":"data"})
        self.assertEqual(f, {"test":"data"})

        g = self.d('object', {"test":{"value":"data"}})
        self.assertEqual(g, {"test":{"value":"data"}})

        with self.assertRaises(DeserializationError):
            self.d('object', {"test":self.TestObj()})

        h =  self.d('object', {"test":[1,2,3,4,5]})
        self.assertEqual(h, {"test":[1,2,3,4,5]})

    def test_deserialize_date(self):
        # https://github.com/OAI/OpenAPI-Specification/blob/4d5a749c365682e6718f5a78f113a64391911647/versions/2.0.md#data-types
        a = Deserializer.deserialize_date('2018-12-27')
        self.assertEqual(date(2018,12,27), a)

        with self.assertRaises(DeserializationError):
            a = Deserializer.deserialize_date('201O-18-90')

    def test_deserialize_time(self):
        a = Deserializer.deserialize_time('11:22:33')
        assert time(11,22,33) == a

        with self.assertRaises(DeserializationError):
            Deserializer.deserialize_time('1O:22:33')

    def test_deserialize_datetime(self):

        a = Deserializer.deserialize_iso('9999-12-31T23:59:59+23:59')
        utc = a.utctimetuple()

        self.assertEqual(utc.tm_year, 9999)
        self.assertEqual(utc.tm_mon, 12)
        self.assertEqual(utc.tm_mday, 31)
        self.assertEqual(utc.tm_hour, 0)
        self.assertEqual(utc.tm_min, 0)
        self.assertEqual(utc.tm_sec, 59)
        self.assertEqual(a.microsecond, 0)

        with self.assertRaises(DeserializationError):
            a = Deserializer.deserialize_iso('9999-12-31T23:59:59-23:59')

        a = Deserializer.deserialize_iso('1999-12-31T23:59:59-23:59')
        utc = a.utctimetuple()
        self.assertEqual(utc.tm_year, 2000)
        self.assertEqual(utc.tm_mon, 1)
        self.assertEqual(utc.tm_mday, 1)
        self.assertEqual(utc.tm_hour, 23)
        self.assertEqual(utc.tm_min, 58)
        self.assertEqual(utc.tm_sec, 59)
        self.assertEqual(a.microsecond, 0)

        a = Deserializer.deserialize_iso('0001-01-01T23:59:00+23:59')
        utc = a.utctimetuple()

        self.assertEqual(utc.tm_year, 1)
        self.assertEqual(utc.tm_mon, 1)
        self.assertEqual(utc.tm_mday, 1)
        self.assertEqual(utc.tm_hour, 0)
        self.assertEqual(utc.tm_min, 0)
        self.assertEqual(utc.tm_sec, 0)
        self.assertEqual(a.microsecond, 0)

        # Only supports microsecond precision up to 6 digits, and chop off the rest
        a = Deserializer.deserialize_iso('2018-01-20T18:35:24.666666312345Z')
        utc = a.utctimetuple()

        self.assertEqual(utc.tm_year, 2018)
        self.assertEqual(utc.tm_mon, 1)
        self.assertEqual(utc.tm_mday, 20)
        self.assertEqual(utc.tm_hour, 18)
        self.assertEqual(utc.tm_min, 35)
        self.assertEqual(utc.tm_sec, 24)
        self.assertEqual(a.microsecond, 666666)

        #with self.assertRaises(DeserializationError):
        #    a = Deserializer.deserialize_iso('1996-01-01T23:01:54-22:66') #TODO

        with self.assertRaises(DeserializationError):
            a = Deserializer.deserialize_iso('1996-01-01T23:01:54-24:30')

        with self.assertRaises(DeserializationError):
            a = Deserializer.deserialize_iso('1996-01-01T23:01:78+00:30')

        with self.assertRaises(DeserializationError):
            a = Deserializer.deserialize_iso('1996-01-01T23:60:01+00:30')

        with self.assertRaises(DeserializationError):
            a = Deserializer.deserialize_iso('1996-01-01T24:01:01+00:30')

        #with self.assertRaises(DeserializationError):
        #    a = Deserializer.deserialize_iso('1996-01-01t01:01:01/00:30') #TODO

        with self.assertRaises(DeserializationError):
            a = Deserializer.deserialize_iso('1996-01-01F01:01:01+00:30')

        with self.assertRaises(DeserializationError):
            a = Deserializer.deserialize_iso('2015-02-32')

        with self.assertRaises(DeserializationError):
            a = Deserializer.deserialize_iso('2015-22-01')

        with self.assertRaises(DeserializationError):
            a = Deserializer.deserialize_iso('2010-13-31')

        with self.assertRaises(DeserializationError):
            a = Deserializer.deserialize_iso('99999-12-31')

        with self.assertRaises(DeserializationError):
            a = Deserializer.deserialize_iso(True)

        with self.assertRaises(DeserializationError):
            a = Deserializer.deserialize_iso(2010)

        with self.assertRaises(DeserializationError):
            a = Deserializer.deserialize_iso(None)

        with self.assertRaises(DeserializationError):
            a = Deserializer.deserialize_iso('Happy New Year 2016')

        a = Deserializer.deserialize_iso('2012-02-24T00:53:52.780Z')
        utc = a.utctimetuple()

        self.assertEqual(utc.tm_year, 2012)
        self.assertEqual(utc.tm_mon, 2)
        self.assertEqual(utc.tm_mday, 24)
        self.assertEqual(utc.tm_hour, 0)
        self.assertEqual(utc.tm_min, 53)
        self.assertEqual(utc.tm_sec, 52)
        self.assertEqual(a.microsecond, 780000)

    def test_deserialize_datetime_rfc(self):

        a = Deserializer.deserialize_rfc("Mon, 20 Nov 1995 19:12:08 -0500")
        utc = a.utctimetuple()

        # UTC: 21 Nov, 00:12:08
        self.assertEqual(utc.tm_year, 1995)
        self.assertEqual(utc.tm_mon, 11)
        self.assertEqual(utc.tm_mday, 21)
        self.assertEqual(utc.tm_hour, 0)
        self.assertEqual(utc.tm_min, 12)
        self.assertEqual(utc.tm_sec, 8)
        self.assertEqual(a.microsecond, 0)

        a = Deserializer.deserialize_rfc("Mon, 20 Nov 1995 19:12:08 CDT")
        utc = a.utctimetuple()

        # UTC: 21 Nov, 00:12:08
        self.assertEqual(utc.tm_year, 1995)
        self.assertEqual(utc.tm_mon, 11)
        self.assertEqual(utc.tm_mday, 21)
        self.assertEqual(utc.tm_hour, 0)
        self.assertEqual(utc.tm_min, 12)
        self.assertEqual(utc.tm_sec, 8)
        self.assertEqual(a.microsecond, 0)

        a = Deserializer.deserialize_rfc("Mon, 20 Nov 1995 19:12:08")
        utc = a.utctimetuple()

        # UTC: No info is considered UTC
        self.assertEqual(utc.tm_year, 1995)
        self.assertEqual(utc.tm_mon, 11)
        self.assertEqual(utc.tm_mday, 20)
        self.assertEqual(utc.tm_hour, 19)
        self.assertEqual(utc.tm_min, 12)
        self.assertEqual(utc.tm_sec, 8)
        self.assertEqual(a.microsecond, 0)

        a = Deserializer.deserialize_rfc("Mon, 20 Nov 1995 19:12:08 GMT")
        utc = a.utctimetuple()

        self.assertEqual(utc.tm_year, 1995)
        self.assertEqual(utc.tm_mon, 11)
        self.assertEqual(utc.tm_mday, 20)
        self.assertEqual(utc.tm_hour, 19)
        self.assertEqual(utc.tm_min, 12)
        self.assertEqual(utc.tm_sec, 8)
        self.assertEqual(a.microsecond, 0)

    def test_rfc_pickable(self):
        """Check datetime created by RFC parser are pickable.

        See https://github.com/Azure/msrest-for-python/issues/205
        """

        datetime_rfc = "Mon, 25 May 2020 11:00:00 GMT"
        datetime1 = Deserializer.deserialize_rfc(datetime_rfc)

        pickled = pickle.dumps(datetime1)
        datetime2 = pickle.loads(pickled)

        assert datetime1 == datetime2

    def test_polymorphic_deserialization(self):

        class Zoo(Model):

            _attribute_map = {
                "animals":{"key":"Animals", "type":"[Animal]"},
            }

            def __init__(self, animals=None):
                self.animals = animals

        class Animal(Model):

            _attribute_map = {
                "name":{"key":"Name", "type":"str"},
                "d_type":{"key":"dType", "type":"str"}
            }

            _subtype_map = {
                'd_type': {"cat":"Cat", "dog":"Dog"}
            }

            def __init__(self, name=None):
                self.name = name

        class Dog(Animal):

            _attribute_map = {
                "name":{"key":"Name", "type":"str"},
                "likes_dog_food":{"key":"likesDogFood","type":"bool"},
                "d_type":{"key":"dType", "type":"str"}
                }

            def __init__(self, name=None, likes_dog_food=None):
                self.likes_dog_food = likes_dog_food
                super(Dog, self).__init__(name)
                self.d_type = 'dog'

        class Cat(Animal):

            _attribute_map = {
                "name":{"key":"Name", "type":"str"},
                "likes_mice":{"key":"likesMice","type":"bool"},
                "dislikes":{"key":"dislikes","type":"Animal"},
                "d_type":{"key":"dType", "type":"str"}
                }

            _subtype_map = {
                "d_type":{"siamese":"Siamese"}
                }

            def __init__(self, name=None, likes_mice=None, dislikes = None):
                self.likes_mice = likes_mice
                self.dislikes = dislikes
                super(Cat, self).__init__(name)
                self.d_type = 'cat'

        class Siamese(Cat):

            _attribute_map = {
                "name":{"key":"Name", "type":"str"},
                "likes_mice":{"key":"likesMice","type":"bool"},
                "dislikes":{"key":"dislikes","type":"Animal"},
                "color":{"key":"Color", "type":"str"},
                "d_type":{"key":"dType", "type":"str"}
                }

            def __init__(self, name=None, likes_mice=None, dislikes = None, color=None):
                self.color = color
                super(Siamese, self).__init__(name, likes_mice, dislikes)
                self.d_type = 'siamese'

        message = {
            "Animals": [{
                "dType": "dog",
                "likesDogFood": True,
                "Name": "Fido"
            },{
                "dType": "cat",
                "likesMice": False,
                "dislikes": {
                    "dType": "dog",
                    "likesDogFood": True,
                    "Name": "Angry"
                },
                "Name": "Felix"
            },{
                "dType": "siamese",
                "Color": "grey",
                "likesMice": True,
                "Name": "Finch"
            }]
        }

        self.d.dependencies = {
            'Zoo':Zoo, 'Animal':Animal, 'Dog':Dog,
             'Cat':Cat, 'Siamese':Siamese}

        zoo = self.d(Zoo, message)
        animals = [a for a in zoo.animals]

        self.assertEqual(len(animals), 3)
        self.assertIsInstance(animals[0], Dog)
        self.assertTrue(animals[0].likes_dog_food)
        self.assertEqual(animals[0].name, message['Animals'][0]["Name"])

        self.assertIsInstance(animals[1], Cat)
        self.assertFalse(animals[1].likes_mice)
        self.assertIsInstance(animals[1].dislikes, Dog)
        self.assertEqual(animals[1].dislikes.name, message['Animals'][1]["dislikes"]["Name"])
        self.assertEqual(animals[1].name, message['Animals'][1]["Name"])

        self.assertIsInstance(animals[2], Siamese)
        self.assertEqual(animals[2].color, message['Animals'][2]["Color"])
        self.assertTrue(animals[2].likes_mice)

        message = {
            "Name": "Didier",
            "dType": "Animal"
        }
        animal = self.d(Animal, message)
        self.assertIsInstance(animal, Animal)
        self.assertEqual(animal.name, "Didier")

    @unittest.skipIf(sys.version_info < (3,4), "assertLogs not supported before 3.4")
    def test_polymorphic_missing_info(self):
        class Animal(Model):

            _attribute_map = {
                "name":{"key":"Name", "type":"str"},
                "d_type":{"key":"dType", "type":"str"}
            }

            _subtype_map = {
                'd_type': {}
            }

            def __init__(self, name=None):
                self.name = name

        message = {
            "Name": "Didier"
        }
        with self.assertLogs('storage_models.serialization', level="WARNING"):
            animal = self.d(Animal, message)
        self.assertEqual(animal.name, "Didier")

        message = {
            "dType": "Penguin",
            "likesDogFood": True,
            "Name": "Fido"
        }
        with self.assertLogs('storage_models.serialization', level="WARNING"):
            animal = self.d(Animal, message)
        self.assertEqual(animal.name, "Fido")

    def test_polymorphic_deserialization_with_escape(self):

        class Animal(Model):

            _attribute_map = {
                "name":{"key":"Name", "type":"str"},
                "d_type":{"key":"odata\\.type", "type":"str"}
            }

            _subtype_map = {
                'd_type': {"dog":"Dog"}
            }

            def __init__(self, name=None):
                self.name = name

        class Dog(Animal):

            _attribute_map = {
                "name":{"key":"Name", "type":"str"},
                "likes_dog_food":{"key":"likesDogFood","type":"bool"},
                "d_type":{"key":"odata\\.type", "type":"str"}
                }

            def __init__(self, name=None, likes_dog_food=None):
                self.likes_dog_food = likes_dog_food
                super(Dog, self).__init__(name)
                self.d_type = 'dog'

        message = {
            "odata.type": "dog",
            "likesDogFood": True,
            "Name": "Fido"
            }

        self.d.dependencies = {
            'Animal':Animal, 'Dog':Dog}

        animal = self.d('Animal', message)

        self.assertIsInstance(animal, Dog)
        self.assertTrue(animal.likes_dog_food)

    def test_additional_properties(self):

        class AdditionalTest(Model):

            _attribute_map = {
                "name": {"key":"Name", "type":"str"},
                "display_name": {"key":"DisplayName", "type":"str"},
                'additional_properties': {'key': '', 'type': '{object}'}
            }

        message = {
            "Name": "test",
            "DisplayName": "diplay_name",
            "PropInt": 2,
            "PropStr": "AdditionalProperty",
            "PropArray": [1,2,3],
            "PropDict": {"a": "b"}
        }

        d = Deserializer({'AdditionalTest': AdditionalTest})

        m = d('AdditionalTest', message)

        self.assertEqual(m.name, "test")
        self.assertEqual(m.display_name, "diplay_name")
        self.assertEqual(m.additional_properties['PropInt'], 2)
        self.assertEqual(m.additional_properties['PropStr'], "AdditionalProperty")
        self.assertEqual(m.additional_properties['PropArray'], [1,2,3])
        self.assertEqual(m.additional_properties['PropDict'], {"a": "b"})

    def test_additional_properties_declared(self):

        class AdditionalTest(Model):

            _attribute_map = {
                "name": {"key":"Name", "type":"str"},
                'additional_properties': {'key': 'AddProp', 'type': '{object}'}
            }

            def __init__(self, name=None, additional_properties=None):
                self.name = name
                self.additional_properties = additional_properties

        message = {
            "Name": "test",
            "AddProp": {
                "PropInt": 2,
                "PropStr": "AdditionalProperty",
                "PropArray": [1,2,3],
                "PropDict": {"a": "b"}
            }
        }

        d = Deserializer({'AdditionalTest': AdditionalTest})

        m = d('AdditionalTest', message)

        self.assertEqual(m.name, "test")
        self.assertEqual(m.additional_properties['PropInt'], 2)
        self.assertEqual(m.additional_properties['PropStr'], "AdditionalProperty")
        self.assertEqual(m.additional_properties['PropArray'], [1,2,3])
        self.assertEqual(m.additional_properties['PropDict'], {"a": "b"})


    def test_additional_properties_not_configured(self):

        class AdditionalTest(Model):

            _attribute_map = {
                "name": {"key":"Name", "type":"str"}
            }

            def __init__(self, name=None):
                self.name = name

        message = {
            "Name": "test",
            "PropInt": 2,
            "PropStr": "AdditionalProperty",
            "PropArray": [1,2,3],
            "PropDict": {"a": "b"}
        }

        d = Deserializer({'AdditionalTest': AdditionalTest})

        m = d('AdditionalTest', message)

        self.assertEqual(m.name, "test")
        self.assertEqual(m.additional_properties['PropInt'], 2)
        self.assertEqual(m.additional_properties['PropStr'], "AdditionalProperty")
        self.assertEqual(m.additional_properties['PropArray'], [1,2,3])
        self.assertEqual(m.additional_properties['PropDict'], {"a": "b"})

    def test_additional_properties_flattening(self):

        class AdditionalTest(Model):

            _attribute_map = {
                "name": {"key":"Name", "type":"str"},
                "content" :{"key":"Properties.Content", "type":"str"}
            }

            def __init__(self, name=None, content=None):
                super(AdditionalTest, self).__init__()
                self.name = name
                self.content = content

        message = {
            "Name": "test",
            "Properties": {
                "Content": "Content",
                "Unknown": "Unknown"
            }
        }

        d = Deserializer({'AdditionalTest': AdditionalTest})

        m = d('AdditionalTest', message)

        self.assertEqual(m.name, "test")
        self.assertEqual(m.content, "Content")
        self.assertEqual(m.additional_properties, {})

    def test_attr_enum(self):
        """
        Test deserializing with Enum.
        """

        test_obj = type("TestEnumObj", (Model,), {"_attribute_map":None})
        test_obj._attribute_map = {
            "abc":{"key":"ABC", "type":"TestEnum"}
        }
        class TestEnum(Enum):
            val = "Value"

        deserializer = Deserializer({
            'TestEnumObj': test_obj,
            'TestEnum': TestEnum
        })

        obj = deserializer('TestEnumObj', {
            'ABC': 'Value'
        })

        self.assertEqual(obj.abc, TestEnum.val)

        obj = deserializer('TestEnumObj', {
            'ABC': 'azerty'
        })

        self.assertEqual(obj.abc, 'azerty')

        class TestEnum2(Enum):
            val2 = "Value"

        deserializer = Deserializer({
            'TestEnumObj': test_obj,
            'TestEnum': TestEnum,
            'TestEnum2': TestEnum2
        })

        obj = deserializer('TestEnumObj', {
            'ABC': TestEnum2.val2
        })
        self.assertEqual(obj.abc, TestEnum.val)

    def test_long_as_type_object(self):
        """Test irrelevant on Python 3. But still doing it to test regression.
            https://github.com/Azure/msrest-for-python/pull/121
        """

        try:
            long_type = long
        except NameError:
            long_type = int


        class TestModel(Model):
            _attribute_map = {'data': {'key': 'data', 'type': 'object'}}

        m = TestModel.deserialize({'data': {'id': long_type(1)}})
        assert m.data['id'] == long_type(1)

    def test_failsafe_deserialization(self):
        class Error(Model):

            _attribute_map = {
                "status": {"key": "status", "type": "int"},
                "message": {"key": "message", "type": "str"},
            }

            def __init__(self, **kwargs):
                super(Error, self).__init__(**kwargs)
                self.status = kwargs.get("status", None)
                self.message = kwargs.get("message", None)


        with pytest.raises(DeserializationError):
            self.d(Error, json.dumps(''), 'text/html')

        # should fail
        deserialized = self.d.failsafe_deserialize(Error, json.dumps(''), 'text/html')
        assert deserialized is None

        # should not fail
        error = {"status": 400, "message": "should deserialize"}
        deserialized = self.d.failsafe_deserialize(Error, json.dumps(error), 'application/json')
        assert deserialized.status == 400
        assert deserialized.message == "should deserialize"

class TestModelInstanceEquality(unittest.TestCase):

    def test_model_instance_equality(self):

        class Animal(Model):

            _attribute_map = {
                "name":{"key":"Name", "type":"str"},
            }

            def __init__(self, name=None):
                self.name = name

        animal1 = Animal('a1')
        animal2 = Animal('a2')
        animal3 = Animal('a1')
        self.assertTrue(animal1!=animal2)
        self.assertTrue(animal1==animal3)

class TestAzureCoreExceptions(unittest.TestCase):

    def test_azure_core_exceptions(self):
        self.assertEqual(SerializationError, AzureCoreSerializationError)
        self.assertEqual(DeserializationError, AzureCoreDeserializationError)

if __name__ == '__main__':
    unittest.main()
