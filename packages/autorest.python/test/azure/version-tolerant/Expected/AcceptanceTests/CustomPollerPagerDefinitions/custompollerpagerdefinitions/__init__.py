import typing
from azure.core.paging import ItemPaged, ReturnType
from azure.core.polling import LROPoller, PollingMethod
from azure.core.polling._poller import PollingReturnType_co


class CustomPager(ItemPaged[ReturnType]):
    pass

class CustomPoller(LROPoller[PollingReturnType_co]):
    @classmethod
    def from_continuation_token(
        cls, polling_method: PollingMethod[PollingReturnType_co], continuation_token: str, **kwargs: typing.Any
    ) -> "CustomPoller[PollingReturnType_co]":
        pass

__all__ = [
    'CustomPager',
    'CustomPoller',
]
