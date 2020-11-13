from azure.core.paging import ItemPaged, ReturnType, PageIterator
from azure.core.polling import LROPoller
from azure.core.polling._poller import PollingReturnType


class CustomPager(ItemPaged[ReturnType]):
    pass

class CustomPoller(LROPoller[PollingReturnType]):
    pass


class PageIteratorWithMetadata(PageIterator):
    def _ensure_response(f):
        # pylint:disable=protected-access
        def wrapper(self, *args, **kw):
            if self._paging_method._did_a_call_already:
                self._response = self._paging_method.get_page(self.continuation_token)
                self.continuation_token, self._current_page = self._paging_method.extract_data(
                    self._response
                )
            return f(self, *args, **kw)

        return wrapper

    @_ensure_response
    def get_count(self):
        return self._paging_method.count

class PagerWithMetadata(ItemPaged[ReturnType]):
    def __init__(self, *args, **kwargs):
        super(PagerWithMetadata, self).__init__(*args, **kwargs)
        self._first_page_iterator_instance = None
        self._page_iterator_class = PageIteratorWithMetadata

    def _first_iterator_instance(self):
        if self._first_page_iterator_instance is None:
            self._first_page_iterator_instance = self.by_page()
        return self._first_page_iterator_instance

    def get_count(self):
        # type: () -> float
        return self._first_iterator_instance().get_count()

__all__ = [
    'CustomPager',
    'CustomPoller',
    'PagerWithMetadata',
]