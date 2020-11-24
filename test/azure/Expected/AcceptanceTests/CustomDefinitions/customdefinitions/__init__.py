from azure.core.paging import ItemPaged, ReturnType, PageIterator
from azure.core.paging_method import BasicPagingMethod
from azure.core.polling import LROPoller
from azure.core.polling._poller import PollingReturnType


class CustomPager(ItemPaged[ReturnType]):
    pass

class CustomPoller(LROPoller[PollingReturnType]):
    pass

class PagerWithMetadata(ItemPaged[ReturnType]):
    def __init__(self, *args, **kwargs):
        super(PagerWithMetadata, self).__init__(*args, **kwargs)
        self._paging_method = kwargs.pop("paging_method")

    def get_count(self):
        # type: () -> float
        return self._paging_method._count

class MyPagingMethod(BasicPagingMethod):
    pass

__all__ = [
    'CustomPager',
    'CustomPoller',
    'PagerWithMetadata',
    'MyPagingMethod',
]