import pytest
from azure.core.pipeline.policies import SansIOHTTPPolicy

@pytest.fixture
def credential():
    class FakeCredential:
        pass
    return FakeCredential()

@pytest.fixture
def authentication_policy():
    return SansIOHTTPPolicy()