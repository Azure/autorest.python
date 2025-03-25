# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft Corporation (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from setuptools import setup, find_packages


PACKAGE_NAME = "custompollerpager"
version = "0.1.0"


setup(
    name=PACKAGE_NAME,
    version=version,
    description="custompollerpager",
    author_email="",
    url="",
    keywords="azure, azure sdk",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "msrest>=0.7.1",
        "azure-mgmt-core>=1.3.2",
        "typing-extensions>=4.6.0",
    ],
    long_description="""\
    Long-running Operation for AutoRest.
    """,
)
