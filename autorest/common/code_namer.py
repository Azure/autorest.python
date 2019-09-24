import re
class CodeNamer:
    def __init__(self):
        self.reserved_words = [
            "and","as","assert","break","class","continue",
            "def","del","elif","else","except","exec",
            "finally","for","from","global","if","import",
            "in","is","lambda","not","or","pass",
            "print","raise","return","try","while","with",
            "yield", "async", "await",
            "int","bool","bytearray","date","datetime","float",
            "long","object","decimal","str","timedelta", "mro"
        ]

    def to_python_case(name):
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

    def _remove_invalid_characters(name, allowed_characters):
        valid_string = name.replace('[]', 'Sequence')
        for c in name:
            if c.isalpha() or c.isdigit() or c in allowed_characters:
                valid_string.append(c)
        return valid_string

    def _get_valid_name(name, allowed_characters):
        correct_name = self._remove_invalid_characters(name, allowed_characters)

        # here we have only letters and digits or an empty string
        # TODO

        return correct_name


    def remove_invalid_python_characters(name):
        if not name:
            raise TypeError("Property name {} cannot be used as an identifier, as it contains only invalid characters.")
        return self._get_valid_name(name.replace('-', '_'), '_')