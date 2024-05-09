# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from ..models.sdk_package import SdkPackage


class Serializer:
    def __init__(self, sdk_package: SdkPackage, output_dir: str) -> None:
        self.sdk_package = sdk_package
        self.output_dir = output_dir

    def serialize(self) -> None:
        ...
