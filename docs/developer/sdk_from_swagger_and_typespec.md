# Overview

This document compares Python SDKs generated from Swagger (OpenAPI) specifications versus TypeSpec. For clarity, we'll refer to these as "Swagger SDKs" and "TypeSpec SDKs" respectively.

## Model 

### Model Structure

#### Msrest Model

Swagger SDKs are generated from [Swagger specifications](https://github.com/Azure/azure-rest-api-specs/tree/main/specification) using [@autorest/python](https://www.npmjs.com/package/@autorest/python), and implement the Msrest model pattern. The following example illustrates the fundamental structure of an Msrest model:

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

### DPG Model

TypeSpec SDKs are generated from [TypeSpec](https://github.com/microsoft/typespec/) using [@azure-tools/typespec-python](https://www.npmjs.com/package/@azure-tools/typespec-python), and implement the DPG model pattern. The following example demonstrates the fundamental structure of a DPG model:

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

### Model Usage

#### Msrest Model Usage

```python
msrest_model = Person(name="xxx", parent_name="xxx")
print(msrest_model.name)
print(msrest_model.parent_name)

# Access model as a dictionary
json_model = msrest_model.as_dict()
print(json_model["name"])
print(json_model["parentName"])
```

#### DPG Model Usage

```python
dpg_model = Person(name="xxx", parent_name="xxx")
print(dpg_model.name)
print(dpg_model.parent_name)

# Access model directly as a dictionary
print(dpg_model["name"])
print(dpg_model["parentName"])
```

By comparing these usage patterns, we can see that DPG models can be accessed directly as dictionaries without calling `.as_dict()`, providing a more convenient experience.

#### Usage Note

For backward compatibility, DPG models continue to support the `.as_dict()` method for existing SDK users.

### Model Flattening

When a property is marked with `"x-ms-flatten": "true"` (as described [here](https://azure.github.io/autorest/extensions/#x-ms-client-flatten)), nested properties can be accessed directly in Msrest models as follows:

#### Simple Flattening Example

```python
class Person(_serialization.Model):
    _attribute_map = {
        "name": {"key": "properties.name", "type": "str"},
    }

    def __init__(self, *, name: Optional[str] = None) -> None:
        ...

msrest_model = Person(name="xxx")
print(msrest_model.name) # A
print(msrest_model.properties.name) # equivalent to A
``` 

When an inner property name matches an outer property name, a prefix is added to avoid name collisions:

#### Complex Flattening Example

```python
class Person(_serialization.Model):
    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "properties_name": {"key": "properties.name", "type": "str"},
    }

    def __init__(self, *, name: Optional[str] = None) -> None:
        ...

msrest_model = Person(name="xxx", properties_name="properties_name")
print(msrest_model.name)
print(msrest_model.properties_name) # A
print(msrest_model.properties.name) # equivalent to A
```

Due to inconsistent usage of flattening in some Swagger specifications, property names can become unwieldy and user-unfriendly. For this reason, **DPG models do not support flattening**.

#### Flattening Compatibility Note

For legacy SDKs generated from Swagger that are migrated to TypeSpec, we've designed a [compatibility mechanism](https://azure.github.io/typespec-azure/docs/howtos/generate-client-libraries/07types/#flattening) to minimize breaking changes. However, for deeply nested flattened properties, code updates may be required:

```python
# Msrest model
msrest_model = Model(...)

print(msrest_model.properties_name) # A
print(msrest_model.properties.name) # equivalent to A
print(msrest_model.properties_properties_name) # B
print(msrest_model.properties.properties.name) # equivalent to B

# After migration to TypeSpec
dpg_model = Model(...)
print(dpg_model.properties_name) # A, backwards compatible but not recommended
print(dpg_model.properties.name) # equivalent to A
print.dpg_model.properties_properties_name) # no longer works
print(dpg_model.properties.properties.name) # recommended approach after migration
```

### Additional Properties

#### Additional Properties in Msrest Models
To support [additional properties](https://www.apimatic.io/openapi/additionalproperties), Msrest models include an `additional_properties` parameter:

```python
msrest_model = Model(additional_properties={"hello": "world"})
print(msrest_model) # output is `{"hello": "world"}`
```

#### Additional Properties in DPG Models
DPG models inherently support additional properties through dictionary-like behavior:

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

## Query/Header Parameters in Operations

Query and header parameters in Swagger-generated SDKs are positional, while in TypeSpec-generated SDKs they are keyword-only:

```python
# Swagger SDK
client.operation("header", "query") # A
client.operation(header_parameter="header", query_parameter="query") # equivalent to A

# After migration to TypeSpec
client.operation("header", "query") # no longer works
client.operation(header_parameter="header", query_parameter="query") # correct approach
```

## File Name Changes
After migration, some internal file names change, but these changes do not affect SDK users:

```
_xxx_client.py => _client.py
_xxx_enums.py  => _enum.py
_models_py3.py => _models.py
```
