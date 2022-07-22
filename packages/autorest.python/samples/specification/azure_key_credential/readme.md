# Sample Azure Key Credential Generation

Use the flags `--credential-default-policy-type` and `--credential-key-header-name` to specify you want your credential to be of type [`AzureKeyCredential`][azure_key_credential].

### Settings

``` yaml
input-file: ../../../node_modules/@microsoft.azure/autorest.testserver/swagger/head.json
namespace: azure.key.credential.sample
package-name: azure-key-credential-sample
license-header: MICROSOFT_MIT_NO_VERSION
credential-default-policy-type: AzureKeyCredentialPolicy
credential-key-header-name: Ocp-Apim-Subscription-Key
add-credential: true
package-version: 0.1.0
basic-setup-py: true
clear-output-folder: true
```

<!-- LINKS -->
[azure_key_credential]: https://docs.microsoft.com/python/api/azure-core/azure.core.credentials.azurekeycredential?view=azure-python
