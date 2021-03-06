# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class ModelAsStringNoRequiredOneValueDefault(msrest.serialization.Model):
    """ModelAsStringNoRequiredOneValueDefault.

    :param parameter:  Possible values include: "value1".
    :type parameter: str or ~constants.models.ModelAsStringNoRequiredOneValueDefaultEnum
    """

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(ModelAsStringNoRequiredOneValueDefault, self).__init__(**kwargs)
        self.parameter = kwargs.get("parameter", "value1")


class ModelAsStringNoRequiredOneValueNoDefault(msrest.serialization.Model):
    """ModelAsStringNoRequiredOneValueNoDefault.

    :param parameter:  Possible values include: "value1".
    :type parameter: str or ~constants.models.ModelAsStringNoRequiredOneValueNoDefaultEnum
    """

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(ModelAsStringNoRequiredOneValueNoDefault, self).__init__(**kwargs)
        self.parameter = kwargs.get("parameter", None)


class ModelAsStringNoRequiredTwoValueDefault(msrest.serialization.Model):
    """ModelAsStringNoRequiredTwoValueDefault.

    :param parameter:  Possible values include: "value1", "value2".
    :type parameter: str or ~constants.models.ModelAsStringNoRequiredTwoValueDefaultEnum
    """

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(ModelAsStringNoRequiredTwoValueDefault, self).__init__(**kwargs)
        self.parameter = kwargs.get("parameter", "value1")


class ModelAsStringNoRequiredTwoValueNoDefault(msrest.serialization.Model):
    """ModelAsStringNoRequiredTwoValueNoDefault.

    :param parameter:  Possible values include: "value1", "value2".
    :type parameter: str or ~constants.models.ModelAsStringNoRequiredTwoValueNoDefaultEnum
    """

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(ModelAsStringNoRequiredTwoValueNoDefault, self).__init__(**kwargs)
        self.parameter = kwargs.get("parameter", None)


class ModelAsStringRequiredOneValueDefault(msrest.serialization.Model):
    """ModelAsStringRequiredOneValueDefault.

    All required parameters must be populated in order to send to Azure.

    :param parameter: Required.  Possible values include: "value1".
    :type parameter: str or ~constants.models.ModelAsStringRequiredOneValueDefaultEnum
    """

    _validation = {
        "parameter": {"required": True},
    }

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(ModelAsStringRequiredOneValueDefault, self).__init__(**kwargs)
        self.parameter = kwargs.get("parameter", "value1")


class ModelAsStringRequiredOneValueNoDefault(msrest.serialization.Model):
    """ModelAsStringRequiredOneValueNoDefault.

    All required parameters must be populated in order to send to Azure.

    :param parameter: Required.  Possible values include: "value1".
    :type parameter: str or ~constants.models.ModelAsStringRequiredOneValueNoDefaultEnum
    """

    _validation = {
        "parameter": {"required": True},
    }

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(ModelAsStringRequiredOneValueNoDefault, self).__init__(**kwargs)
        self.parameter = kwargs["parameter"]


class ModelAsStringRequiredTwoValueDefault(msrest.serialization.Model):
    """ModelAsStringRequiredTwoValueDefault.

    All required parameters must be populated in order to send to Azure.

    :param parameter: Required.  Possible values include: "value1", "value2".
    :type parameter: str or ~constants.models.ModelAsStringRequiredTwoValueDefaultEnum
    """

    _validation = {
        "parameter": {"required": True},
    }

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(ModelAsStringRequiredTwoValueDefault, self).__init__(**kwargs)
        self.parameter = kwargs.get("parameter", "value1")


class ModelAsStringRequiredTwoValueNoDefault(msrest.serialization.Model):
    """ModelAsStringRequiredTwoValueNoDefault.

    All required parameters must be populated in order to send to Azure.

    :param parameter: Required.  Possible values include: "value1", "value2".
    :type parameter: str or ~constants.models.ModelAsStringRequiredTwoValueNoDefaultEnum
    """

    _validation = {
        "parameter": {"required": True},
    }

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(ModelAsStringRequiredTwoValueNoDefault, self).__init__(**kwargs)
        self.parameter = kwargs["parameter"]


class NoModelAsStringNoRequiredOneValueDefault(msrest.serialization.Model):
    """NoModelAsStringNoRequiredOneValueDefault.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar parameter:  Default value: "value1".
    :vartype parameter: str
    """

    _validation = {
        "parameter": {"constant": True},
    }

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
    }

    parameter = "value1"

    def __init__(self, **kwargs):
        super(NoModelAsStringNoRequiredOneValueDefault, self).__init__(**kwargs)


class NoModelAsStringNoRequiredOneValueNoDefault(msrest.serialization.Model):
    """NoModelAsStringNoRequiredOneValueNoDefault.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar parameter:  Default value: "value1".
    :vartype parameter: str
    """

    _validation = {
        "parameter": {"constant": True},
    }

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
    }

    parameter = "value1"

    def __init__(self, **kwargs):
        super(NoModelAsStringNoRequiredOneValueNoDefault, self).__init__(**kwargs)


class NoModelAsStringNoRequiredTwoValueDefault(msrest.serialization.Model):
    """NoModelAsStringNoRequiredTwoValueDefault.

    :param parameter:  Possible values include: "value1", "value2".
    :type parameter: str or ~constants.models.NoModelAsStringNoRequiredTwoValueDefaultEnum
    """

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(NoModelAsStringNoRequiredTwoValueDefault, self).__init__(**kwargs)
        self.parameter = kwargs.get("parameter", "value1")


class NoModelAsStringNoRequiredTwoValueNoDefault(msrest.serialization.Model):
    """NoModelAsStringNoRequiredTwoValueNoDefault.

    :param parameter:  Possible values include: "value1", "value2".
    :type parameter: str or ~constants.models.NoModelAsStringNoRequiredTwoValueNoDefaultEnum
    """

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(NoModelAsStringNoRequiredTwoValueNoDefault, self).__init__(**kwargs)
        self.parameter = kwargs.get("parameter", None)


class NoModelAsStringRequiredOneValueDefault(msrest.serialization.Model):
    """NoModelAsStringRequiredOneValueDefault.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar parameter: Required.  Default value: "value1".
    :vartype parameter: str
    """

    _validation = {
        "parameter": {"required": True, "constant": True},
    }

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
    }

    parameter = "value1"

    def __init__(self, **kwargs):
        super(NoModelAsStringRequiredOneValueDefault, self).__init__(**kwargs)


class NoModelAsStringRequiredOneValueNoDefault(msrest.serialization.Model):
    """NoModelAsStringRequiredOneValueNoDefault.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar parameter: Required.  Default value: "value1".
    :vartype parameter: str
    """

    _validation = {
        "parameter": {"required": True, "constant": True},
    }

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
    }

    parameter = "value1"

    def __init__(self, **kwargs):
        super(NoModelAsStringRequiredOneValueNoDefault, self).__init__(**kwargs)


class NoModelAsStringRequiredTwoValueDefault(msrest.serialization.Model):
    """NoModelAsStringRequiredTwoValueDefault.

    All required parameters must be populated in order to send to Azure.

    :param parameter: Required.  Possible values include: "value1", "value2".
    :type parameter: str or ~constants.models.NoModelAsStringRequiredTwoValueDefaultEnum
    """

    _validation = {
        "parameter": {"required": True},
    }

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(NoModelAsStringRequiredTwoValueDefault, self).__init__(**kwargs)
        self.parameter = kwargs.get("parameter", "value1")


class NoModelAsStringRequiredTwoValueNoDefault(msrest.serialization.Model):
    """NoModelAsStringRequiredTwoValueNoDefault.

    All required parameters must be populated in order to send to Azure.

    :param parameter: Required.  Possible values include: "value1", "value2".
    :type parameter: str or ~constants.models.NoModelAsStringRequiredTwoValueNoDefaultEnum
    """

    _validation = {
        "parameter": {"required": True},
    }

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(NoModelAsStringRequiredTwoValueNoDefault, self).__init__(**kwargs)
        self.parameter = kwargs["parameter"]
