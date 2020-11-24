from azure.core.paging import ReturnType
from azure.core.async_paging import AsyncItemPaged, AsyncPageIterator
from azure.core.polling import AsyncLROPoller
from azure.core.polling._poller import PollingReturnType



class AsyncCustomPager(AsyncItemPaged[ReturnType]):
    pass

class AsyncCustomPoller(AsyncLROPoller[PollingReturnType]):
    pass

class AsyncPagerWithMetadata(AsyncItemPaged[ReturnType]):
    def __init__(self, *args, **kwargs):
        super(AsyncPagerWithMetadata, self).__init__(*args, **kwargs)
        self._paging_method = kwargs.pop("paging_method")

    def get_count(self):
        # type: () -> float
        return self._paging_method._count

__all__ = [
    'AsyncCustomPager',
    'AsyncCustomPoller',
    'AsyncPagerWithMetadata',
]