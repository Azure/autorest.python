# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from .serializers import MultiClientSerializer
from .models import CodeModel
from .. import Plugin

_LOGGER = logging.getLogger(__name__)


class MultiClientPlugin(Plugin):
    def process(self) -> bool:
        package_version: str = (
            self._autorestapi.get_value("package-version") or "1.0.0b1"
        )
        _LOGGER.info("Generating files for multi client")

        multiapi_serializer = MultiClientSerializer(
            autorestapi=self._autorestapi, code_model=CodeModel(package_version)
        )
        multiapi_serializer.serialize()

        _LOGGER.info("Generating Done for multi client!")
        return True
