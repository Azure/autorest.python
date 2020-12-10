# Generate Pets in Python with Multi API

### General settings

```yaml
python: true
package-name: azure-pets
```

### Multi API generation

These settings apply only when `--multiapi` is specified on the command line.

```yaml $(multiapi)
batch:
    - tag: v1
    - tag: v2
    - multiapiscript: true
```

### Multi API script

```yaml $(multiapiscript)
output-folder: $(python-sdks-folder)/pets/azure-pets/azure/pets
perform-load: false
clear-output-folder: false
```

### Tag: v1

These settings apply only when `--tag=v1` is specified on the command line.

```yaml $(tag) == 'v1'
input-file: pets.json
namespace: azure.pets.v1
output-folder: $(python-sdks-folder)/pets/azure-pets/azure/pets/v1
```

### Tag: v2

These settings apply only when `--tag=v2` is specified on the command line.

```yaml $(tag) == 'v2'
input-file: petsv2.json
namespace: azure.pets.v2
output-folder: $(python-sdks-folder)/pets/azure-pets/azure/pets/v2
```
