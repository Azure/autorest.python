# Azure Mgmt Test client library for Python
<!-- write necessary description of service -->

## Getting started

### Install the package

```bash
python -m pip install azure-mgmt-test
```

#### Prequisites

- Python 3.9 or later is required to use this package.
- You need an [Azure subscription][azure_sub] to use this package.
- An existing Azure Mgmt Test instance.

#### Create with an Azure Active Directory Credential
To use an [Azure Active Directory (AAD) token credential][authenticate_with_token],
provide an instance of the desired credential type obtained from the
[azure-identity][azure_identity_credentials] library.

To authenticate with AAD, you must first [pip][pip] install [`azure-identity`][azure_identity_pip]

After setup, you can choose which type of [credential][azure_identity_credentials] from azure.identity to use.
As an example, [DefaultAzureCredential][default_azure_credential] can be used to authenticate the client:

Set the values of the client ID, tenant ID, and client secret of the AAD application as environment variables:
`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_CLIENT_SECRET`

Use the returned token credential to authenticate the client:

```python
>>> from azure.mgmt.test import AutoRestSwaggerBATArrayService
>>> from azure.identity import DefaultAzureCredential
>>> client = AutoRestSwaggerBATArrayService(endpoint='<endpoint>', credential=DefaultAzureCredential())
```

## Examples

```python
>>> from azure.mgmt.test import AutoRestSwaggerBATArrayService
>>> from azure.identity import DefaultAzureCredential
>>> from azure.core.exceptions import HttpResponseError

>>> client = AutoRestSwaggerBATArrayService(endpoint='<endpoint>', credential=DefaultAzureCredential())
>>> try:
        <!-- write test code here -->
    except HttpResponseError as e:
        print('service responds error: {}'.format(e.response.json()))

```

## Contributing

This project welcomes contributions and suggestions. Most contributions require
you to agree to a Contributor License Agreement (CLA) declaring that you have
the right to, and actually do, grant us the rights to use your contribution.
For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether
you need to provide a CLA and decorate the PR appropriately (e.g., label,
comment). Simply follow the instructions provided by the bot. You will only
need to do this once across all repos using our CLA.

This project has adopted the
[Microsoft Open Source Code of Conduct][code_of_conduct]. For more information,
see the Code of Conduct FAQ or contact opencode@microsoft.com with any
additional questions or comments.

<!-- LINKS -->
[code_of_conduct]: https://opensource.microsoft.com/codeofconduct/
[authenticate_with_token]: https://docs.microsoft.com/azure/cognitive-services/authentication?tabs=powershell#authenticate-with-an-authentication-token
[azure_identity_credentials]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity#credentials
[azure_identity_pip]: https://pypi.org/project/azure-identity/
[default_azure_credential]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity#defaultazurecredential
[pip]: https://pypi.org/project/pip/
[azure_sub]: https://azure.microsoft.com/free/
