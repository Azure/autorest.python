
# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import pytest
import importlib
import sys
import inspect

from dpgcustomizationinitialversiontolerant import DPGClient as DPGClientInitial
from dpgcustomizationcustomizedversiontolerant import DPGClient as DPGClientCustomized
from dpgcustomizationcustomizedversiontolerant.models import *

@pytest.fixture
def client(client_cls):
    with client_cls() as client:
        yield client

CLIENTS = [DPGClientInitial, DPGClientCustomized]

@pytest.mark.parametrize("client_cls", CLIENTS)
def test_get_raw_model(client):
    assert client.get_model(mode="raw") == {"received": "raw"}

@pytest.mark.parametrize("client_cls", [DPGClientCustomized])
def test_get_customized_model(client):
    assert client.get_model("model").received == "model"

@pytest.mark.parametrize("client_cls", CLIENTS)
def test_post_raw_model(client):
    assert client.post_model("raw", {"hello": "world!"})["received"] == "raw"

@pytest.mark.parametrize("client_cls", [DPGClientCustomized])
def test_post_customized_model(client):
    assert client.post_model("model", Input(hello="world!")).received == "model"

@pytest.mark.parametrize("client_cls", CLIENTS)
def test_get_raw_pages(client):
    assert list(client.get_pages("raw")) == [{'received': 'raw'}, {'received': 'raw'}]

@pytest.mark.parametrize("client_cls", [DPGClientCustomized])
def test_get_customized_pages(client):
    pages = list(client.get_pages("model"))
    assert all(p for p in pages if isinstance(p, Product))
    assert all(p for p in pages if p.received == "model")

@pytest.mark.parametrize("client_cls", CLIENTS)
def test_raw_lro(client):
    assert client.begin_lro(mode="raw").result() == {'provisioningState': 'Succeeded', 'received': 'raw'}

@pytest.mark.parametrize("client_cls", [DPGClientCustomized])
def test_customized_lro(client):
    product = client.begin_lro(mode="model").result()
    assert isinstance(product, LROProduct)
    assert product.received == "model"
    assert product.provisioning_state == "Succeeded"

@pytest.mark.parametrize("package_name", ["dpgcustomizationinitialversiontolerant", "dpgcustomizationcustomizedversiontolerant"])
def test_dunder_all(package_name):
    assert importlib.import_module(package_name).__all__ == ["DPGClient"]
    assert importlib.import_module(f"{package_name}._operations").__all__ == ["DPGClientOperationsMixin"]

def test_imports():
    # make sure we can import all of the models we've added to the customization class
    from dpgcustomizationcustomizedversiontolerant.models import (
        Input, LROProduct, Product
    )
    models = [Input, LROProduct, Product]
    # check public models
    public_models = [
        name for name, obj in
        inspect.getmembers(sys.modules["dpgcustomizationcustomizedversiontolerant.models"])
        if name[0] != "_" and obj in models
    ]
    assert len(public_models) == 3
