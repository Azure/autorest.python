# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# coding: utf-8
from setuptools import setup, find_packages


PACKAGE_NAME = "anomalydetectorclient"
version = "1.0.0b1"
setup(
    name=PACKAGE_NAME,
    version=version,
    description="AnomalyDetectorClient",
    author_email="",
    url="",
    keywords="azure, azure sdk",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "isodate<1.0.0,>=0.6.1",
        "azure-core<2.0.0,>=1.24.0",
        "typing-extensions>=4.3.0; python_version<'3.8.0'",
    ],
    long_description="""\
    The Anomaly Detector API detects anomalies automatically in time series data.
It supports two kinds of mode, one is for stateless using, another is for
stateful using. In stateless mode, there are three functionalities. Entire
Detect is for detecting the whole series with model trained by the time series,
Last Detect is detecting last point with model trained by points before.
ChangePoint Detect is for detecting trend changes in time series. In stateful
mode, user can store time series, the stored time series will be used for
detection anomalies. Under this mode, user can still use the above three
functionalities by only giving a time range without preparing time series in
client side. Besides the above three functionalities, stateful model also
provide group based detection and labeling service. By leveraging labeling
service user can provide labels for each detection result, these labels will be
used for retuning or regenerating detection models. Inconsistency detection is
a kind of group based detection, this detection will find inconsistency ones in
a set of time series. By using anomaly detector service, business customers can
discover incidents and establish a logic flow for root cause analysis.
    """,
)
