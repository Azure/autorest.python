# coding=utf-8
#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------
# coding: utf-8

from setuptools import setup, find_packages

NAME = "multiapicombiner"
VERSION = "0.1.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "isodate<1.0.0,>=0.6.1",
    "azure-common~=1.1",
    "azure-mgmt-core>=1.3.2,<2.0.0",
    "typing-extensions>=4.3.0; python_version<'3.8.0'",
]

setup(
    name=NAME,
    version=VERSION,
    description="multiapicombiner",
    author_email="",
    url="",
    keywords=["Swagger", "multiapicombiner"],
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
