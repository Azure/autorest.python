# Change Log

### 2021-xx-xx - 5.9.0

| Library | Min Version
| --------------- | -------
|`@autorest/core` |  `3.4.5`
|`@autorest/modelerfour` | `4.19.1`
|`azure-core` dep of generated code | `1.16.0`
|`msrest` dep of generated code | `0.6.21`
|`azure-mgmt-core` dep of generated code (If generating mgmt plane code) | `1.3.0`

**New Features**

- We have added a **provisional** `rest` layer to our generated code. We have also added the following **provisional** flags listed [here](https://github.com/Azure/autorest.python/wiki/Generating-Low-Level-Client#generate-a-low-level-client). #875
- With this new release, we are also dropping support for Python 3.5 + async.  #875
- For mgmt plan SDK, default policy changes from `BearerTokenCredentialPolicy` to `ARMChallengeAuthenticationPolicy`.

**Bug Fixes**

- Correctly pad operation groups with reserved names with `Operations`  #1005

### 2021-07-13 - 5.8.4

min Autorest core version: 3.4.5

min Modelerfour version: 4.19.1

**Bug Fixes**

- Fix case where we have a grouped parameter whose name is a reserved property name #970
- Remove all hosts from global parameters, regardless of how many m4 sends us #972

### 2021-07-06 - 5.8.3

min Autorest core version: 3.3.0

min Modelerfour version: 4.19.1

**Bug Fixes**

- Fix LRO path parameterization when we have a constant path parameter #968

### 2021-06-22 - 5.8.2

min Autorest core version: 3.3.0

min Modelerfour version: 4.19.1

**Bug Fixes**

- We are now more lenient with our checks for the content type parameter  #956

### 2021-06-16 - 5.8.1

min Autorest core version: 3.3.0

min Modelerfour version: 4.19.1

**Bug Fixes**

- Fix optional properties with constant schemas. Now, properties that have constant schemas but are optional will not have the hardcoded constant value,
but will default to its `x-ms-client-default` or `None`  #952

### 2021-05-17 - 5.8.0

min Autorest core version: 3.3.0

min Modelerfour version: 4.19.1

**New Features**

- Add support for parameters and properties that can be of type "Anything".  #946

### 2021-04-20 - 5.7.0

min Autorest core version: 3.1.0

min Modelerfour version: 4.15.456

**Bug Fixes**

- Fix data plane LRO operations so they poll by default. Bumping minor version because this bug fix will change some default behavior. #936

### 2021-04-07 - 5.6.6

min Autorest core version: 3.1.0

min Modelerfour version: 4.15.456

**Bug Fixes**

- Fix docstrings so they don't get split on hyphens  #931

### 2021-04-07 - 5.6.5

min Autorest core version: 3.1.0

min Modelerfour version: 4.15.456

**Bug Fixes**

- Fix regression in multiapi generation for multiapi versions without mixin operations  #928

### 2021-03-01 - 5.6.4

min Autorest core version: 3.1.0

min Modelerfour version: 4.15.456

**Bug Fixes**
- Bump `Autorest core` minimum version to be able to deal with indented `python` blocks in config files

### 2021-02-10 - 5.6.3

min Autorest core version: 3.0.6372

min Modelerfour version: 4.15.456

**Bug Fixes**
- Bump `Autorest core` minimum version to [correctly deal with](https://github.com/Azure/autorest/pull/3860) overriding configs. Fixes submodule-specific code in our multiapi client  #880

### 2021-02-04 - 5.6.2

Autorest core version: 3.0.6318

Modelerfour version: 4.15.456

**Bug Fixes**
- Bump `Modelerfour` minimum version to [correctly deal with](https://github.com/Azure/autorest.modelerfour/pull/385) parameters specified as `'required': false` in swagger  #877

### 2021-01-27 - 5.6.1

Autorest core version: 3.0.6318

Modelerfour version: 4.15.442

**Bug Fixes**

- Instead of throwing a `DeserializationError` in the case of failed error model deserialization, we swallow the error and return the `HttpResponseError` to users.
  WARNING: You need to make sure your `msrest` version is `0.6.21` or above, or a lot of your calls will fail with an `AttributeError` message #870

### 2021-01-15 - 5.6.0

Autorest core version: 3.0.6318

Modelerfour version: 4.15.442

**New Features**

- Add support for [`black`](https://pypi.org/project/black/) formatting of your generated files. Pass flag `--black` when generating to get this behavior. #836

**Bug Fixes**

- Wrap individual enum descriptions #844
- Bump `Modelerfour` minimum version to `4.15.442` to fix [circular reference error](https://github.com/Azure/autorest/issues/3630). Special thanks to @amrElroumy for this PR. #866

### 2020-11-12 - 5.5.0

Autorest core version: 3.0.6318

Modelerfour version: 4.15.421

**New Features**

- Can now take in custom pollers and pagers through directives. This will override the defaults (`LROPoller` and `ItemPaged`, respectively). See [this readme](https://github.com/Azure/autorest.python/tree/autorestv3/test/azure/specification/custompollerpager) for the directive to use to override. #821

### 2020-11-11 - 5.4.3

Autorest core version: 3.0.6320

Modelerfour version: 4.15.421

**Bug Fixes**

- Correctly choose schema from response with 200 status code in the case of LRO operations with multiple responses #814
- Fix conflict for model deserialization when operation has input param with name `models` #819

### 2020-11-09 - 5.4.2

Autorest core version: 3.0.6320

Modelerfour version: 4.15.421

**Bug Fixes**

- Set discriminator value in cases where discriminator is readonly #815

### 2020-11-03 - 5.4.1

Autorest core version: 3.0.6318

Modelerfour version: 4.15.421

**Bug Fixes**

- Honor default value for properties if `x-ms-client-default` value is passed #798
- Can now generate services with no operations #801

### 2020-10-19 - 5.4.0

Autorest core version: 3.0.6318

Modelerfour version: 4.15.421

**New Features**

- Add support for `--python.debugger`. With this flag, you can start debugging using VS Code. Make sure to still set up your [debugging configuration](https://github.com/Azure/autorest.python/wiki/Autorest-v3-based-generator-cheatsheet#vscode-debug) #790

**Bug Fixes**

- Correctly handling inheritance of class properties for inheritance chains > 3 levels #795

### 2020-10-06 - 5.3.5

Autorest core version: 3.0.6318

Modelerfour version: 4.15.421

**Bug Fixes**

- Can now correctly poll in the case of parameterized endpoints with relative polling urls #784

### 2020-09-24 - 5.3.4

Autorest core version: 3.0.6318

Modelerfour version: 4.15.421

**Bug Fixes**

- Include `content_type` docstrings for LRO and paging operations in the case of multiple media types #778
- Return response body if its content type is `text/plain` (taken from m4 update - m4 PR #353)

### 2020-09-17 - 5.3.3

Autorest core version: 3.0.6318

Modelerfour version: 4.15.419

**Bug fixes**

- Fix trailing comma issues in metadata.json (unblocks resource multiapi generation) #777

### 2020-09-14 - 5.3.2

Autorest core version: 3.0.6318

Modelerfour version: 4.15.419

**Bug fixes**

- Allow client side validation to be turned off for multiapi mixin operations #775

### 2020-09-14 - 5.3.1

Autorest core version: 3.0.6318

Modelerfour version: 4.15.419

**Bug fixes**

- Min autorest core is now 3.0.6318 to ensure client-side-validation is disabled by default (per track2 guidelines) #772

### 2020-09-11 - 5.3.0

Autorest Core version: 3.0.6306

Modelerfour version: 4.15.419

GA of autorest V5!

**Breaking Changes**

- Raise `ValueError` instead of `NotImplementedError` if API version code doesn't exist #764

### 2020-08-31 - 5.2.0-preview.1

Autorest Core version: 3.0.6306

Modelerfour version: 4.15.410

**Breaking Changes**

- Removed the `_async` suffix from async files #759

**New Features**

- Add mapping of 401 to `ClientAuthenticationError` for default error map #763
- Updated minimum `azure-core` version to 1.8.0 #747
- Updated minimum `msrest` version to 0.6.18 #747
- Support for `multipart/form-data` #746

**Bug fixes**

- Fix "multi" in Swagger (will generate correctly multiple query param now)

### 2020-08-07 - 5.1.0-preview.7

Autorest Core version: 3.0.6302
Modelerfour version: 4.15.400

**New Features**

- Add `azure-mgmt-core` as a dependency in the generated setup.py file #738
- Correct typing for `credential` when default credential policy type is `AzureKeyCredentialPolicy` #744
- Replace instead of extending `credential_scopes` if user has inputted their own #745

### 2020-08-04 - 5.1.0-preview.6

Autorest Core version: 3.0.6287
Modelerfour version: 4.15.378

**New Features**

- Add support for `x-ms-text` XML extension #722
- Allow users to pass the name of the key header for `AzureKeyCredentialPolicy` during generation. To use, pass in
  `AzureKeyCredentialPolicy` with the `--credential-default-policy-type` flag, and pass in the key header name using
  the `--credential-key-header-name` flag #736

**Bug Fixes**

- Fix duplicate type signatures in multiapi async config file #727
- Allowing single quote in regexp #726

### 2020-06-23 - 5.1.0-preview.5

Autorest Core version: 3.0.6287
Modelerfour version: 4.15.378

**Bug Fixes**

- Correctly have default behavior of csv for array query parameters when collection format is not specified in the swagger
  (taken from m4 update - perks PR #118)
- Fix bug when generating parameters with client default value and constant schema #707
- Make operation mixin signatures for multiapi default to default api version #715
- Fix name in setup.py to default to `package-name` if set #721
- Allow different custom base url host templates across API versions #719

### 2020-07-07 - 5.1.0-preview.4

Modelerfour version: 4.15.378

**New Features**

- Enum values are uppercase (with an alias from the lowercase version) #692
- Add `http_logging_policy` setting for config, and users can override the default by passing in the kwarg `http_logging_policy` #698

### 2020-06-24 - 5.1.0-preview.3

Modelerfour version: 4.13.351

**New Features**

- Supports a function that is both LRO and paging #689
- We have added a `--credential-default-policy-type` flag. Its default value is `BearerTokenCredentialPolicy`, but it can also accept
  `AzureKeyCredentialPolicy`. The value passed in will be the default authentication policy in the client's config, so users using the
  generated library will use that auth policy unless they pass in a separate one through kwargs #686
- Added support for a data plane multiapi client #693

**Bug Fixes**

- Fix typing for discriminator values in models, so Python 3.5 can import py3 file for models #691

**Bug Fixes**

- Make enum names all upper case. This fixes issues that arise if the name of an enum is also a method that can be applied to, say, a string.
  For example, if an enum's name is count. Made sure this fix will not break users currently accessing with lower case enum names #692

### 2020-06-08 - 5.1.0-preview.2

Modelerfour version: 4.13.351

**Bug Fixes**

- Fixed "Failed to install or start extension" issue arising when invoking autorest from a tar file, by correcctly calling Python 3. #678
- Generating correct formatting for LRO and paging operation docstrings #652
- Generating correct content and formatting for LRO and paging operations in multiapi mixin #652

### 2020-06-03 - 5.1.0-preview.1

Modelerfour version: 4.13.351

**Disclaimer**

This version requires azure-core 1.6.0 and contains features and bugfixes 5.0.0-preview.8

**Features**

- Refactor async LRO poller with a AsyncLROPoller class + "begin\_" prefix
- Add continuation_token kwargs to LRO methods

**Bug Fixes**

- Corrected generation of the item name of paging response when extracting data #648
- Corrected return type typing annotation for operations that return an optional body #656
- Fixed mypy issue by only setting the generated `deserialized` variable to None if the operation has an optional return type #656
- Fixed generation of pkgutil init files #661
- Have the next operation in a paging call use the HTTP verb GET if the next operation is not defined #664

### 2020-05-22 - 5.0.0-preview.8

Modelerfour version: 4.13.351

**Bug Fixes**

- Corrected ordering of summary and description in generated methods #640
- Have `IOSchema` call super init to get all of the properties shared in `BaseSchema` #642

### 2020-05-15 - 5.0.0-preview.7

Modelerfour version: 4.13.351

**Bug Fixes**

- Adding `self` as a reserved key word for parameters to avoid "duplicate argument 'self' in function definition" error #630
- Removed `self` as a reserved key word for method and model names #630

### 2020-05-13 - 5.0.0-preview.6

Modelerfour version: 4.13.351

**Bug Fixes**

- No longer assuming that response with body from an LRO call is an ObjectSchema #623
- Checking whether "protocol" entry exists in yaml in name converter to remove erroneous "KeyError: 'protocol'" #628

### 2020-05-08 - 5.0.0-preview.5

Modelerfour version: 4.13.351

**Bug Fixes**

- Users can pass in content types with ';' inside (such as 'text/plain; encoding=UTF-8') #619
- Allowing parameters to be of type `IO` as well #618
- Can now generate without FATAL: bad indentation error (taken from m4 update - perks PR #105)

### 2020-05-06 - 5.0.0-preview.4

Modelerfour version: 4.13.346

**New Features**

- Displaying the default and possible values for content type in the docstring for operations with multiple requests #615

**Bug Fixes**

- Fixing `AsyncTokenCredential` typing import and adding to service client #591
- Can now pass `content_type` and `error_map` kwargs to LRO functions without error #597
- Now making sure to include the content type of exceptions when passing content types to 'Accept' header #602
- `include_apis` in `Metrics` for tables swagger now cased correctly #603
- Corrected spacing after `if cls:` block in operations #606

### 2020-04-23 - 5.0.0-preview.3

Modelerfour version: 4.12.301

**Bug Fixes**

- Fixed sync lro method naming in MultiAPI operation mixins #572

### 2020-04-22 - 5.0.0-preview.2

Modelerfour version: 4.12.301

**New Features**

- User can now pass in credential scopes through kwargs #575
- Default error map always contains a mapping of 404 to `ResourceNotFoundError` and 409 to `ResourceExistsError` #580

**Bug Fixes**

- Not generating async multiapi client if `--no-async` flag is specified #586
- Fixes query parameter handling in paging operations #172
- Fixes losing 404/409 default is user pass a user_map #580

### 2020-04-16 - 5.0.0-preview.1

Modelerfour version: 4.12.301

**Breaking Changes**

- If the user would like to add a patch file, they now must name the file `_patch.py` #573

**New features**

- Support non-ARM polling by default (azure-core 1.4.0)
- Adding multiple inheritance #567
- Accept polling_interval keyword passed to LRO operations #571

**Bug Fixes**

- Fixed some generated typing hints (such as LROPoller) #507

### 2020-04-09 - 5.0.0-dev.20200409.1

Modelerfour version: 4.12.301

**Bug Fixes**

- Separating out typing imports in TYPE_CHECKING block #538
- Overriding a property inherited from a parent if they both have the same name #563

**New Features**

- Client side validation is now disabled by default #558
- We now also generate an async multiapi client when running multiapiscript # 480

### 2020-04-06 - 5.0.0-dev.20200406.1

Modelerfour version: 4.12.294

**New Features**

- Can now directly patch a client by defining a `patch.py` file in the top-level of the module with a `patch_sdk` function #548
- Can now handle `time` formats #551

### 2020-04-03 - 5.0.0-dev.20200403.1

Modelerfour version: 4.12.276

**Bug Fixes**

- Fixes parameter ordering so parameters with default values are all ordered at the end #545
- Fixes `TokenCredential` and `AsyncTokenCredential` sphinx docstring #546

### 2020-04-01 - 5.0.0-dev.20200401.1

Modelerfour version: 4.12.276

**Bug Fixes**

- Now the generic models file and python3 models file have the same behavior in regards to required properties and their default values #532
- Can now specify non-string enums #534
- Fixes `TokenCredential` typing #535

### 2020-03-30 - 5.0.0-dev.20200330.1

Modelerfour version: 4.12.276

**Bug Fixes**

- Fix enum default and required default #532

### 2020-03-26 - 5.0.0-dev.20200326.1

Modelerfour version: 4.12.276

**Bug Fixes**

- Will no longer permit generated enums and models to have the same name #504
- No longer exposing models from operation groups without importing them #486
- Now correctly deserializes error's that have an empty object (AnySchema) as a model #516
- Added a list of parameter names to reserved parameter words, so there won't be clashes #525
- If a property's schema is readonly, we will show that property as being readonly (taken from m4 update #234)
- Remove `"azure-"` prefix from user agent name #523
- Correcting issue in generating multiapi with submodule, where generated user agent name included the `#` #505

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
  To keep auto-completion in most cases, models are now generated for Python 2 and Python 3. Python 3 uses the "\*" syntax for keyword-only arguments.
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

- All Model call super(XX, self).**init**()

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
