# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional

from msrest import Serializer

from azure.core.rest import HttpRequest

_SERIALIZER = Serializer()


def build_get_with_filter_request(
    *, filter: Optional[str] = None, top: Optional[int] = None, orderby: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    """Specify filter parameter with value '$filter=id gt 5 and name eq 'foo'&$orderby=id&$top=10'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword filter: The filter parameter with value '$filter=id gt 5 and name eq 'foo''. Default
     value is None.
    :paramtype filter: str
    :keyword top: The top parameter with value 10. Default value is None.
    :paramtype top: int
    :keyword orderby: The orderby parameter with value id. Default value is None.
    :paramtype orderby: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    _url = "/azurespecials/odata/filter"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if filter is not None:
        _query_parameters["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if top is not None:
        _query_parameters["$top"] = _SERIALIZER.query("top", top, "int")
    if orderby is not None:
        _query_parameters["$orderby"] = _SERIALIZER.query("orderby", orderby, "str")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_query_parameters, headers=_header_parameters, **kwargs)
