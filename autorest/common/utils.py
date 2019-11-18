import logging
import re

from .python_mappings import primary_types, basic_latin_chars, reserved_words


_LOGGER = logging.getLogger(__name__)


def to_python_type(original_type):
    try:
        return primary_types[original_type]
    except KeyError as e:
        _LOGGER.critical("The type you are trying to convert to Python is not a known type")
        return "KEYERROR" # FIXME
    except:
        # one entry in the swagger has three types under type[]
        # https://github.com/Azure/perks/blob/master/codemodel/.resources/all-in-one/json/code-model.json#L882
        return "string"
