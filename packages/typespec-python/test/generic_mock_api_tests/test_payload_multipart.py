# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from pathlib import Path
import pytest
from payload.multipart import MultiPartClient, models

FILE_FOLDER = Path(__file__).parent

@pytest.fixture
def client():
    with MultiPartClient(endpoint="http://localhost:3000") as client:
        yield client

def test_basic(client: MultiPartClient, jpg_data: bytes):
    # test bytes
    client.form_data.basic({"id": "123", "profileImage": jpg_data})
    client.form_data.basic(models.MultiPartRequest(id="123", profile_image=jpg_data))

    # test io
    with open(str(FILE_FOLDER / "data/image.jpg"), "rb") as jpg_data_io:
        client.form_data.basic({"id": "123", "profileImage": jpg_data_io})

    with open(str(FILE_FOLDER / "data/image.jpg"), "rb") as jpg_data_io:
        # caused by deepcopy when DPG model init
        with pytest.raises(TypeError):
            client.form_data.basic(models.MultiPartRequest(id="123", profile_image=jpg_data_io))
