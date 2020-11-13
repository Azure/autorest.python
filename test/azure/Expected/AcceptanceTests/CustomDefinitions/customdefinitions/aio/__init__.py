from azure.core.paging import ReturnType
from azure.core.async_paging import AsyncItemPaged, AsyncPageIterator
from azure.core.polling import AsyncLROPoller
from azure.core.polling._poller import PollingReturnType



class AsyncCustomPager(AsyncItemPaged[ReturnType]):
    pass

class AsyncCustomPoller(AsyncLROPoller[PollingReturnType]):
    pass

class AsyncPageIteratorWithMetadata(AsyncPageIterator):
    def _ensure_response(f):
        # pylint:disable=protected-access
        async def wrapper(self, *args, **kw):
            if not self._paging_method.did_a_call_already:
                self._response = await self._paging_method.get_page(self.continuation_token, self._initial_request)
                self.continuation_token, self._current_page = self._paging_method.extract_data(
                    self._response
                )
            return await f(self, *args, **kw)

        return wrapper

    @_ensure_response
    async def get_count(self):
        return self._paging_method.count

class AsyncPagerWithMetadata(AsyncItemPaged[ReturnType]):
    def __init__(self, *args, **kwargs):
        super(AsyncPagerWithMetadata, self).__init__(*args, **kwargs)
        self._first_page_iterator_instance = None
        self._page_iterator_class = AsyncPageIteratorWithMetadata

    def _first_iterator_instance(self):
        if self._first_page_iterator_instance is None:
            self._first_page_iterator_instance = self.by_page()
        return self._first_page_iterator_instance

    async def get_count(self):
        # type: () -> float
        return await self._first_iterator_instance().get_count()

__all__ = [
    'AsyncCustomPager',
    'AsyncCustomPoller',
    'AsyncPagerWithMetadata',
]