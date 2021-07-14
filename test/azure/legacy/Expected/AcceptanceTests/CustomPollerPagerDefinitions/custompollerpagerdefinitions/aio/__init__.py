from azure.core.paging import ReturnType
from azure.core.async_paging import AsyncItemPaged
from azure.core.polling import AsyncLROPoller
from azure.core.polling._poller import PollingReturnType



class AsyncCustomPager(AsyncItemPaged[ReturnType]):
    pass

class AsyncCustomPoller(AsyncLROPoller[PollingReturnType]):
    pass

__all__ = [
    'AsyncCustomPager',
    'AsyncCustomPoller',
]