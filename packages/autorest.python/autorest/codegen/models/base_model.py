# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from .code_model import NamespaceModel


class BaseModel:
    """This is the base class for model representations that are based on some YAML data.

    :param yaml_data: the yaml data for this schema
    :type yaml_data: dict[str, Any]
    """

    def __init__(
        self, yaml_data: Dict[str, Any], namespace_model: "NamespaceModel"
    ) -> None:
        self.yaml_data = yaml_data
        self.namespace_model = namespace_model

    @property
    def id(self) -> int:
        return id(self.yaml_data)

    def __repr__(self):
        return f"<{self.__class__.__name__}>"
