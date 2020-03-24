import pytest
import os
import subprocess
import signal
from azure.core.pipeline.policies import SansIOHTTPPolicy

cwd = os.path.dirname(os.path.realpath(__file__))

#Ideally this would be in a common helper library shared between the tests
def start_server_process():
    cmd = "node {}/../../../node_modules/@microsoft.azure/autorest.testserver".format(cwd)
    if os.name == 'nt': #On windows, subprocess creation works without being in the shell
        return subprocess.Popen(cmd)

    return subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid) #On linux, have to set shell=True

#Ideally this would be in a common helper library shared between the tests
def terminate_server_process(process):
    if os.name == 'nt':
        process.kill()
    else:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)  # Send the signal to all the process groups

@pytest.fixture(scope="session")
def testserver():
    """Start the Autorest testserver."""
    server = start_server_process()
    yield
    terminate_server_process(server)

@pytest.fixture
def credential():
    class FakeCredential:
        pass
    return FakeCredential()

@pytest.fixture
def authentication_policy():
    return SansIOHTTPPolicy()