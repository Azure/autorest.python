# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from abc import abstractmethod
from typing import Optional
from .credential_schema import CredentialSchema

class CredentialSchemaPolicy:
    name: Optional[str] = None

    def __init__(self) -> None:
        self._credential = None

    @property
    def credential(self) -> CredentialSchema:
        if not self._credential:
            raise ValueError(
                "You have not initialized this policy with its credential yet"
            )
        return self._credential

    def initialize(self, credential, **kwargs):  # pylint: disable=unused-argument
        """Initialize your schema policy"""
        self._credential = credential

    @abstractmethod
    def call(self, async_mode: bool) -> str:
        ...


class BearerTokenCredentialPolicy(CredentialSchemaPolicy):
    name = "BearerTokenCredentialPolicy"

    def __init__(self) -> None:
        super().__init__()
        self.credential_scopes = None

    def initialize(self, credential, **kwargs):
        super().initialize(credential)
        self.credential_scopes = kwargs.pop("credential_scopes")

    def call(self, async_mode: bool) -> str:
        policy_name = f"Async{self.name}" if async_mode else self.name
        return f"policies.{policy_name}(self.credential, *self.credential_scopes, **kwargs)"


class AzureKeyCredentialPolicy(CredentialSchemaPolicy):
    name = "AzureKeyCredentialPolicy"

    def __init__(self) -> None:
        super().__init__()
        self.credential_key_header_name = None

    def initialize(self, credential, **kwargs):
        super().initialize(credential)
        self.credential_key_header_name = kwargs.pop("credential_key_header_name")

    def call(self, async_mode: bool) -> str:
        return f'policies.AzureKeyCredentialPolicy(self.credential, "{self.credential_key_header_name}", **kwargs)'

def get_credential_schema_policy(name):
    policies = [BearerTokenCredentialPolicy(), AzureKeyCredentialPolicy()]
    try:
        return next(p for p in policies if p.name.lower() == name.lower())
    except StopIteration:
        raise ValueError(
            "The credential policy you pass in with --credential-default-policy-type must be either "
            "{}".format(
                " or ".join([p.name for p in policies])
            )
        )
