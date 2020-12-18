# <img align="center" src="../images/logo.png">  Accessing Models and Enums

## General

Models and enums are generated in the `models` namespace. So, say you are using package `azure.pets`. To access model `Dog`, you would use the following code
snippet

```
from azure.pets.models import Dog
```

Enums are also listed in the `models` namespace, so say you have enum class `DogTypes`. To access the `DALMATION` enum, your code would look like

```
from azure.pets.models import DogTypes

my_dog_type = DogTypes.DALMATION
```

## Multi API

There is also a `models` module in a multi API client. There, you can access the latest version of each models.

If you want to access a specific API version's models, you can do so through the [`models()`][models_ex] class method we expose on the multi API client.
It accepts optional parameter `api_version`. If specified, it will retrieve the models from that API version. Otherwise, retrieves models from the
default API version the code was generated with.

<!-- LINKS -->
[models_ex]: https://github.com/Azure/autorest.python/blob/autorestv3/test/multiapi/Expected/AcceptanceTests/Multiapi/multiapi/_multiapi_service_client.py#L91
