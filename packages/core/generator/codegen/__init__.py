# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import yaml

from .models.sdk_package import SdkPackage
from .serializers import Serializer
from .. import Plugin

class CodegenPlugin(Plugin):
    
    def process(self) -> bool:
        yaml_data = yaml.safe_load(self.api.read(self.options["yamlFile"]))
        sdk_package = SdkPackage(yaml_data, self.options)
        serializer = Serializer(sdk_package, output_dir=self.options["outputDir"])
        serializer.serialize()
        return True
