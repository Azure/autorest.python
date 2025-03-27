# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from setuptools import setup, find_packages


PACKAGE_NAME = "autorestparameterflattening"
version = "0.1.0"


setup(
    name=PACKAGE_NAME,
    version=version,
    description="AutoRestParameterFlattening",
    author_email="",
    url="",
    keywords="azure, azure sdk",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "isodate>=0.6.1",
        "azure-core>=1.30.0",
        "typing-extensions>=4.6.0",
    ],
    long_description="""\
    Resource Flattening for AutoRest.
    """,
)
