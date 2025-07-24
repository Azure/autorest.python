# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------


def test_patch_mixin_operation_group_in_operations_folder():
    from authentication.apikey import ApiKeyClient, aio

    assert hasattr(ApiKeyClient, "patch_added_operation")
    assert hasattr(aio.ApiKeyClient, "patch_added_operation")
