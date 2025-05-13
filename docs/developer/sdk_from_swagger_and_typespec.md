# Overview

This doc introdcues the difference between Python SDK generated from swagger(OpenAPI) and typespec. In the following doc, we call the former swagger SDK and the latter typespec SDK.

## Model 

### Model structure

#### Msrest model

Swagger SDK is generated from [Swagger specifications](https://github.com/Azure/azure-rest-api-specs/tree/main/specification) using [@autorest/python](https://www.npmjs.com/package/@autorest/python), and implements the Msrest model pattern for SDK consumers. The following example illustrates the fundamental structure of an Msrest model:

```python
from azure.mgmt.example._utils import serialization as _serialization

class Person(_serialization.Model):
    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "parent_name": {"key": "parentName", "type": "str"},
    }

    def __init__(self, *, name: Optional[str] = None, parent_name: Optional[str] = None) -> None:
        ...
```

### DPG model

Typespec SDK is generated from [typespec](https://github.com/microsoft/typespec/) using [@azure-tools/typespec-python](https://www.npmjs.com/package/@azure-tools/typespec-python), and implements the DPG model pattern. The following example demonstrates the fundamental structure of a DPG model:

```python
from azure.mgmt.example._utils.model_base import Model as _Model, rest_field

class Person(_Model):
    name: Optional[str] = rest_field()
    parent_name: Optional[str] = rest_field(name="parentName")

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
        parent_name: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None: ...


    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
```

### Model usage

#### Msrest model usage

```python
msrest_model = Person(name="xxx", parent_name="xxx")
print(msrest_model.name)
print(msrest_model.parent_name)

# Access model as a dictionary
json_model = msrest_model.as_dict()
print(json_model["name"])
print(json_model["parentName"])
```

#### DPG model usage

```python
dpg_model = Person(name="xxx", parent_name="xxx")
print(dpg_model.name)
print(dpg_model.parent_name)

# Access model directly as a dictionary
print(dpg_model["name"])
print(dpg_model["parentName"])
```

By comparing the usage, We can see that users could use DPG model as dictionary directly instead of calling `.as_dict()` as before, which is more convenient.

#### NOTE for usage

For backward compatibility, DPG model still supports `.as_dict()` for legacy SDK users.

### Model for flatten

If property is marked with `"x-ms-flatten": "true"` (e.g. [here](https://azure.github.io/autorest/extensions/#x-ms-client-flatten)), nested property could be accessed directly in Msrest model like:

#### Simple flatten

```python
class Person(_serialization.Model):
    _attribute_map = {
        "name": {"key": "properties.name", "type": "str"},
    }

    def __init__(self, *, name: Optional[str] = None) -> None:
        ...

msrest_model = Persion(name="xxx")
print(msrest_model.name) # A
print(msrest_model.properties.name) # equal to A
``` 

When the inner property name is same with outter property name, to avoid name duplicated, there will be prefix before the innter property name like:

#### Bad flatten

```python
class Person(_serialization.Model):
    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "properties_name": {"key": "properties.name", "type": "str"},
    }

    def __init__(self, *, name: Optional[str] = None) -> None:
        ...

msrest_model = Persion(name="xxx", properties_name="properties_name")
print(msrest_model.name)
print(msrest_model.properties_name) # A
print(msrest_model.properties.name) # equal to A
```

Since some swagger author abouse flatten, some property name has long and ugly prefix name which is not friendly for SDK user. Thus **DPG model don't support flatten**.

#### NOTE for flatten

For legacy SDKs which are genearted from swagger, after migration to typespec, we design a [compatible logic](https://azure.github.io/typespec-azure/docs/howtos/generate-client-libraries/07types/#flattening) to not break legacy SDK users. However, for deep nested flatten, legacy SDK users still have to update the code.

```python
# Msrest model
msrest_model = Model(...)

print(msrest_model.properties_name) # A
print(msrest_model.properties.name) # equal to A
print(msrest_model.properties_properties_name) # B
print(msrest_model.properties.properties.name) # equal to B

# after migrate to typespec
dpg_model = Model(...)
print(dpg_model.properties_name) # A, compatible with before but not recommend
print(msrest_model.properties.name) # equal to A
print(msrest_model.properties_properties_name) # can't work anymore
print(msrest_model.properties.properties.name) # legacy SDK users shall update code to use model with this way
```

### Additional properties

#### Additional properties in Msrest model
To support [additional properties](https://www.apimatic.io/openapi/additionalproperties), Msrest model introduce a property named `additional_properties`:

```python
msrest_model = Model(additional_properties={"hello": "world"})
print(msrest_model) # output is `{"hello": "world"}`
```

#### Additional properties in DPG model
DPG model could accept any key just like a dictionary so it supports additional properties natively:

```python
dpg_model = Model({"hello": "world"})
# or
dpg_model = Model()
dpg_model.update({"hello": "world"})
# or 
dpg_model = Model()
dpg_model["hello"] = "world"

print(dpg_model) # output is `{"hello": "world"}`
```

## Query/Header parameter in Operation

Query/Header parameter in SDK generated from swagger is positional but in SDK generated from typespec is keyword only:

```python

client.operation("header", "query") # A
client.operation(header_parameter="header", query_parameter="query") # equal to A

# After migration
client.operation("header", "query") # can't work anymore
client.operation(header_parameter="header", query_parameter="query") # OK
```


## File name change
After migration, there are some changes for private file name but will not have any impact for SDK users.

```
_xxx_client.py => _client.py
_xxx_enums.py  => _enum.py
_models_py3.py => _models.py
```
