# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
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
    "op_name,model_class,data,file",
    [
        ("basic", models.MultiPartRequest, {"id": "123"}, {"profileImage": JPG}),
        (
            "multi_binary_parts",
            models.MultiBinaryPartsRequest,
            {},
            {"profileImage": JPG, "picture": PNG},
        ),
        (
            "multi_binary_parts",
            models.MultiBinaryPartsRequest,
            {},
            {"profileImage": JPG},
        ),
    ],
)
async def test_multi_part(client: MultiPartClient, op_name, model_class, data, file):
    op = getattr(client.form_data, op_name)
    # test bytes
    body = {k: open(str(v), "rb").read() for k, v in file.items()}
    body.update(data)
    await op(body)
    await op(model_class(body))

    # test io
    body = {k: open(str(v), "rb") for k, v in file.items()}
    body.update(data)
    await op(body)

    body = {k: open(str(v), "rb") for k, v in file.items()}
    body.update(data)
    with pytest.raises(TypeError):
        # caused by deepcopy when DPG model init
        await op(model_class(body))
