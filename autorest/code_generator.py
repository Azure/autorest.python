from pathlib import Path
import sys

import yaml

from jinja2 import Template, PackageLoader, Environment

from .jinja2_model import CodeModel
from .jsonrpc_server import write_file

def generate(yaml_model_file, session_id=None):

    env = Environment(
        loader=PackageLoader('autorest', 'templates'),
        keep_trailing_newline=True
    )

    # Parse the received YAML
    yaml_code_model = yaml.safe_load(yaml_model_file)

    # Create a code model
    code_model = CodeModel()
    code_model.client_name = yaml_code_model["info"]["title"]
    code_model.api_version = yaml_code_model["info"]["version"]

    # Generate the service client content
    template = env.get_template("service_client.py.jinja2")
    service_client = template.render(code_model=code_model)

    # Write it
    write_file(session_id, "service_client.py", service_client)


def main(yaml_model_file):
    generate(yaml_model_file)

if __name__ == "__main__":
    main(sys.argv[1])