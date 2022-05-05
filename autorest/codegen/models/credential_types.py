# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from abc import abstractmethod
from typing import (
    Optional,
    Any,
    Dict,
    TYPE_CHECKING,
    List,
    Generic,
    TypeVar,
    Union,
    cast,
)

from .imports import FileImport, ImportType, TypingSection
from .base_type import BaseType

if TYPE_CHECKING:
    from .code_model import CodeModel


class _CredentialPolicyBaseType:
    """Base class for our different credential policy types.

    Inherited by our BearerTokenCredentialPolicy and AzureKeyCredentialPolicy types.
    """

    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel") -> None:
        self.yaml_data = yaml_data
        self.code_model = code_model

    @abstractmethod
    def call(self, async_mode: bool) -> str:
        """
        How to call this credential policy. Used to initialize the credential policy in the config file.
        """
        ...


class BearerTokenCredentialPolicyType(_CredentialPolicyBaseType):
    """Credential policy type representing BearerTokenCredentialPolicy"""

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        credential_scopes: List[str],
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.credential_scopes = credential_scopes

    def call(self, async_mode: bool) -> str:
        policy_name = f"{'Async' if async_mode else ''}BearerTokenCredentialPolicy"
        return f"policies.{policy_name}(self.credential, *self.credential_scopes, **kwargs)"

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "BearerTokenCredentialPolicyType":
        return cls(yaml_data, code_model, yaml_data["credentialScopes"])


class ARMChallengeAuthenticationPolicyType(BearerTokenCredentialPolicyType):
    """Credential policy type representing ARMChallengeAuthenticationPolicy"""

    def call(self, async_mode: bool) -> str:
        policy_name = f"{'Async' if async_mode else ''}ARMChallengeAuthenticationPolicy"
        return f"{policy_name}(self.credential, *self.credential_scopes, **kwargs)"


class AzureKeyCredentialPolicyType(_CredentialPolicyBaseType):
    def __init__(
        self, yaml_data: Dict[str, Any], code_model: "CodeModel", key: str
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.key = key

    def call(self, async_mode: bool) -> str:
        return f'policies.AzureKeyCredentialPolicy(self.credential, "{self.key}", **kwargs)'

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "AzureKeyCredentialPolicyType":
        return cls(yaml_data, code_model, yaml_data["key"])


CredentialPolicyType = TypeVar(
    "CredentialPolicyType",
    bound=Union[
        BearerTokenCredentialPolicyType,
        ARMChallengeAuthenticationPolicyType,
        AzureKeyCredentialPolicyType,
    ],
)


class CredentialType(
    BaseType, Generic[CredentialPolicyType]
):  # pylint:disable=abstract-method
    """Store info about the type of the credential. Can be either an AzureKeyCredential or a TokenCredential"""

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        policy: CredentialPolicyType,
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.policy = policy

    def description(
        self, *, is_operation_file: bool  # pylint: disable=unused-argument
    ) -> str:
        return ""

    def get_json_template_representation(
        self,
        *,
        optional: bool = True,
        client_default_value_declaration: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Any:
        raise TypeError(
            "You should not try to get a JSON template representation of a CredentialSchema"
        )

    @property
    def docstring_text(self) -> str:
        return "credential"

    @property
    def serialization_type(self) -> str:
        return self.docstring_type

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "CredentialType":
        from . import build_type

        return cls(
            yaml_data,
            code_model,
            policy=cast(
                CredentialPolicyType, build_type(yaml_data["policy"], code_model)
            ),
        )


class TokenCredentialType(
    CredentialType[  # pylint: disable=unsubscriptable-object
        Union[BearerTokenCredentialPolicyType, ARMChallengeAuthenticationPolicyType]
    ]
):
    """Type of a token credential. Used by BearerAuth and ARMChallenge policies"""

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        policy: Union[
            BearerTokenCredentialPolicyType, ARMChallengeAuthenticationPolicyType
        ],
        async_mode: bool = False,
    ) -> None:
        super().__init__(yaml_data, code_model, policy)
        self.async_mode = async_mode
        self._async_type = "~azure.core.credentials_async.AsyncTokenCredential"
        self._sync_type = "~azure.core.credentials.TokenCredential"

    def type_annotation(
        self, *, is_operation_file: bool = False  # pylint: disable=unused-argument
    ) -> str:
        if self.async_mode:
            return '"AsyncTokenCredential"'
        return '"TokenCredential"'

    @property
    def docstring_type(self) -> str:
        if self.async_mode:
            return self._async_type
        return self._sync_type

    def imports(
        self, *, is_operation_file: bool  # pylint: disable=unused-argument
    ) -> FileImport:
        file_import = FileImport()
        if self.async_mode:
            file_import.add_submodule_import(
                "azure.core.credentials_async",
                "AsyncTokenCredential",
                ImportType.AZURECORE,
                typing_section=TypingSection.TYPING,
            )
        else:
            file_import.add_submodule_import(
                "azure.core.credentials",
                "TokenCredential",
                ImportType.AZURECORE,
                typing_section=TypingSection.TYPING,
            )
        return file_import

    @property
    def instance_check_template(self) -> str:
        return "hasattr({}, get_token)"


class AzureKeyCredentialType(
    # pylint: disable=unsubscriptable-object
    CredentialType[AzureKeyCredentialPolicyType]
):
    """Type for an AzureKeyCredential"""

    @property
    def docstring_type(self) -> str:
        return "~azure.core.credentials.AzureKeyCredential"

    def type_annotation(  # pylint: disable=no-self-use
        self, *, is_operation_file: bool = False  # pylint: disable=unused-argument
    ) -> str:
        return "AzureKeyCredential"

    @property
    def instance_check_template(self) -> str:
        return "isinstance({}, AzureKeyCredential)"

    def imports(  # pylint: disable=no-self-use
        self, *, is_operation_file: bool  # pylint: disable=unused-argument
    ) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import(
            "azure.core.credentials",
            "AzureKeyCredential",
            ImportType.AZURECORE,
            typing_section=TypingSection.CONDITIONAL,
        )
        return file_import
