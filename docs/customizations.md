# Grow Up Story for Generated SDKs

This quickstart will introduce how to grow up your generated code with customizations.

**Note: This quickstart does not focus on renaming or removing generated objects**. If you'd like to rename or remove generated objects, the changes should really be made in the
OpenAPI definition of your service. If you absolutely can not modify the OpenAPI definition, you can use directives, specifically [these pre-defined directives](https://github.com/Azure/autorest/blob/main/docs/generate/built-in-directives.md) in your README configuration

## Key Concept: _patch.py

The `_patch.py` files at each level of the modules will be the entry point to customize the generated code.

For example, if you want to override a model, you will use the `_patch.py` file at the `models` level of your
generated code to override.

The main flow of the `_patch.py` file will be:

1. Import the generated object you wish to override.
2. Inherit from the generated object, and override its behavior with your desired code functionality
3. Include the name of your customized object in the `__all__` of the `_patch.py` file

To test that your behavior has been properly customized, please add tests for your customized code.
If you find that your customizations for an object are not being called, please make sure that
your customized object is included in the `__all__` of your `_patch.py` file.

The `_patch.py` file will never be removed during regeneration, so no worries about your customizations being
lost!

## Examples

- [Change Model Behavior](#change-model-behavior)
- [Change Operation Behavior](#change-operation-behavior)
- [Overload an Operation](#overload-an-operation)
- [Change Client Behavior](#change-client-behavior)
- [Add a Client Method](#add-a-client-method)

### Change Model Behavior

To override model behavior, you will work with the `_patch.py` file in the `models` folder of your generated code.

In the following example, we override the generated `Model`'s `input` parameter to accept both `str` and `datetime`,
instead of just `str`.

In this `_patch.py` file:

```
azure-sdk
│   README.md
│
└───azure
    └───sdk
        └───models
        │   _models.py # where the generated models are
        |   _patch.py # where we customize the models code
```

```python
import datetime
from typing import Union
from ._models import Model as ModelGenerated

class Model(ModelGenerated):

  def __init__(self, input: Union[str, datetime.datetime]):
    super().__init__(
      input=input.strftime("%d-%b-%Y") if isinstance(input, datetime.datetime) else input
    )

__all__ = ["Model"]
```

### Change Operation Behavior

To change an operation, you will import the generated operation group the operation is on. Then you can inherit
from the generated operation group and modify the behavior of the operation.

In the following example, the generated operation takes in a datetime input, and returns a datetime response.
We want to also allow users to input strings, and return a string response if users inputted a string.

In this `_patch.py` file:

```
azure-sdk
│   README.md
│
└───azure
    └───sdk
        └───operations
        │   _operations.py # where the generated operations are
        |   _patch.py # where we customize the models code
```

```python
from typing import Union
import datetime
from ._operations import OperationGroup as OperationGroupGenerated

class OperationGroup(OperationGroupGenerated):

  def operation(self, input: Union[str, datetime.datetime]):
    response: datetime.datetime = super().operation(
        datetime.datetime.strptime(input, '%b %d %Y') if isinstance(input, str) else input
    )
    return response.strftime("%d-%b-%Y") if isinstance(input, str) else response


__all__ = ["OperationGroup"]
```

### Overload an Operation

You can also easily overload generated operations. For example, if you want users to be able to pass in the body parameter
as a positional-only single dictionary, or as splatted keyword arguments, you can inherit and override the operation on the operation group
in the `_patch.py` file in the `operations` modules.

In this `_patch.py` file:

```
azure-sdk
│   README.md
│
└───azure
    └───sdk
        └───operations
        │   _operations.py # where the generated operations are
        |   _patch.py # where we customize the models code
```

```python
from typing import overload, Dict, Any
from ._operations import OperationGroup as OperationGroupGenerated

class OperationGroup(OperationGroupGenerated):

    @overload
    def operation(self, body: Dict[str, Any], /, **kwargs: Any):
        """Pass in the body as a positional only parameter."""

    @overload
    def operation(self, *, foo: str, bar: str, **kwargs: Any):
        """Pass in the body as splatted keyword only arguments."""

    def operation(self, *args, **kwargs):
        """Base operation for the two overloads"""
        if not args:
            args.append({"foo": kwargs.pop("foo"), "bar": kwargs.pop("bar")})
        return super().operation(*args, **kwargs)

__all__ = ["OperationGroup"]
```

### Change Client Behavior

In this example, we change the default authentication policy for a client.

In this `_patch.py` file:

```
azure-sdk
│   README.md
│
└───azure
    └───sdk
        │   _service_client.py # where the generated service client is
        |   _patch.py # where we customize the models code
        └───operations
        └───models
```

```python
from ._service_client import ServiceClient as ServiceClientGenerated
from azure.core.pipeline import PipelineRequest
from azure.core.pipeline.policies import SansIOHTTPPolicy

class MyAuthenticationPolicy(SansIOHTTPPolicy):

    def __init__(self, key: str):
        self.key = key

    def on_request(self, request: PipelineRequest):
        request.http_request.headers["Authorization"] = f"My key is {self.key}"
        return super().on_request(request)

class ServiceClient(ServiceClientGenerated):

    def __init__(self, endpoint: str, credential: str, **kwargs):
        super().__init__(
            endpoint=endpoint,
            credential=credential,
            authentication_policy=kwargs.pop("authentication_policy", MyAuthenticationPolicy(credential)),
            **kwargs
        )

__all__ = ["ServiceClient"]
```

### Add a Client Method

Similar to models and operations, you can override client behavior in a `_patch.py` file, this time
at the root of the sdk.

Here, we will be adding an alternate form of authentication on the client, class method `from_connection_string`.

In this `_patch.py` file:

```
azure-sdk
│   README.md
│
└───azure
    └───sdk
        │   _service_client.py # where the generated service client is
        |   _patch.py # where we customize the models code
        └───operations
        └───models
```

```python
from typing import Any
from azure.core.credentials import AzureKeyCredential
from ._service_client import ServiceClient as ServiceClientGenerated

class ServiceClient(ServiceClientGenerated):

    @classmethod
    def from_connection_string(cls, connection_string: str, **kwargs: Any):
        parsed_connection_string = _parse_connection_string(connection_string) # parsing function you've defined
        return cls(
            credential=AzureKeyCredential(parsed_connection_string.pop("accesskey")),
            endpoint=parsed_connection_string.pop("endpoint")
        )

__all__ = ["ServiceClient"]
```
