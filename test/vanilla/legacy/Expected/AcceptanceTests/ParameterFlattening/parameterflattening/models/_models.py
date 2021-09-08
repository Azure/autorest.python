# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class AvailabilitySetUpdateParameters(msrest.serialization.Model):
    """AvailabilitySetUpdateParameters.

    All required parameters must be populated in order to send to Azure.

    :keyword tags: Required. A set of tags. A description about the set of tags.
    :paramtype tags: dict[str, str]
    """

    _validation = {
        "tags": {"required": True},
    }

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
    }

    def __init__(self, **kwargs):
        super(AvailabilitySetUpdateParameters, self).__init__(**kwargs)
        self.tags = kwargs["tags"]
