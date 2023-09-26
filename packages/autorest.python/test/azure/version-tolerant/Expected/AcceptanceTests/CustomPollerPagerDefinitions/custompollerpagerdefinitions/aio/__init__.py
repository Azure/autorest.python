import typing
from azure.core.paging import ReturnType
from azure.core.async_paging import AsyncItemPaged
from azure.core.polling import AsyncLROPoller, AsyncPollingMethod
from azure.core.polling._poller import PollingReturnType_co



class AsyncCustomPager(AsyncItemPaged[ReturnType]):
    pass

class AsyncCustomPoller(AsyncLROPoller[PollingReturnType_co]):
    @classmethod
    def from_continuation_token(
        cls, polling_method: AsyncPollingMethod[PollingReturnType_co], continuation_token: str, **kwargs: typing.Any
    ) -> "AsyncCustomPoller[PollingReturnType_co]":
        pass

__all__ = [
    'AsyncCustomPager',
    'AsyncCustomPoller',
]
