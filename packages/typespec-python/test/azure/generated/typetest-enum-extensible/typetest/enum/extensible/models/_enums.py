# coding=utf-8
None

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class DaysOfWeekExtensibleEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Days of the week."""

    MONDAY = "Monday"
    """Monday."""
    TUESDAY = "Tuesday"
    """Tuesday."""
    WEDNESDAY = "Wednesday"
    """Wednesday."""
    THURSDAY = "Thursday"
    """Thursday."""
    FRIDAY = "Friday"
    """Friday."""
    SATURDAY = "Saturday"
    """Saturday."""
    SUNDAY = "Sunday"
    """Sunday."""
