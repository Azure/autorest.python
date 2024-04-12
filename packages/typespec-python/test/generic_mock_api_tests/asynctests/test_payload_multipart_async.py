# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import uuid
from typing import Dict, Any
from pathlib import Path
import pytest
from payload.multipart.aio import MultiPartClient
from payload.multipart import models
from payload.multipart._model_base import Model

JPG = Path(__file__).parent.parent / "data/image.jpg"
PNG = Path(__file__).parent.parent / "data/image.png"


@pytest.fixture
async def client():
    async with MultiPartClient(endpoint="http://localhost:3000") as client:
        yield client


@pytest.mark.asyncio
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
        (
            "check_file_name_and_content_type",
            models.MultiPartRequest,
            {"id": "123"},
            {"profileImage": JPG},
            {"content_type": "image/jpg", "file_name": "hello.jpg"},
        ),
        (
            "anonymous_model",
            dict,
            {},
            {"profileImage": JPG},
            {},
        ),
    ],
)
async def test_multi_part(client: MultiPartClient, op_name, model_class, data, file, file_info):
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
    await op(body)

    # test io (raw dict)
    body = convert()
    await op(body)

    # test io (model)
    body = convert()
    if issubclass(model_class, Model):
        # https://github.com/Azure/autorest.python/issues/2516
        with pytest.raises(TypeError):
            # caused by deepcopy when DPG model init
            await op(model_class(body))