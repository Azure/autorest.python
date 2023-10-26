# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools


def api_version_validation(**kwargs):
    params_added_on = kwargs.pop("params_added_on", {})
    method_added_on = kwargs.pop("method_added_on", "")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # this assumes the client has an _api_version attribute
                client = args[0]
                client_api_version = client._config.api_version  # pylint: disable=protected-access
            except AttributeError:
                return func(*args, **kwargs)

            if method_added_on > client_api_version:
                raise ValueError(
                    f"'{func.__name__}' is not available in API version "
                    f"{client_api_version}. Pass service API version {method_added_on} or newer to your client."
                )

            unsupported = {
                parameter: api_version
                for api_version, parameters in params_added_on.items()
                for parameter in parameters
                if parameter in kwargs and api_version > client_api_version
            }
            if unsupported:
                raise ValueError(
                    "".join(
                        [
                            f"'{param}' is not available in API version {client_api_version}. "
                            f"Use service API version {version} or newer.\n"
                            for param, version in unsupported.items()
                        ]
                    )
                )
            return func(*args, **kwargs)

        return wrapper

    return decorator
