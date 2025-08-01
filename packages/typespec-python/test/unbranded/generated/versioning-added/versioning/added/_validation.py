import functools


def api_version_validation(**kwargs):
    params_added_on = kwargs.pop("params_added_on", {})
    method_added_on = kwargs.pop("method_added_on", "")
    api_versions_list = kwargs.pop("api_versions_list", [])

    def _index_with_default(value: str, default: int = -1) -> int:
        """Get the index of value in lst, or return default if not found.

        :param value: The value to search for in the api_versions_list.
        :type value: str
        :param default: The default value to return if the value is not found.
        :type default: int
        :return: The index of the value in the list, or the default value if not found.
        :rtype: int
        """
        try:
            return api_versions_list.index(value)
        except ValueError:
            return default

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # this assumes the client has an _api_version attribute
                client = args[0]
                client_api_version = client._config.api_version  # pylint: disable=protected-access
            except AttributeError:
                return func(*args, **kwargs)

            if _index_with_default(method_added_on) > _index_with_default(client_api_version):
                raise ValueError(
                    f"'{func.__name__}' is not available in API version "
                    f"{client_api_version}. Pass service API version {method_added_on} or newer to your client."
                )

            unsupported = {
                parameter: api_version
                for api_version, parameters in params_added_on.items()
                for parameter in parameters
                if parameter in kwargs and _index_with_default(api_version) > _index_with_default(client_api_version)
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
