# coding=utf-8
import os
import pytest
from dotenv import load_dotenv
from devtools_testutils import (
    test_proxy,
    add_general_regex_sanitizer,
    add_body_key_sanitizer,
    add_header_regex_sanitizer,
)

load_dotenv()


# For security, please avoid record sensitive identity information in recordings
@pytest.fixture(scope="session", autouse=True)
def add_sanitizers(test_proxy):
    a_subscription_id = os.environ.get("A_SUBSCRIPTION_ID", "00000000-0000-0000-0000-000000000000")
    a_tenant_id = os.environ.get("A_TENANT_ID", "00000000-0000-0000-0000-000000000000")
    a_client_id = os.environ.get("A_CLIENT_ID", "00000000-0000-0000-0000-000000000000")
    a_client_secret = os.environ.get("A_CLIENT_SECRET", "00000000-0000-0000-0000-000000000000")
    add_general_regex_sanitizer(regex=a_subscription_id, value="00000000-0000-0000-0000-000000000000")
    add_general_regex_sanitizer(regex=a_tenant_id, value="00000000-0000-0000-0000-000000000000")
    add_general_regex_sanitizer(regex=a_client_id, value="00000000-0000-0000-0000-000000000000")
    add_general_regex_sanitizer(regex=a_client_secret, value="00000000-0000-0000-0000-000000000000")

    b_subscription_id = os.environ.get("B_SUBSCRIPTION_ID", "00000000-0000-0000-0000-000000000000")
    b_tenant_id = os.environ.get("B_TENANT_ID", "00000000-0000-0000-0000-000000000000")
    b_client_id = os.environ.get("B_CLIENT_ID", "00000000-0000-0000-0000-000000000000")
    b_client_secret = os.environ.get("B_CLIENT_SECRET", "00000000-0000-0000-0000-000000000000")
    add_general_regex_sanitizer(regex=b_subscription_id, value="00000000-0000-0000-0000-000000000000")
    add_general_regex_sanitizer(regex=b_tenant_id, value="00000000-0000-0000-0000-000000000000")
    add_general_regex_sanitizer(regex=b_client_id, value="00000000-0000-0000-0000-000000000000")
    add_general_regex_sanitizer(regex=b_client_secret, value="00000000-0000-0000-0000-000000000000")

    add_header_regex_sanitizer(key="Set-Cookie", value="[set-cookie;]")
    add_header_regex_sanitizer(key="Cookie", value="cookie;")
    add_body_key_sanitizer(json_path="$..access_token", value="access_token")
