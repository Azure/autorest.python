# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Set, Optional, Type
from .credential_schema_policy import CredentialSchemaPolicy, BearerTokenCredentialPolicy
from .credential_schema_policy import ARMChallengeAuthenticationPolicy
from .credential_schema import TokenCredentialSchema, AzureKeyCredentialSchema


class CredentialModel:
    """Store info about credential.
    """

    def __init__(
        self,
        azure_arm: bool
    ) -> None:
        self.azure_arm: bool = azure_arm
        self.credential_scopes: Set[str] = set()
        self.key_header_name: str = ""
        self.policy_type: Optional[Type[CredentialSchemaPolicy]] = None
        self._credential_schema_policy: Optional[CredentialSchemaPolicy] = None

    @staticmethod
    def aad_type() -> str:
        return "OAuth2"

    @staticmethod
    def key_type() -> str:
        return "key"

    @property
    def default_authentication_policy(self) -> Type[CredentialSchemaPolicy]:
        return ARMChallengeAuthenticationPolicy if self.azure_arm else BearerTokenCredentialPolicy

    @property
    def credential_schema_policy(self) -> CredentialSchemaPolicy:
        if not self._credential_schema_policy:
            raise ValueError(
                "You want to find the Credential Schema Policy, but have not given a value")
        return self._credential_schema_policy

    def build_authentication_policy(self):
        if hasattr(self.policy_type, "credential_scopes"):
            self._credential_schema_policy = self.policy_type( # pylint: disable=not-callable
                credential=TokenCredentialSchema(async_mode=False),
                credential_scopes=list(self.credential_scopes),
            )
        elif hasattr(self.policy_type, "credential_key_header_name"):
            self._credential_schema_policy = self.policy_type( # pylint: disable=not-callable
                credential=AzureKeyCredentialSchema(),
                credential_key_header_name=self.key_header_name
            )
