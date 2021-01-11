# <img align="center" src="../images/logo.png">  Initializing Your Python Client

The first step to using your generated client in code is to import and initialize your client. Our SDKs are modelled such
that the client is the main point of access to the generated code.

## Importing Your Client

You import your client from the namespace specified when generating (under flag `--namespace`). For the sake of this example,
let's say the namespace is `azure.pets`. Your client's name is detailed in the swagger, (TODO link to swagger docs), and let's say
ours is called `PetsClient`.

Putting this together, we import our client like so:

```python
from azure.pets import PetsClient
```

## Minimum Dependencies of Your Client

The only scenario the generated code can force dependencies is if you generate with a `setup.py` file using the `--basic-setup-py` flag.
The following are core libraries your generated code depend on, and the minimum version we highly recommend:

| Library | Description | Min Version
|------------------|-------------|-------------
|[`azure-core`][azure_core_library]|The most important library to have installed. It provides shared exceptions and modules for all the Python SDK client libraries.|1.8.2
|[`msrest`][msrest_library]|Library mainly used for serializing and deserializing objects|0.6.18
|[`azure-mgmt-core`][azure_mgmt_core_library]|Required if you're generating mgmt plane code (see `--azure-arm` flag in our [flag index][flag_index]. Provides mgmt plane specific shared exceptions and modules.|1.2.1

> Note: We highly recommend tying your library to a major version, for instance, adding `azure-core<2.0.0` to tie the `azure-core` library to `1.x.x`

## Initializing and Authenticating Your Client

Next, on to initialization. Your constructor can take any number of parameters. By default we generate our clients with an [Azure Active Directory (AAD) token credential][aad_authentication]. We always recommend
using a [credential type][identity_credentials] obtained from the [`azure-identity`][azure_identity_library] library for AAD authentication. For this example,
we use the most common [`DefaultAzureCredential`][default_azure_credential].

As an installation note, the [`azure-identity`][azure_identity_library] library is not a requirement in the basic `setup.py` file we generate
(see `--basic-setup-py` in our [flag index][flag_index] for more information), so you would need to explicitly include this library.

```python
from azure.identity import DefaultAzureCredential
from azure.pets import PetsClient

client = PetsClient(credential=DefaultAzureCredential())
```

You can also have your generated client take in an [`AzureKeyCredential`][azure_key_credential] instead. To do so, generate with flag `--credential-types=AzureKeyCredential`,
and for more information on this flag, see our [flag index][flag_index]

```python
from azure.core.credentials import AzureKeyCredential
from azure.pets import PetsClient

credential = "myCredential"
client = PetsClient(credential=AzureKeyCredential(credential))
```

Each of these credential types also correspond to their own authentication policies that handle the credential. AutoRest automatically generates with the following default authentication policies based on the credential types:

| Credential Type | Authentication Policy
|------------------|-------------
|[`TokenCredential`][aad_authentication] | [`BearerTokenCredentialPolicy`][bearer_token_credential_policy]
|[`AzureKeyCredential`][azure_key_credential] | [`AzureKeyCredentialPolicy`][azure_key_credential_policy]

Currently, we only support generating credentials of type [`TokenCredential`][aad_authentication] and / or [`AzureKeyCredential`][azure_key_credential]. If you'd like to use your own custom credential,
you can pass the custom type into the client. However, you may have to use a custom authentication policy to handle the credential. That can also be passed in to the
client. Say your custom credential is called `MyCredential`, and the policy that handles this credential is called `MyAuthenticationPolicy`. Initializing your
client would look something like `client = PetsClient(credential=MyCredential(), authentication_policy=MyAuthenticationPolicy())`, though this of course varies
based on inputs.

## Multi API Client

Initializing your Multi API client is very similar to initializing a normal client. The only difference is there's an added optional
parameter `api_version`. With this parameter, you can specify the API version you want your client to have. If not specified, the multi
API client uses the default API version.

Using the Multi API client we generated in our [multi API generation][multiapi_generation], our example client uses default API version
`v2`. If we would like our client at runtime to have API version `v1`, we would initialize our client like:

```python
from azure.identity import DefaultAzureCredential
from azure.pets import PetsClient

client = PetsClient(credential=DefaultAzureCredential(), api_version="v1")
```

<!-- LINKS -->
[multiapi_generation]: ../generate/multiapi.md
[azure_core_library]: https://pypi.org/project/azure-core/
[msrest_library]: https://pypi.org/project/msrest/
[azure_mgmt_core_library]: https://pypi.org/project/azure-mgmt-core/
[azure_identity_library]: https://pypi.org/project/azure-identity/
[flag_index]: https://github.com/Azure/autorest/tree/master/docs/generate/flags.md
[aad_authentication]: https://docs.microsoft.com/azure/cognitive-services/authentication?tabs=powershell#authenticate-with-an-authentication-token
[identity_credentials]: https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/identity/azure-identity#credentials
[default_azure_credential]: https://docs.microsoft.com/python/api/azure-identity/azure.identity.defaultazurecredential?view=azure-python
[azure_key_credential]: https://docs.microsoft.com/python/api/azure-core/azure.core.credentials.azurekeycredential?view=azure-python
[bearer_token_credential_policy]: https://docs.microsoft.com/python/api/azure-core/azure.core.pipeline.policies.bearertokencredentialpolicy?view=azure-python
[azure_key_credential_policy]: https://docs.microsoft.com/python/api/azure-core/azure.core.pipeline.policies.azurekeycredentialpolicy?view=azure-python
