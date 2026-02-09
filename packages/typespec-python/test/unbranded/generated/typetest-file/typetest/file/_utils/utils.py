# pylint: disable=line-too-long,useless-suppression
def raise_if_not_implemented(cls, abstract_methods):
    not_implemented = [f for f in abstract_methods if not callable(getattr(cls, f, None))]
    if not_implemented:

        def _not_implemented(method_name, og_name):
            def _raise(self, *args, **kwargs):
                raise NotImplementedError(
                    "Method '{}' on operation group '{}' is not implemented."
                    " Please refer to https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize.".format(
                        method_name, og_name
                    )
                )

            return _raise

        for method in not_implemented:
            setattr(cls, method, _not_implemented(method, cls.__name__))
