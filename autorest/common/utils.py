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

# The below code is all used to switch names to python case

def to_camel_case(name):
    name_list = re.split('[^a-zA-Z\\d]', name)
    name_list = [s[0].upper() + s[1:] if len(s) > 1 else s.upper()
                        for s in name_list]
    return ''.join(name_list)

def get_client_name(name):
    return _get_valid_python_name(name, "Model")

def get_property_name(name):
    return _get_valid_python_name(name, "Property")

def get_namespace_name(name):
    return _get_valid_python_name(name, "")

def get_enum_name(name):
    return _get_valid_python_name(name, "Enum")

def get_method_name(name):
    return _get_valid_python_name(name, "Method")

def get_parameter_name(name):
    return _get_valid_python_name(name, "Parameter")

def _get_valid_python_name(name, pad_string):
    if not name:
        return pad_string
    return _to_python_case(_get_escaped_reserved_name(_remove_invalid_python_characters(name), pad_string))

def _to_python_case(name):
    def replace_upper_characters(m):
        match_str = m.group().lower()
        if m.start() > 0 and name[m.start() - 1] == '_':
            # we are good if a '_' already exists
            return match_str
        # the first letter should not have _
        prefix = '_' if m.start() > 0 else ''

        # we will add an extra _ if there are multiple upper case chars together
        next_non_upper_case_char_location = m.start() + len(match_str)
        if (len(match_str) > 2 and len(name) - next_non_upper_case_char_location > 1 and
            name[next_non_upper_case_char_location].isalpha()):

            return prefix + match_str[: len(match_str) - 1] + '_' + match_str[len(match_str) - 1]

        return prefix + match_str

    return re.sub("[A-Z]+", replace_upper_characters, name)

def _get_escaped_reserved_name(name, append_value):
    if name is None:
        raise TypeError("The value for name can not be None")
    if append_value is None:
        raise TypeError("The value for append_value can not be None")
    if name.lower() in reserved_words:
        name += append_value
    return name

def _remove_invalid_characters(name, allowed_characters):
    name = name.replace('[]', 'Sequence')
    valid_string = ''.join([n for n in name if n.isalpha() or n.isdigit() or n in allowed_characters])
    return valid_string

def _get_valid_name(name, allowed_characters):
    correct_name = _remove_invalid_characters(name, allowed_characters)

    # here we have an empty string or a string that consists only of invalid characters
    if not correct_name or correct_name[0] in basic_latin_chars.keys():
        ret_name = ""
        for c in name:
            if c in basic_latin_chars.keys():
                ret_name += basic_latin_chars[c]
            else:
                ret_name += c
        correct_name = _remove_invalid_characters(ret_name, allowed_characters)

    if not correct_name:
        raise ValueError("Property name {} cannot be used as an identifier, as it contains only invalid characters.".format(name))


    return correct_name


def _remove_invalid_python_characters(name):
    return _get_valid_name(name.replace('-', '_'), '_')
