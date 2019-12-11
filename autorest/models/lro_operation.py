import logging
from .operation import Operation
from typing import Dict, List, Any, Optional
from .parameter import Parameter
from .schema_response import SchemaResponse

_LOGGER = logging.getLogger(__name__)

class LROOperation(Operation):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        description: str,
        url: str,
        method: str,
        parameters: List[Parameter] = None,
        responses: List[SchemaResponse] = [None],
        exceptions: List[SchemaResponse] = None,
        media_types: List[str] = None,
        want_description_docstring: Optional[bool] = True,
        want_tracing: Optional[bool] = True
    ) -> None:
        super(LROOperation, self).__init__(
            yaml_data,
            name,
            description,
            url,
            method,
            parameters,
            responses,
            exceptions,
            media_types,
            want_description_docstring,
            want_tracing
        )
        self.lro_response: Optional[SchemaResponse] = None

    def set_lro_response_type(self) -> None:
        responses = {response.schema: response for response in self.responses if response.has_body}
        response_types = list(responses.values())
        if len(response_types) > 1:
            _LOGGER.warning("Multiple schema types in responses: %s", response_types)
        self.lro_response = response_types.pop() if response_types else None
