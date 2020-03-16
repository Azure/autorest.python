from wiremock.client import *

mapping = Mapping(
    priority=100,
    request=MappingRequest(
        method=HttpMethods.PUT,
        url="/multiapi/testOneEndpoint"
    ),
    response=MappingResponse(
        status=200
    ),
    persistent=False
)