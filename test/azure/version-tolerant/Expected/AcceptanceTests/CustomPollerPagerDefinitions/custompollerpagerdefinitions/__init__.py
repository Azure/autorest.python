from azure.core.paging import ItemPaged, ReturnType
from azure.core.polling import LROPoller
from azure.core.polling._poller import PollingReturnType


class CustomPager(ItemPaged[ReturnType]):
    pass

class CustomPoller(LROPoller[PollingReturnType]):
    pass

__all__ = [
    'CustomPager',
    'CustomPoller',
]
