# coding=utf-8

from enum import Enum
from corehttp.utils import CaseInsensitiveEnumMeta


class ExtensibleString(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Verify enum member names that are special words using extensible enum (union)."""

    AND = "and"
    AS = "as"
    ASSERT = "assert"
    ASYNC = "async"
    AWAIT = "await"
    BREAK = "break"
    CLASS = "class"
    CONSTRUCTOR = "constructor"
    CONTINUE = "continue"
    DEF = "def"
    DEL = "del"
    ELIF = "elif"
    ELSE = "else"
    EXCEPT = "except"
    EXEC = "exec"
    FINALLY = "finally"
    FOR = "for"
    FROM = "from"
    GLOBAL = "global"
    IF = "if"
    IMPORT = "import"
    IN = "in"
    IS = "is"
    LAMBDA = "lambda"
    NOT = "not"
    OR = "or"
    PASS = "pass"
    RAISE = "raise"
    RETURN = "return"
    TRY = "try"
    WHILE = "while"
    WITH = "with"
    YIELD = "yield"
