# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

import glob
import sys
import subprocess
import os
import signal
from os.path import dirname, realpath
from unittest import TestLoader, TextTestRunner

from os.path import dirname, pardir, join, realpath

import requests
from requests.adapters import HTTPAdapter
from urllib3 import HTTPConnectionPool, Retry
from urllib3.poolmanager import (
    PoolManager,
    PoolKey,
    _default_key_normalizer
)

import pytest


#Ideally this would be in a common helper library shared between the tests
def start_server_process():
    cmd = "node ../../node_modules/@microsoft.azure/autorest.testserver"
    if os.name == 'nt': #On windows, subprocess creation works without being in the shell
        return subprocess.Popen(cmd)
    
    return subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid) #On linux, have to set shell=True

#Ideally this would be in a common helper library shared between the tests
def terminate_server_process(process):
    if os.name == 'nt':
        process.kill()
    else:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)  # Send the signal to all the process groups

@pytest.fixture(scope="module")
def testserver():
    """Start the Autorest testserver."""
    server = start_server_process()
    yield
    terminate_server_process(server)

# Ignore collection of async tests for Python 2
collect_ignore = []
if sys.version_info < (3,6):
    collect_ignore.append("asynctests")

# The cookie manager of the test server
class RetryForTest(Retry):
    """Wrapper for urllib3 Retry object.
    """

    def __init__(self, **kwargs):
        self.retry_cookie = None
        super(RetryForTest, self).__init__(**kwargs)

    def increment(self, method=None, url=None, response=None,
                  error=None, _pool=None, _stacktrace=None):
        increment = super(RetryForTest, self).increment(
            method, url, response, error, _pool, _stacktrace)

        if response:
            # Fixes open socket warnings in Python 3.
            response.close()
            response.release_conn()

            # Collect retry cookie - we only do this for the test server
            # at this point, unless we implement a proper cookie policy.
            increment.retry_cookie = response.getheader("Set-Cookie")
        return increment

class HTTPConnectionPoolForTest(HTTPConnectionPool):
    """Cookie logic only used for test server (localhost)"""

    def _add_test_cookie(self, retries, headers):
        host = self.host.strip('.')
        if retries.retry_cookie and host == 'localhost':
            if headers:
                headers['cookie'] = retries.retry_cookie
            else:
                self.headers['cookie'] = retries.retry_cookie

    def _remove_test_cookie(self, retries, headers):
        host = self.host.strip('.')
        if retries.retry_cookie and host == 'localhost':
            retries.retry_cookie = None
            if headers:
                del headers['cookie']
            else:
                del self.headers['cookie']

    def urlopen(self, method, url, body=None, headers=None,
                retries=None, *args, **kwargs):
        if hasattr(retries, 'retry_cookie'):
            self._add_test_cookie(retries, headers)

        response = super(HTTPConnectionPoolForTest, self).urlopen(
            method, url, body, headers, retries, *args, **kwargs)

        if hasattr(retries, 'retry_cookie'):
            self._remove_test_cookie(retries, headers)
        return response

class AdapterForTest(HTTPAdapter):

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block)
        context = {
            "scheme": "http",
            "host": "localhost",
            "port": 3000,
            "block": block,
            "maxsize": maxsize
        }
        test_hosts = [_default_key_normalizer(PoolKey, context)]
        for host in test_hosts:
            self.poolmanager.pools[host] = \
                HTTPConnectionPoolForTest(host[1], port=host[2])
        self.max_retries = RetryForTest()
        self.max_retries.status_forcelist.add(408)
        self.max_retries.status_forcelist.add(500)
        self.max_retries.status_forcelist.add(502)
        self.max_retries.status_forcelist.add(503)
        self.max_retries.status_forcelist.add(504)
        self.max_retries.method_whitelist = {'HEAD', 'GET', 'PUT', 'DELETE', 'OPTIONS', 'TRACE', 'PATCH', 'POST'}

class TestAuthentication(object):
    def signed_session(self):
        session = requests.Session()
        session.mount('http://localhost:3000/', AdapterForTest())
        return session

@pytest.fixture()
def test_server_credentials():
    return TestAuthentication()