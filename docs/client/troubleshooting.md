# <img align="center" src="../images/logo.png">  Troubleshooting

## Error Handling

Our generated clients raise [exceptions defined in `azure-core`][azure_core_exceptions]. While the base for all exceptions is [`AzureError`][azure_error],
[`HttpResponseError`][http_response_error] is also a common base catch-all for exceptions, as these errors are thrown in the case of a request being made, and a non-successful
status code being received from the service.

Our generated code also offers some default mapping of status codes to exceptions. These are `401` to [`ClientAuthenticationError`][client_authentication_error], `404` to
[`ResourceNotFoundError`][resource_not_found_error], and `409` to [`ResourceExistsError`][resource_exists_error].

A very basic form of error handling looks like this:

```python
from azure.identity import DefaultAzureCredential
from azure.pets import PetsClient

client = PetsClient(credential=DefaultAzureCredential())
try:
    dog = client.get_dog()
except HttpResponseError as e:
    print("{}: {}".format(e.status_code, e.message))
```

You can also catch errors with more granularity, i.e. just catching a `ResourceExistsError`.

```python
from azure.identity import DefaultAzureCredential
from azure.pets import PetsClient

client = PetsClient(credential=DefaultAzureCredential())
try:
    dog = client.get_dog()
except ResourceExistsError as e:
    print(e.message)
```

A final note regarding error models: If you define your own special error model (like [this][error_model]), we still expose these to the users. Though the error thrown to
the user will be one defined in [`azure-core`][azure_core_exceptions] (most likely [`HttpResponseError`][http_response_error]), we expose your specially-defined swagger
models through the `model` property on the returned error. I.e.:

```python
from azure.identity import DefaultAzureCredential
from azure.pets import PetsClient

client = PetsClient(credential=DefaultAzureCredential())
try:
    dog = client.get_dog()
except HttpResponseError as e:
    pet_action_error = e.model
```

## Logging

Our generated libraries use the standard [`logging`][logging] library for logging. Basic information about HTTP sessions (URLs, headers, etc.) is logged at INFO level.
Our logger's name is `azure`.

Detailed DEBUG level logging, including request/response bodies and un-redacted headers, can be enabled on a client with the logging_enable argument:

```python
import logging
import sys
from azure.identity import DefaultAzureCredential
from azure.pets import PetsClient

# Create a logger for the 'azure' SDK
logger = logging.getLogger('azure')
logger.setLevel(logging.DEBUG)

# Configure a console output
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

client = PetsClient(credential=DefaultAzureCredential(), logging_enable=True)
```

Network trace logging can also be enabled for any single operation:

```python
dog = client.get_dog(logging_enable=True)
```

<!-- LINKS -->
[azure_core_exceptions]: https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/core/azure-core#azure-core-library-exceptions
[azure_error]: https://docs.microsoft.com/en-us/python/api/azure-core/azure.core.exceptions.azureerror?view=azure-python
[http_response_error]: https://docs.microsoft.com/en-us/python/api/azure-core/azure.core.exceptions.httpresponseerror?view=azure-python
[client_authentication_error]: https://docs.microsoft.com/en-us/python/api/azure-core/azure.core.exceptions.clientauthenticationerror?view=azure-python
[resource_not_found_error]: https://docs.microsoft.com/en-us/python/api/azure-core/azure.core.exceptions.resourcenotfounderror?view=azure-python
[resource_exists_error]: https://docs.microsoft.com/en-us/python/api/azure-core/azure.core.exceptions.resourceexistserror?view=azure-python
[error_model]: https://github.com/Azure/autorest.testserver/blob/master/swagger/xms-error-responses.json#L220
[logging]: https://docs.python.org/3.5/library/logging.html