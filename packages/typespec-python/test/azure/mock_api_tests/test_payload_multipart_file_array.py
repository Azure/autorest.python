# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, Any
from pathlib import Path
import pytest
from payload.multipart import MultiPartClient, models
from payload.multipart._model_base import Model

JPG = Path(__file__).parent.parent.parent / "generic_mock_api_tests/data/image.jpg"
PNG = Path(__file__).parent.parent.parent / "generic_mock_api_tests/data/image.png"


@pytest.fixture
def client():
    with MultiPartClient(endpoint="http://localhost:3000") as client:
        yield client


# @pytest.mark.parametrize(
#     "op_name,model_class,data,file",
#     [
#         (
#             "binary_array_parts",
#             models.BinaryArrayPartsRequest,
#             {"id": "123"},
#             {"pictures": [PNG, PNG]},
#         ),
#         (
#             "complex",
#             models.ComplexPartsRequest,
#             {"id": "123", "previousAddresses": [models.Address(city="Y"), models.Address(city="Z")], "address": models.Address(city="X")},
#             {"pictures": [PNG, PNG], "profileImage": JPG},
#         )
#     ],
# )
# def test_multi_part(client: MultiPartClient, op_name, model_class, data, file):
#     file_bytes = lambda p: open(str(p), "rb").read()
#     op = getattr(client.form_data, op_name)
#     # test bytes
#     body = {k: ([file_bytes(vi) for vi in v] if isinstance(v, list) else file_bytes(v)) for k, v in file.items()}
#     body.update(data)
#     op(body)
#     op(model_class(body))

#     # test io
#     file_io = lambda p: open(str(p), "rb")
#     body = {k: ([file_io(vi) for vi in v] if isinstance(v, list) else file_io(v)) for k, v in file.items()}
#     body.update(data)
#     op(body)

#     body = {k: ([file_io(vi) for vi in v] if isinstance(v, list) else file_io(v)) for k, v in file.items()}
#     body.update(data)
#     with pytest.raises(TypeError):
#         # caused by deepcopy when DPG model init
#         op(model_class(body))

# def test_sample_single_file(client: MultiPartClient):
#     # Python SDK support several kinds of file format for multipart/form-data and users can choose any of them

#     # 1. bytes
#     client.form_data.basic(models.MultiPartRequest(id="123", profile_image=open(str(JPG), "rb").read()))

#     # 2. file io
#     client.form_data.basic({"id": "123", "profileImage": open(str(JPG), "rb")})

#     # 3. file tuple (only set file name)
#     client.form_data.basic({"id": "123", "profileImage": ("my_image.jpg", open(str(JPG), "rb"))})
#     # or
#     client.form_data.basic({"id": "123", "profileImage": ("my_image.jpg", open(str(JPG), "rb").read())})

#     # 4. file tuple (set file name and content type)
#     client.form_data.basic({"id": "123", "profileImage": ("my_image.jpg", open(str(JPG), "rb"), "image/jpeg")})
#     # or
#     client.form_data.basic({"id": "123", "profileImage": ("my_image.jpg", open(str(JPG), "rb").read(), "image/jpeg")})

# def test_sample_array_file(client: MultiPartClient):
#     # If users want to upload array files for same field name, they can use list, and users can 
#     # choose any of the above file format for each file. e.g. 

#     # List[bytes, io]
#     client.form_data.binary_array_parts({"id": "123", "pictures": [open(str(PNG), "rb").read(), open(str(PNG), "rb")]})

#     # List[bytes, tuple]
#     client.form_data.binary_array_parts({
#         "id": "123", 
#         "pictures": [open(str(PNG), "rb").read(), ("my_image.png", open(str(PNG), "rb"))]
#     })
#     # or
#     client.form_data.binary_array_parts({
#         "id": "123", 
#         "pictures": [open(str(PNG), "rb").read(), ("my_image.png", open(str(PNG), "rb"), "image/png")]
#     })
#     # List[io, bytes]
#     client.form_data.binary_array_parts({"id": "123", "pictures": [open(str(PNG), "rb"), open(str(PNG), "rb").read()]})

#     # List[tuple, tuple]
#     client.form_data.binary_array_parts({
#         "id": "123", 
#         "pictures": [("my_image1.png", open(str(PNG), "rb"), "image/png"), ("my_image2.png", open(str(PNG), "rb"), "image/png")]
#     })
#     # ...
