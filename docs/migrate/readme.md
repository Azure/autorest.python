# <img align="center" src="../images/logo.png">  Migrating to Latest AutoRest

See the [main docs][main_docs] for changes in versioning and flags, this section focuses on how the generated code differs.

## Breaking Changes

* The credential system has been completely revamped:
    - Previously we had used `azure.common.credentials` or `msrestazure.azure_active_directory` instances, which
    are no longer supported. We now use credentials from [`azure_identity`][azure_identity_credentials] and the [`AzureKeyCredential`][azure_key_credential] from
    [`azure-core`][azure_core_library].
    - The `credentials` parameter to the service client has been renamed to `credential`
* The `config` attribute is no longer exposed on the client, and custom configurations should be passed as a kwarg. For example, we now have `Client(credential, subscription_id, enable_logging=True`).
For a complete set of supported inputs to your client, see our list of [acceptable initialization parameters in azure-core][azure_core_init_parameters].
* You can't import a `version` module anymore, use `__version__` instead. Additionally, we only generate a version file if you specify a package version on the command line (`--package-version`), or you
tell AutoRest during generation time to keep the current version file in the directory (`--keep-version-file`). See our [flag index][flag_index] for more information on these 2 flags.
* Long running operations that used to return  a `msrest.polling.LROPoller` now return a [`azure.core.polling.LROPoller`][lro_poller_docs] by default. These operations are also now prefixed with `begin_`.
* The exception tree has been simplified, and now most exceptions are an [`azure.core.exceptions.HttpResponseError`][http_response_error]. `CloudError` has been removed.
* Most of the operation kwargs have changed. The most noticeable are:
    - `raw` has been removed. We now use `cls`, which is a callback that gives access to the internal HTTP response for advanced users.
    - For a complete set of supported options, see the [acceptable parameters to operations in azure-core][azure_core_operation_parameters].

## New Features

* Type annotations using the standard `typing` library. SDKs are [`mypy`][mypy] ready!
* This client has stable and official support for async. Look in the `aio` namespace of your generated package to find the async client.
* The client now natively supports tracing libraries such as [`OpenCensus`][open_census] and [`OpenTelemetry`][open_telemetry]. Use the flag `--trace` to generate
code for this, and you can see our [tracing docs][tracing_docs] for more information.


<!-- LINKS -->
[main_docs]: https://github.com/Azure/autorest/blob/master/docs/migrate/readme.md
[azure_identity_credentials]: https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/identity/azure-identity#credentials
[azure_key_credential]: https://docs.microsoft.com/python/api/azure-core/azure.core.credentials.azurekeycredential?view=azure-python
[azure_core_library]: https://pypi.org/project/azure-core/
[azure_core_init_parameters]: https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies
[flag_index]: https://github.com/Azure/autorest/blob/master/docs/generate/flags.md
[lro_poller_docs]: https://docs.microsoft.com/python/api/azure-core/azure.core.polling.lropoller?view=azure-python
[http_response_error]: https://docs.microsoft.com/python/api/azure-core/azure.core.exceptions.httpresponseerror?view=azure-python
[azure_core_operation_parameters]: https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies
[mypy]: https://mypy.readthedocs.io/en/stable/introduction.html
[open_census]: https://opencensus.io/
[open_telemetry]: https://opentelemetry.io/
[tracing_docs]: ../client/tracing.md