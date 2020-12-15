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

## Initializing Your Client

Next, on to initialization. Your constructor can take any number of parameters. If your client has no parameters (no client parameters detailed
in the swagger (TODO: link to swagger docs) and you choose to generate without credentials), initializing your client would just look like

```python
from azure.pets import PetsClient

client = PetsClient()
```

However, by default we generate clients with credentials, so continue on to [Authenticating Your Client](#authenticating-your-client "Authenticating Your Client")
to find out how to input a credential.

## Authenticating Your Client

By default we generate our clients with an [Azure Active Directory (AAD) token credential][aad_authentication]. We always recommend
using a [credential type][identity_credentials] obtained from the [`azure-identity`][identity_pypi] library for AAD authentication. For this example,
we use the most common [`DefaultAzureCredential`][default_azure_credential].

As an installation note, the [`azure-identity`][identity_pypi] library is not a requirement in the basic `setup.py` file we generate
(see `--basic-setup-py` in our [flag index][flag_index] for more information), so you would need to install this library separately.

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

Currently, we only support generating credentials of type `TokenCredential` and / or `AzureKeyCredential`. If you'd like to use your own custom credential,
you can still pass it in to the client. However, you may have to use a custom authentication policy to handle the credential. That can also be passed in to the
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
[aad_authentication]: https://docs.microsoft.com/en-us/azure/cognitive-services/authentication?tabs=powershell#authenticate-with-azure-active-directory
[identity_credentials]: https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/identity/azure-identity#credentials
[identity_pypi]: https://pypi.org/project/azure-identity/
[default_azure_credential]: https://docs.microsoft.com/en-us/python/api/azure-identity/azure.identity.defaultazurecredential?view=azure-python
[azure_key_credential]: https://docs.microsoft.com/en-us/python/api/azure-core/azure.core.credentials.azurekeycredential?view=azure-python
[flag_index]: https://github.com/Azure/autorest/tree/master/docs/generate/flags.md
