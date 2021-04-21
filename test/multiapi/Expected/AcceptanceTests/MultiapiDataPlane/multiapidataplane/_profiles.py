#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------
from enum import Enum

class ProfileDefinition(object):
    """Allow to define a custom Profile definition.

    Note::

    The dict format taken as input is yet to be confirmed and should
    *not* be considered as stable in the current implementation.

    :param dict profile_dict: A profile dictionnary
    :param str label: A label for pretty printing
    """
    def __init__(self, profile_dict, label=None):
        self._profile_dict = profile_dict
        self._label = label

    @property
    def label(self):
        """The label associated to this profile definition.
        """
        return self._label

    def __repr__(self):
        return self._label if self._label else self._profile_dict.__repr__()

    def get_profile_dict(self):
        """Return the current profile dict.

        This is internal information, and content should not be considered stable.
        """
        return self._profile_dict

def _is_profile_definition(profile):
    """Checks whether I have the properties / methods of ProfileDefinition"""
    return hasattr(profile, "label") and callable(getattr(profile, "get_profile_dict", None))

def _is_known_profiles(profile):
    """Checks whether I have the properties of KnownProfiles"""
    return all([
        callable(getattr(profile, attr, None)) for attr in ["use", "definition", "from_name"]
    ]) and all([
        hasattr(profile, attr) for attr in ["latest", "default"]
    ])

class DefaultProfile(object):
    """Store a default profile.

    :var ProfileDefinition profile: The default profile as class attribute
    """
    profile = None

    def use(self, profile):
        """Define a new default profile."""
        if not _is_profile_definition(profile) and not _is_known_profiles(profile):
            raise ValueError("Can only set as default a ProfileDefinition or a KnownProfiles")
        type(self).profile = profile

    def definition(self):
        return type(self).profile

class KnownProfiles(Enum):
    default = DefaultProfile()
    latest = ProfileDefinition(None, "latest")

    def use(self, profile):
        if self is not type(self).default:
            raise ValueError("use can only be used for `default` profile")
        self.value.use(profile)

    def definition(self):
        if self is not type(self).default:
            raise ValueError("use can only be used for `default` profile")
        return self.value.definition()

    @classmethod
    def from_name(cls, profile_name):
        if profile_name == "default":
            return cls.default
        for profile in cls:
            if _is_profile_definition(profile.value) and profile.value.label == profile_name:
                return profile
        raise ValueError("No profile called {}".format(profile_name))


class InvalidMultiApiClientError(Exception):
    """If the mixin is not used with a compatible class.
    """
    pass


class MultiApiClientMixin(object):
    """Mixin that contains multi-api version profile management.

    To use this mixin, a client must define two class attributes:
    - LATEST_PROFILE : a ProfileDefinition correspond to latest profile
    - _PROFILE_TAG : a tag that filter a full profile for this particular client

    This should not be used directly and will only provide private methods.
    """

    def __init__(self, *args, **kwargs):
        # Consume "api_version" and "profile", to avoid sending them to base class
        api_version = kwargs.pop("api_version", None)
        self._input_profile = False

        # Can't do "super" call here all the time, or I would break old client with:
        # TypeError: object.__init__() takes no parameters
        # So I try to detect if I correctly use this class as a Mixin, or the messed-up
        # approach like before. If I think it's the messed-up old approach,
        # don't call super
        if args or "creds" in kwargs or "config" in kwargs:
            super(MultiApiClientMixin, self).__init__(*args, **kwargs)

        try:
            type(self).LATEST_PROFILE
        except AttributeError:
            raise InvalidMultiApiClientError("To use this mixin, main client MUST define LATEST_PROFILE class attribute")

        try:
            type(self)._PROFILE_TAG
        except AttributeError:
            raise InvalidMultiApiClientError("To use this mixin, main client MUST define _PROFILE_TAG class attribute")

        profile = kwargs.pop("profile", None)
        if profile:
            self._input_profile = True
            try:
                import azure.profiles
            except ImportError:
                raise TypeError("In order to pass in a profile, you have to pip install azure-common")

        if api_version and profile:
            raise ValueError("Cannot use api-version and profile parameters at the same time")

        if not profile:
            profile = KnownProfiles.default
            profile.use(KnownProfiles.latest)

        if api_version:
            self.profile = ProfileDefinition({
                self._PROFILE_TAG: {
                    None: api_version
                }},
                self._PROFILE_TAG + " " + api_version
            )
        elif isinstance(profile, dict):
            self.profile = ProfileDefinition({
                self._PROFILE_TAG: profile,
                },
                self._PROFILE_TAG + " dict"
            )
            if api_version:
                self.profile._profile_dict[self._PROFILE_TAG][None] = api_version
        else:
            self.profile = profile

    def _get_api_version(self, operation_group_name):
        current_profile = self.profile
        try:
            if current_profile.name == "default" or current_profile.name == "latest":
                current_profile = self.LATEST_PROFILE
        except AttributeError:
            pass

        try:
            current_profile = current_profile.value
        except AttributeError:
            if _is_profile_definition(current_profile):
                pass
            else:
                raise ValueError("Cannot determine a ProfileDefinition from {}".format(self.profile))

        local_profile_dict = current_profile.get_profile_dict()
        if self._PROFILE_TAG not in local_profile_dict:
            raise ValueError("This profile doesn't define {}".format(self._PROFILE_TAG))

        local_profile = local_profile_dict[self._PROFILE_TAG]
        if operation_group_name in local_profile:
            return local_profile[operation_group_name]
        try:
            return local_profile[None]
        except KeyError:
            raise ValueError("This profile definition does not contain a default API version")