# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------
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
# --------------------------------------------------------------------------
import decimal
from decimal import Decimal
import sys
import json
import isodate
import logging
import pickle
from enum import Enum
from datetime import datetime, timedelta, date, time
import unittest
from typing import Any

import xml.etree.ElementTree as ET

from requests import Response

from storage_models.serialization import (
    Model,
    last_restapi_key_transformer,
    full_restapi_key_transformer,
    rest_key_extractor,
)
from storage_models.serialization import Serializer, Deserializer, RawDeserializer

# from azure.core.exceptions import ValidationError
from azure.core.exceptions import SerializationError, DeserializationError
from azure.core.exceptions import (
    SerializationError as AzureCoreSerializationError,
    DeserializationError as AzureCoreDeserializationError,
)
from azure.core.serialization import NULL as CoreNull

import storage_models

import pytest
import os
from pathlib import Path

FILE_DIR = Path(os.path.dirname(__file__))


class TestPolymorphicDeserialization():
    class Fish(Model):
        _validation = {
            "age": {"required": True},
            "kind": {"required": True},
        }
        _attribute_map = {
            "age": {"key": "age", "type": "int"},
            "kind": {"key": "kind", "type": "str"},
        }
        _subtype_map = {
            "kind": {
                "shark": "Shark",
                "salmon": "Salmon",
            }
        }

        def __init__(self, *, age: int, **kwargs: Any) -> None:
            super().__init__(**kwargs)
            self.age = age
            self.kind = None

    class Salmon(Fish):
        _validation = {
            "age": {"required": True},
            "kind": {"required": True},
        }
        _attribute_map = {
            "age": {"key": "age", "type": "int"},
            "kind": {"key": "kind", "type": "str"},
            "friends": {"key": "friends", "type": "[Fish]"},
            "partner": {"key": "partner", "type": "Fish"},
            "hate": {"key": "hate", "type": "{object}"},
        }

        def __init__(self, *, age: int, friends, partner, hate, **kwargs: Any) -> None:
            super().__init__(age=age, **kwargs)
            self.friends = friends
            self.partner = partner
            self.hate = hate
            self.kind = "salmon"

    class Shark(Fish):
        _validation = {
            "age": {"required": True},
            "kind": {"required": True},
            "sharktype": {"required": True},
        }
        _attribute_map = {
            "age": {"key": "age", "type": "int"},
            "kind": {"key": "kind", "type": "str"},
            "sharktype": {"key": "sharktype", "type": "str"},
        }
        _subtype_map = {
            "sharktype": {
                "saw": "SawShark",
                "goblin": "GoblinShark",
            }
        }

        def __init__(self, *, age: int, **kwargs: Any) -> None:
            super().__init__(age=age, **kwargs)
            self.kind = "shark"
            self.sharktype = None

    class SawShark(Shark):
        _validation = {
            "age": {"required": True},
            "kind": {"required": True},
            "sharktype": {"required": True},
        }
        _attribute_map = {
            "age": {"key": "age", "type": "int"},
            "kind": {"key": "kind", "type": "str"},
            "sharktype": {"key": "sharktype", "type": "str"},
        }

        def __init__(self, *, age: int, **kwargs: Any) -> None:
            super().__init__(age=age, **kwargs)
            self.sharktype = "saw"

    class GoblinShark(Shark):
        _validation = {
            "age": {"required": True},
            "kind": {"required": True},
            "sharktype": {"required": True},
        }
        _attribute_map = {
            "age": {"key": "age", "type": "int"},
            "kind": {"key": "kind", "type": "str"},
            "sharktype": {"key": "sharktype", "type": "str"},
        }

        def __init__(self, *, age: int, **kwargs: Any) -> None:
            super().__init__(age=age, **kwargs)
            self.sharktype = "goblin"

    def setUp(self):
        self.d = Deserializer(
            {
                "Fish": self.Fish,
                "Salmon": self.Salmon,
                "Shark": self.Shark,
                "SawShark": self.SawShark,
                "GoblinShark": self.GoblinShark,
            }
        )

    def _json_data(self):
        with open(FILE_DIR / "data/nested_polymorphic.json", "r") as f:
            return json.load(f)
        
    def assertEqual(self, a, b):
        assert a == b

    def _check_result(self, fish):
        self.assertEqual(fish.age, 1)
        self.assertEqual(fish.kind, "salmon")
        self.assertEqual(fish.partner.kind, "shark")
        self.assertEqual(fish.partner.sharktype, "saw")
        self.assertEqual(fish.partner.age, 2)
        self.assertEqual(fish.friends[0].age, 2)
        self.assertEqual(fish.friends[0].kind, "salmon")
        self.assertEqual(fish.friends[0].partner.age, 3)
        self.assertEqual(fish.friends[0].partner.kind, "salmon")
        self.assertEqual(fish.friends[0].hate["keys1"], {"age": 4, "kind": "salmon"})
        self.assertEqual(fish.friends[0].hate["keys2"], {"age": 2, "kind": "shark", "sharktype": "goblin"})
        self.assertEqual(fish.friends[1].age, 3)
        self.assertEqual(fish.friends[1].kind, "shark")
        self.assertEqual(fish.friends[1].sharktype, "goblin")

        self.assertEqual(fish.hate["keys3"], {"age": 3, "kind": "shark", "sharktype": "saw"})
        self.assertEqual(
            fish.hate["keys4"],
            {
                "age": 2,
                "kind": "salmon",
                "friends": [{"age": 1, "kind": "salmon"}, {"age": 4, "kind": "shark", "sharktype": "goblin"}],
            },
        )
    def _check_original_data(self, data):
        self.assertEqual(data["kind"], "salmon")
        self.assertEqual(data["partner"]["kind"], "shark")


    def test_nested_polymorphic_deserialization(self):
        json_data = self._json_data()
        fish = self.d._deserialize("Fish", json_data)
        self._check_result(fish)
        # self._check_original_data(json_data)


x = TestPolymorphicDeserialization()
x.setUp()
x.test_nested_polymorphic_deserialization()
