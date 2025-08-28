# <img align="center" src="../images/logo.png">  Accessing Models and Enums

## General

Models and enums are generated in the `models` namespace. So, say you are using package `azure.pets`. To access model `Dog`, you would use the following code
snippet

```
from azure.pets.models import Dog
```

Enums are also listed in the `models` namespace, so say you have enum class `DogTypes`. To access the `DALMATIAN` enum, your code would look like

```
from azure.pets.models import DogTypes

my_dog_type = DogTypes.DALMATIAN
```
