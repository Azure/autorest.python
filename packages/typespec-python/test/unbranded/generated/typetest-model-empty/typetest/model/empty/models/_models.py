# coding=utf-8
# pylint: disable=too-many-lines


from .. import _model_base


class EmptyInput(_model_base.Model):
    """Empty model used in operation parameters."""


class EmptyInputOutput(_model_base.Model):
    """Empty model used in both parameter and return type."""


class EmptyOutput(_model_base.Model):
    """Empty model used in operation return type."""
