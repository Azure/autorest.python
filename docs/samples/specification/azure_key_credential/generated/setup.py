# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# coding: utf-8
from setuptools import setup, find_packages


PACKAGE_NAME = "azure-key-credential-sample"
version = "0.1.0"
setup(
    name=PACKAGE_NAME,
    version=version,
    description="azure-key-credential-sample",
    author_email="",
    url="",
    keywords="azure, azure sdk",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "msrest>=0.6.21",
        "azure-core<2.0.0,>=1.23.0",
    ],
    long_description="""\
    Test Infrastructure for AutoRest.
    """
)
