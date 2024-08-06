# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import copy
import decimal
import json
import datetime
from pathlib import Path
import random
from typing import (
    Any,
    Iterable,
    List,
    Literal,
    Dict,
    Mapping,
    Sequence,
    Set,
    Tuple,
    Optional,
    overload,
    Union,
)
import pytest
import isodate
import sys
from enum import Enum

from specialwords._model_base import (
    SdkJSONEncoder,
    Model,
    rest_field,
    _is_model,
    rest_discriminator,
    _deserialize,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class MyEnum(Enum):
    A = "a"
    B = "b"


class ComplicatedModel(Model):
    basic_value: int = rest_field(name="basicValue")
    datetime_value: datetime.datetime = rest_field(name="datetimeValue")
    duration_value: datetime.timedelta = rest_field(name="durationValue")
    enum_value: "MyEnum" = rest_field(name="enumValue")
    model_value: "BasicModel" = rest_field(name="modelValue")
    list_value: List[int] = rest_field(name="listValue")
    dict_value: Dict[str, int] = rest_field(name="dictValue")
    list_model: List["BasicModel"] = rest_field(name="listModel")
    dict_model: Dict[str, "BasicModel"] = rest_field(name="dictModel")
    nested_model: "ComplicatedModel" = rest_field(name="nestedModel")


class BasicModel(Model):
    int_value: int = rest_field(name="intValue")
    string_value: str = rest_field(name="stringValue")
    float_value: float = rest_field(name="floatValue")
    bool_value: bool = rest_field(name="boolValue")


def test_model_deserialize_benchmark(benchmark):
    benchmark.pedantic(test_model_deserialize, iterations=10, rounds=10)


def test_model_deserialize():
    content = json.load(open("large_test_data.json"))
    model = ComplicatedModel(content)
    assert model


def generate_large_data_json_file():
    def generate_basic_model():
        return BasicModel(
            int_value=random.randint(0, 100000),
            string_value="".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=1000)),
            float_value=random.uniform(0, 100000),
            bool_value=random.choice([True, False]),
        )

    def generate_complicated_model():
        complicated_model_instance = ComplicatedModel(
            basic_value=100,
            datetime_value=datetime.datetime.now(),
            duration_value=datetime.timedelta(days=1, seconds=3600),
            enum_value=MyEnum.A,
            model_value=generate_basic_model(),
            list_value=[i for i in range(1000)],  # Large list of integers
            dict_value={f"key_{i}": i for i in range(1000)},  # Large dictionary
            list_model=[generate_basic_model() for _ in range(2000)],  # Large list of BasicModel
            dict_model={f"key_{i}": generate_basic_model() for i in range(2000)},  # Large dictionary of BasicModel
        )

        nested_model_instance = complicated_model_instance.copy()
        complicated_model_instance.nested_model = nested_model_instance

        return complicated_model_instance

    large_data = generate_complicated_model()

    json_data = json.dumps(large_data, cls=SdkJSONEncoder)

    with open("large_test_data.json", "w") as json_file:
        json_file.write(json_data)

    file_size = len(json_data.encode('utf-8'))
    print(f"Generated JSON size: {file_size / (1024 * 1024):.2f} MB")


if __name__ == "__main__":
    pytest.main([__file__])
    # generate_large_data_json_file()
