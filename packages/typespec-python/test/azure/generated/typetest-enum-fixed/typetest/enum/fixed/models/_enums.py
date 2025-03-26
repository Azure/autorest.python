# coding=utf-8

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class DaysOfWeekEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
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
