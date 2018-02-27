# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# coding: utf-8

from setuptools import setup, find_packages

NAME = "autorestrfc1123datetimetestservice"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["msrest>=0.4.22"]

setup(
    name=NAME,
    version=VERSION,
    description="AutoRestRFC1123DateTimeTestService",
    author_email="",
    url="",
    keywords=["Swagger", "AutoRestRFC1123DateTimeTestService"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Test Infrastructure for AutoRest
    """
)
