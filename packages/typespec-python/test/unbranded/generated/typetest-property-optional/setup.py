# coding=utf-8

# coding: utf-8

import os
import re
from setuptools import setup, find_packages


PACKAGE_NAME = "typetest-property-optional"
PACKAGE_PPRINT_NAME = "Typetest Property Optional"

# a-b-c => a/b/c
package_folder_path = PACKAGE_NAME.replace("-", "/")

# Version extraction inspired from 'requests'
with open(os.path.join(package_folder_path, "_version.py"), "r") as fd:
    version = re.search(r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("Cannot find version information")


setup(
    name=PACKAGE_NAME,
    version=version,
    description=" {} Client Library for Python".format(PACKAGE_PPRINT_NAME),
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    license="MIT License",
    author=" Corporation",
    author_email="azpysdkhelp@microsoft.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
    zip_safe=False,
    packages=find_packages(
        exclude=[
            "tests",
            # Exclude packages that will be covered by PEP420 or nspkg
            "typetest",
            "typetest.property",
        ]
    ),
    include_package_data=True,
    package_data={
        "pytyped": ["py.typed"],
    },
    install_requires=[
        "isodate<1.0.0,>=0.6.1",
        "corehttp",
    ],
    python_requires=">=3.7",
)
