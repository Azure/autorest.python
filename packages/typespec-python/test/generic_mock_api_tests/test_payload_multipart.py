# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import uuid
from typing import Dict, Any
from pathlib import Path
import pytest
from payload.multipart import MultiPartClient, models
from payload.multipart._model_base import Model

JPG = Path(__file__).parent / "data/image.jpg"
PNG = Path(__file__).parent / "data/image.png"


@pytest.fixture
def client():
    with MultiPartClient(endpoint="http://localhost:3000") as client:
        yield client


@pytest.mark.parametrize(
    "op_name,model_class,data,file,file_info",
    [
        ("basic", models.MultiPartRequest, {"id": "123"}, {"profileImage": JPG}, {}),
        (
            "multi_binary_parts",
            models.MultiBinaryPartsRequest,
            {},
            {"profileImage": JPG, "picture": PNG},
            {}
        ),
        (
            "multi_binary_parts",
            models.MultiBinaryPartsRequest,
            {},
            {"profileImage": JPG},
            {}
        ),
        (
            "json_part",
            models.JsonPartRequest,
            {"address": models.Address(city="X")},
            {"profileImage": JPG},
            {},
        ),
        (
            "json_array_parts",
            models.JsonArrayPartsRequest,
            {"previousAddresses": [models.Address(city="Y"), models.Address(city="Z")]},
            {"profileImage": JPG},
            {},
        ),
        (
            "binary_array_parts",
            models.BinaryArrayPartsRequest,
            {"id": "123"},
            {"pictures": [PNG, PNG]},
            {},
        ),
        (
            "complex",
            models.ComplexPartsRequest,
            {"id": "123", "previousAddresses": [models.Address(city="Y"), models.Address(city="Z")], "address": models.Address(city="X")},
            {"pictures": [PNG, PNG], "profileImage": JPG},
            {},
        ),
    ],
)
def test_multi_part(client: MultiPartClient, op_name, model_class, data, file, file_info):
    def add_info(file_path, is_bytes):
        file_content = open(str(file_path), "rb").read() if is_bytes else open(str(file_path), "rb")
        name = str(uuid.uuid4()) if file_info.get("file_name") is None else file_info.get("file_name")
        content_type = "application/octet-stream" if file_info.get("content_type") is None else file_info.get("content_type")
        return (name, file_content, content_type)
    def convert(is_bytes=False):
        files_part = {k: ([add_info(vi, is_bytes) for vi in v] if isinstance(v, list) else add_info(v, is_bytes)) for k, v in file.items()}
        files_part.update(data)
        return files_part
    op = getattr(client.form_data, op_name)
    # test bytes (raw dict)
    body = convert(True)
    op(body)

    # test io (raw dict)
    body = convert()
    op(body)

    # test io (model)
    body = convert()
    with pytest.raises(TypeError):
        # caused by deepcopy when DPG model init
        op(model_class(body))

def _test_sample_single_file(client: MultiPartClient):
    # Python SDK support several kinds of file format for multipart/form-data and users can choose any of them
    # 1. bytes
    client.form_data.basic({"id": "123", "profileImage": open(str(PNG), "rb").read()})

    # 2. file io
    client.form_data.basic({"id": "123", "profileImage": open(str(PNG), "rb")})

    # 3. file tuple (only set file name)
    client.form_data.basic({"id": "123", "profileImage": ("my_image.jpg", open(str(JPG), "rb"))})
    # or
    client.form_data.basic({"id": "123", "profileImage": ("my_image.jpg", open(str(JPG), "rb").read())})

    # 4. file tuple (set file name and content type)
    client.form_data.basic({"id": "123", "profileImage": ("my_image.jpg", open(str(JPG), "rb"), "image/jpeg")})
    # or
    client.form_data.basic({"id": "123", "profileImage": ("my_image.jpg", open(str(JPG), "rb").read(), "image/jpeg")})

def _test_sample_array_file(client: MultiPartClient):
    # If users want to upload array files for same field name, they can use list, and users can 
    # choose any of the above file format for each file. e.g. 

    # List[bytes, io]
    client.form_data.binary_array_parts({"id": "123", "pictures": [open(str(PNG), "rb").read(), open(str(PNG), "rb")]})

    # List[bytes, tuple]
    client.form_data.binary_array_parts({
        "id": "123", 
        "pictures": [open(str(PNG), "rb").read(), ("my_image.png", open(str(PNG), "rb"))]
    })
    # or
    client.form_data.binary_array_parts({
        "id": "123", 
        "pictures": [open(str(PNG), "rb").read(), ("my_image.png", open(str(PNG), "rb"), "image/png")]
    })
    # List[io, bytes]
    client.form_data.binary_array_parts({"id": "123", "pictures": [open(str(PNG), "rb"), open(str(PNG), "rb").read()]})

    # List[tuple, tuple]
    client.form_data.binary_array_parts({
        "id": "123", 
        "pictures": [("my_image1.png", open(str(PNG), "rb"), "image/png"), ("my_image2.png", open(str(PNG), "rb"), "image/png")]
    })
    # ...