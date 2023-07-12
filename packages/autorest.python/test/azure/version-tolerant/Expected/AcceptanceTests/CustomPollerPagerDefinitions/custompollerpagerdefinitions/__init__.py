from azure.core.paging import ItemPaged, ReturnType
from azure.core.polling import LROPoller
from azure.core.polling._poller import PollingReturnType_co


class CustomPager(ItemPaged[ReturnType]):
    pass

class CustomPoller(LROPoller[PollingReturnType_co]):
    pass

__all__ = [
    'CustomPager',
    'CustomPoller',
]
