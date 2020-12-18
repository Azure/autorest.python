# <img align="center" src="../images/logo.png">  Generating a Multi API Python Client with AutoRest

If you want to generate one client that handles multiple API versions (a common use-case for this is supporting multiple Azure clouds, since a service's API versions can differ between them), this is the section for you. Python is the only language that supports this, hence why these docs are in the Python-specific section.

Before getting into the multiapi specific sections that need to be added to your readme, you need to make sure you have a tag set up for every single API version you want to generate. See the ["Adding Tags When Generating"][tags] docs to find out how to set this up. Following the [main example][main_example], this example will suppose you're generating 2 different API versions: `v1` and `v2`.

The flag you use on the command line to specify you want multiapi code generation is `--multiapi`. Thus, we need to add a `multiapi` specific section to our readme.
Let's add it underneath `General Settings` to keep it to the top of our readme

````
### Multi API generation

These settings apply only when `--multiapi` is specified on the command line.
```yaml $(multiapi)
```
````

With `multiapi`, we want to batch execute each of our API versions:

````
### Multi API generation

These settings apply only when `--multiapi` is specified on the command line.
```yaml $(multiapi)
batch:
    - tag: v1
    - tag: v2
```
````

With this code, AutoRest will first generate the files listed under the `v1` tag, then the files listed under the `v2` tag.
After generating these though, AutoRest needs to generate the multiapi client on top of these files. This layer will wire users
to the correct API version based on which API version the user wants. To add this layer, you need to include a `multiapiscript` section
of your config. Users should never specify `multiapiscript` on the command line, but it is a required flag in a configuration
file to let AutoRest know it has to run its multiapi script.

````
```yaml $(multiapiscript)
output-folder: $(python-sdks-folder)/pets/azure-pets/azure/pets
perform-load: false
clear-output-folder: false
```
````

> Note: `perform-load` is an internal configuration field used by AutoRest to decide whether it should try to load an input file. Since we're not actively generating
> from an inputted swagger field in the `multiapiscript` step, we include this in our yaml code block.

Now, if you have `clear-output-folder` specified in your general settings, you would also have to include `clear-output-folder: false` inside
your `multiapiscript` block. This is because `clear-output-folder` clears your output folder before each generation, which is not what we want
if we want to batch generate multiple API versions, then generate a multiAPI client over that.

A final note about optional flags in this section: If you don't specify a default API version, the generated client will use the latest GA service version as the default API version for users, which in our case is `v2`. Meaning, if a user does not pass in an `api_version` value to the generated multi API client, that client will use the default API version `v2`. Thus, if you want another API version, say `v1` to be the default API for users, you would include `default-api: v1` in this `multiapiscript` section.

Finally, we have to actually call the `multiapiscript` section, so we add it to our batch execution:

````
### Multi API generation

These settings apply only when `--multiapi` is specified on the command line.

```yaml $(multiapi)
batch:
    - tag: v1
    - tag: v2
    - multiapiscript: true
```
````

And that's it! We've included the final config file in our [examples folder][examples], please feel free to refer to this.

<!-- LINKS -->
[tags]: https://github.com/Azure/autorest/tree/master/docs/generate/readme.md#adding-tags-when-generating
[main_example]: https://github.com/Azure/autorest/tree/master/docs/generate/examples/tags/readme.md
[examples]: ./examples/multiapi/readme.md