﻿# --------------------------------------------------------------------------
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


def load_tests(test_loader, tests, pattern):
    cwd = dirname(realpath(__file__))
    alltests = glob.glob(os.path.join(cwd, "*_tests.py"))
    test_modules = sorted([os.path.basename(p).rstrip('.py') for p in alltests])
    return test_loader.loadTestsFromNames(test_modules)

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
    
if __name__ == '__main__':    
    server = start_server_process()
    try:
        test_loader = TestLoader()
        suite = load_tests(test_loader, None, None)

        runner = TextTestRunner(verbosity=2)

        result = runner.run(suite)
        if not result.wasSuccessful():
            sys.exit(1)

    finally:
        print("Killing server")
        terminate_server_process(server)
        print("Done killing server")
