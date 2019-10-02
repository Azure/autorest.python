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
        self.basic_latin_chars = {
            ' ': "Space",
            '!': "ExclamationMark",
            '"': "QuotationMark",
            '#': "NumberSign",
            '$': "DollarSign",
            '%': "PercentSign",
            '&': "Ampersand",
            "'": "Apostrophe",
            '(': "LeftParenthesis",
            ')': "RightParenthesis",
            '*': "Asterisk",
            '+': "PlusSign",
            ',': "Comma",
            '-': "HyphenMinus",
            '.': "FullStop",
            '/': "Slash",
            '0': "Zero",
            '1': "One",
            '2': "Two",
            '3': "Three",
            '4': "Four",
            '5': "Five",
            '6': "Six",
            '7': "Seven",
            '8': "Eight",
            '9': "Nine",
            ':': "Colon",
            ';': "Semicolon",
            '<': "LessThanSign",
            '=': "EqualSign",
            '>': "GreaterThanSign",
            '?': "QuestionMark",
            '@': "AtSign",
            '[': "LeftSquareBracket",
            '\\': "Backslash",
            ']': "RightSquareBracket",
            '^': "CircumflexAccent",
            '`': "GraveAccent",
            '{': "LeftCurlyBracket",
            '|': "VerticalBar",
            '}': "RightCurlyBracket",
            '~': "Tilde"
        }

    def _to_python_case(cls, name):
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

    def _get_escaped_reserved_name(cls, name, append_value):
        if name is None:
            raise TypeError("The value for name can not be None")
        if append_value is None:
            raise TypeError("The value for append_value can not be None")
        if name.lower() in cls.reserved_words:
            name += append_value
        return name

    def _remove_invalid_characters(cls, name, allowed_characters):
        name = name.replace('[]', 'Sequence')
        valid_string = ''.join([n for n in name if n.isalpha() or n.isdigit() or n in allowed_characters])
        return valid_string

    def _get_valid_name(cls, name, allowed_characters):
        correct_name = cls._remove_invalid_characters(name, allowed_characters)

        # here we have an empty string or a string that consists only of invalid characters
        if not correct_name or correct_name[0] in cls.basic_latin_chars.keys():
            ret_name = ""
            for c in name:
                if c in cls.basic_latin_chars.keys():
                    ret_name += cls.basic_latin_chars[c]
                else:
                    ret_name += c
            correct_name = cls._remove_invalid_characters(ret_name, allowed_characters)

        if not correct_name:
            raise ValueError("Property name {} cannot be used as an identifier, as it contains only invalid characters.".format(name))


        return correct_name

    def _remove_invalid_python_characters(cls, name):
        if not name:
            raise TypeError("Property name {} cannot be used as an identifier, as it contains only invalid characters.".format(name))
        return cls._get_valid_name(name.replace('-', '_'), '_')


    def get_valid_python_name(cls, name, pad_string):
        return cls._to_python_case(cls._get_escaped_reserved_name(cls._remove_invalid_python_characters(name), pad_string))
