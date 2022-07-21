# coding=utf-8
#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------
# coding: utf-8

from setuptools import setup, find_packages

NAME = "multiapicredentialdefaultpolicy"
VERSION = "0.1.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["msrest>=0.6.0", "azure-core<2.0.0,>=1.2.0"]

setup(
    name=NAME,
    version=VERSION,
    description="multiapi with a non BearerTokenCredentialPolicy auth policy",
    author_email="",
    url="",
    keywords=["Swagger", "multiapicredentialdefaultpolicy"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.
    """
)
