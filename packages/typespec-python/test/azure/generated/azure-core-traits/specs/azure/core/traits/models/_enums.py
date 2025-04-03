# coding=utf-8

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class RepeatabilityResult(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Repeatability Result header options."""

    ACCEPTED = "accepted"
    """If the request was accepted and the server guarantees that the server state reflects a single
    execution of the operation."""
    REJECTED = "rejected"
    """If the request was rejected because the combination of Repeatability-First-Sent and
    Repeatability-Request-ID were invalid
    or because the Repeatability-First-Sent value was outside the range of values held by the
    server."""
