# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from io import BytesIO, IOBase
import json
import sys
from typing import Any, Union
import uuid

from ._model_base import Model, SdkJSONEncoder

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports


class NamedBytesIO(BytesIO):
    def __init__(self, name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name


def multipart_file(file: Union[IOBase, bytes]) -> IOBase:
    if isinstance(file, IOBase):
        return file
    return NamedBytesIO("auto-name-" + str(uuid.uuid4()), file)


def multipart_data(data: Any) -> Any:
    if isinstance(data, (list, tuple, dict, Model)):
        return json.dumps(data, cls=SdkJSONEncoder, exclude_readonly=True)
    return data


def handle_multipart_form_data_model(body: Model) -> MutableMapping[str, Any]:  # pylint: disable=unsubscriptable-object
    """handle first layer of model.
    If its value is bytes or IO, replace it with raw value instead of serialized value.

    :param body: The model to handle.
    :type body: ~payload.multipart._model_base.Model
    :return: The handled model.
    :rtype: MutableMapping[str, Any]
    """
    result = body.as_dict()
    rest_name_attr = {v._rest_name: k for k, v in body._attr_to_rest_field.items()}  # pylint: disable=protected-access
    for rest_name in result.keys():
        attr = rest_name_attr.get(rest_name)
        if attr is not None:
            raw_value = getattr(body, attr, None)
            if isinstance(raw_value, (bytes, IOBase)):
                result[rest_name] = raw_value
    return result
