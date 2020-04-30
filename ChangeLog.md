# Change Log

### Unreleased
Modelerfour version: 4.12.301

**Bug Fixes**

- Fixing `AsyncTokenCredential` typing import and adding to service client  #591
- Can now pass `content_type` and `error_map` kwargs to LRO functions without error  #597

### 2020-04-23 - 5.0.0-preview.3
Modelerfour version: 4.12.301

**Bug Fixes**

- Fixed sync lro method naming in MultiAPI operation mixins  #572

### 2020-04-22 - 5.0.0-preview.2
Modelerfour version: 4.12.301

**New Features**

- User can now pass in credential scopes through kwargs  #575
- Default error map always contains a mapping of 404 to `ResourceNotFoundError` and 409 to `ResourceExistsError` #580

**Bug Fixes**

- Not generating async multiapi client if `--no-async` flag is specified  #586
- Fixes query parameter handling in paging operations  #172
- Fixes losing 404/409 default is user pass a user_map  #580

### 2020-04-16 - 5.0.0-preview.1
Modelerfour version: 4.12.301

**Breaking Changes**

- If the user would like to add a patch file, they now must name the file `_patch.py`  #573

**New features**

- Support non-ARM polling by default (azure-core 1.4.0)
- Adding multiple inheritance  #567
- Accept polling_interval keyword passed to LRO operations  #571

**Bug Fixes**

- Fixed some generated typing hints (such as LROPoller) #507

### 2020-04-09 - 5.0.0-dev.20200409.1
Modelerfour version: 4.12.301

**Bug Fixes**

- Separating out typing imports in TYPE_CHECKING block  #538
- Overriding a property inherited from a parent if they both have the same name  #563

**New Features**

- Client side validation is now disabled by default  #558
- We now also generate an async multiapi client when running multiapiscript  # 480

### 2020-04-06 - 5.0.0-dev.20200406.1
Modelerfour version: 4.12.294

**New Features**

- Can now directly patch a client by defining a `patch.py` file in the top-level of the module with a `patch_sdk` function  #548
- Can now handle `time` formats  #551

### 2020-04-03 - 5.0.0-dev.20200403.1
Modelerfour version: 4.12.276

**Bug Fixes**

- Fixes parameter ordering so parameters with default values are all ordered at the end  #545
- Fixes `TokenCredential` and `AsyncTokenCredential` sphinx docstring  #546

### 2020-04-01 - 5.0.0-dev.20200401.1
Modelerfour version: 4.12.276

**Bug Fixes**

- Now the generic models file and python3 models file have the same behavior in regards to required properties and their default values  #532
- Can now specify non-string enums  #534
- Fixes `TokenCredential` typing  #535

### 2020-03-30 - 5.0.0-dev.20200330.1
Modelerfour version: 4.12.276

**Bug Fixes**

- Fix enum default and required default  #532

### 2020-03-26 - 5.0.0-dev.20200326.1
Modelerfour version: 4.12.276

**Bug Fixes**

- Will no longer permit generated enums and models to have the same name  #504
- No longer exposing models from operation groups without importing them  #486
- Now correctly deserializes error's that have an empty object (AnySchema) as a model  #516
- Added a list of parameter names to reserved parameter words, so there won't be clashes  #525
- If a property's schema is readonly, we will show that property as being readonly (taken from m4 update #234)
- Remove `"azure-"` prefix from user agent name  #523
- Correcting issue in generating multiapi with submodule, where generated user agent name included the `#`  #505


### 2020-01-17 - 4.0.74

- Declare "self" as reserved keyword

### 2019-06-12 - 4.0.71

- no-async flag to skip async code generation

### 2019-05-21 - 4.0.70

- Beta version of --keep-version-file for ARM generator

### 2019-02-13 - 4.0.67

- All models will now be generated in two files `_models` and `_models_py3`, and paging in a page file
- Breaking changes: Import of models and enums from package must be done from package.models

### 2019-02-11 - 4.0.66

- Fix async cross-link documentation

### 2019-02-08 - 4.0.65

- New version of async generation. Requires msrest 0.6.3 and msrestazure 0.6.0.

  - namespace.XXXXClientAsync is now namespace.aio.XXXClient

- Support now MICROSOFT_MIT_SMALL and MICROSOFT_MIT_SMALL_NO_CODEGEN headers options

### 2019-01-08 - 4.0.64

- New version of async generation. Requires msrest 0.6.3 and msrestazure 0.6.0.

### 2018-12-17 - 4.0.63

- Autorest now generates async code.

**This version requires EXACTLY msrest 0.6.0 to 0.6.2 and is considered deprecated. Do NOT generate with it.**

### 2018-07-09 - 3.0.58

- Fix some complex XML parsing issues. Requires msrest 0.5.2

### 2018-07-05 - 3.0.56

- Differentiate Default and AzureAsyncOperation LRO options
- Fix bug with operation flattenning if operation has a parameter called "foo" and model too disambiguiated as "foo1"

### 2018-06-13 - 3.0.54

This version requires msrestazure 0.4.32

- Add support for LRO options

### 2018-06-13 - 3.0.53

This version requires msrest 0.5.0

- XML support
- Big fix on headers (Accept/Content-Type) to better reflect consumes/produces of Swagger
- Refactoring of "send" to better separate request creation and request sending

### 2018-06-08 - 3.0.52

- Beta version of --keep-version-file

### 2018-05-08 - 3.0.51

- Py3 model files must inherit from Py3 files

### 2018-04-18 - 3.0.50

- Add context manager to SDK client that keeps the same sessions across requests.

### 2018-04-17 - 3.0.49

- Fix some valid discriminator + flatten scenarios #2889

### 2018-04-16 - 3.0.48

- Fix bad comma on py3 models if super class has no attributes

### 2018-03-27 - 3.0.43

- Add documentation to enum #49

### 2018-03-07 - 3.0.41

**Breaking changes**

- Model signatures are now using only keywords-arguments syntax. Every positional arguments are required to be rewritten as keywords-arguments.
  To keep auto-completion in most cases, models are now generated for Python 2 and Python 3. Python 3 uses the "*" syntax for keyword-only arguments.
- Enum type are now using the "str" mixin (`class AzureEnum(str, Enum)`) to improve experiences when unkown enum are met. This is not a breaking change,
  but documentation about mixin enum and some recommendations should be known:
  https://docs.python.org/3/library/enum.html#others
  At a glance:

  - "is" should not be used at all.
  - "format" will return the string value, where "%s" string formatting will return `NameOfEnum.stringvalue`. Format syntax should be used always.

- New Long Running Operation:

  - Return type changes from msrestazure.azure_operation.AzureOperationPoller to msrest.polling.LROPoller. External API is the same.
  - Return type is now **always** a msrest.polling.LROPoller, whatever the optional parameters.
  - raw=True changes behavior. Instead of not polling and returning the initial call as ClientRawResponse, now we return a LROPoller as well and the final
    resource is returned as a ClientRawResponse.
  - Adding "polling" parameters. Polling=True is the default and poll using ARM algorithm. Polling=False does not poll and return the initial call reponse.
  - Polling accept instances of subclasses of msrest.polling.PollingMethod.
  - `add_done_callback` now does not fail if poller is done, but execute the callback right away.

### 2018-02-16 - 2.1.38

- Externalize Url as a metadata property on operation

### 2018-02-06 - 2.1.35

- Allow "baseUrl" as a custom parameter at the client level.

### 2018-01-04 - 2.1.34

- Fix inheritance and additionalProperties used together

### 2017-12-28 - 2.1.32

- Refactor LRO operations with an external \_XXX_initial call

### 2017-12-22 - 2.1.30

- Add "async", "await" and "mro" as Python reserved keywords.

### 2017-12-13 - 2.1.28

- All Model call super(XX, self).__init__()

### 2017-11-27 - 2.0.25

- Add no-namespace-folders option
- Add basic-setup-py. Change the default behavior to do NOT generate the setup.py.

### 2017-11-22 - 2.0.23

- Add "models" link inside operation groups
- Add help for Python

### 2017-10-19 - 2.0.18

- Fix namespace folders in Vanilla generator

### 2017-10-10 - 2.0.17

- Fix paging description

### 2017-10-10 - 2.0.16
- Improve polymorphic discriminator documentation (#17)
- Add deprecated support (#16)
- Fix invalid headers test (#15)
- Fix invalid python code in some scenario (#14)
- Stop checking str type for client parameter (#12)
- Add client-side-validation to Autorest.Python (#11)

### 2017-09-27 - 2.0.14
- Improve documentation cross-reference (#9)

### 2017-09-26 - 2.0.13
- Remove constraint on array type, if array is used in the URL (#8)
