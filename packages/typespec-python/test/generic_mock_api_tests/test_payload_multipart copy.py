# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from io import IOBase
import pytest
from payload.multipart import MultiPartClient, models
from pathlib import Path
import sys
import logging
from typing import Any, MutableMapping
import base64

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    stream=sys.stdout)
FILE = Path(__file__).parent / Path("data/image.jpg")

JSON = MutableMapping[str, Any]


with open(str(FILE), "rb") as f:
    client = MultiPartClient(logging_enable=True)
    m = models.MultiPartRequest(id="123", profile_image=f.read())
    client.basic(m)
#     # client.basic({"id": "123", "profileImage": f.read()})
#     print(isinstance(f, IOBase))

    # content = f.read()
    # x = models.MultiPartRequest(profile_image=content)
    # assert x.profile_image == content
    # assert x["profileImage"] == base64.b64encode(content).decode()


