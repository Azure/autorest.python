# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Any, Dict, List
from .. import YamlUpdatePlugin
from .._utils import parse_args

_LOGGER = logging.getLogger(__name__)

OAUTH_TYPE = "OAuth2"
KEY_TYPE = "Key"


def get_azure_key_credential(key: str) -> Dict[str, Any]:
    return {
        "type": KEY_TYPE,
        "policy": {"type": "AzureKeyCredentialPolicy", "key": key},
    }


class CadlFlags(YamlUpdatePlugin):  # pylint: disable=abstract-method
    """A plugin to apply flags from backdoor python.json into cadl yaml file"""

    def update_yaml(self, yaml_data: Dict[str, Any]) -> None:
        """Convert in place the YAML str."""
        if self.options.get("add-credential"):
            self.update_credential(yaml_data)
        if self.options.get("namespace"):
            yaml_data["client"]["namespace"] = self.options["namespace"]
        if self.options.get("title"):
            yaml_data["client"]["name"] = self.options["title"]

    def get_credential_scopes_from_flags(self, auth_policy: str) -> List[str]:
        if self.options.get("azure-arm"):
            return ["https://management.azure.com/.default"]
        credential_scopes_temp = self.options.get("credential-scopes")
        credential_scopes = (
            credential_scopes_temp.split(",") if credential_scopes_temp else None
        )
        if self.options.get("credential-scopes", False) and not credential_scopes:
            raise ValueError(
                "--credential-scopes takes a list of scopes in comma separated format. "
                "For example: --credential-scopes=https://cognitiveservices.azure.com/.default"
            )
        if not credential_scopes:
            _LOGGER.warning(
                "You have default credential policy %s "
                "but not the --credential-scopes flag set while generating non-management plane code. "
                "This is not recommend because it forces the customer to pass credential scopes "
                "through kwargs if they want to authenticate.",
                auth_policy,
            )
            credential_scopes = []
        return credential_scopes

    def get_token_credential(self, credential_scopes: List[str]) -> Dict[str, Any]:
        return {
            "type": OAUTH_TYPE,
            "policy": {
                "type": "ARMChallengeAuthenticationPolicy"
                if self.options.get("azure-arm")
                else "BearerTokenCredentialPolicy",
                "credentialScopes": credential_scopes,
            },
        }

    def update_credential_from_flags(self) -> Dict[str, Any]:
        default_auth_policy = (
            "ARMChallengeAuthenticationPolicy"
            if self.options.get("azure-arm")
            else "BearerTokenCredentialPolicy"
        )
        auth_policy = (
            self.options.get("credential-default-policy-type") or default_auth_policy
        )
        credential_scopes = self.get_credential_scopes_from_flags(auth_policy)
        key = self.options.get("credential-key-header-name")
        if auth_policy.lower() in (
            "armchallengeauthenticationpolicy",
            "bearertokencredentialpolicy",
        ):
            if key:
                raise ValueError(
                    "You have passed in a credential key header name with default credential policy type "
                    f"{auth_policy}. This is not allowed, since credential key header "
                    "name is tied with AzureKeyCredentialPolicy. Instead, with this policy it is recommend you "
                    "pass in --credential-scopes."
                )
            return self.get_token_credential(credential_scopes)
        # Otherwise you have AzureKeyCredentialPolicy
        if self.options.get("credential-scopes"):
            raise ValueError(
                "You have passed in credential scopes with default credential policy type "
                "AzureKeyCredentialPolicy. This is not allowed, since credential scopes is tied with "
                f"{default_auth_policy}. Instead, with this policy "
                "you must pass in --credential-key-header-name."
            )
        if not key:
            key = "api-key"
            _LOGGER.info(
                "Defaulting the AzureKeyCredentialPolicy header's name to 'api-key'"
            )
        return get_azure_key_credential(key)

    def update_credential(self, yaml_data: Dict[str, Any]) -> None:
        credential_type = self.update_credential_from_flags()
        yaml_data["types"].append(credential_type)
        credential = {
            "type": credential_type,
            "optional": False,
            "description": "Credential needed for the client to connect to Azure.",
            "clientName": "credential",
            "location": "other",
            "restApiName": "credential",
            "implementation": "Client",
            "skipUrlEncoding": True,
            "inOverload": False,
        }
        yaml_data["client"]["parameters"].append(credential)


if __name__ == "__main__":
    # CADL pipeline will call this
    args = parse_args()
    CadlFlags(output_folder=args.output_folder, cadl_file=args.cadl_file).process()
