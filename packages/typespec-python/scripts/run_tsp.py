# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import sys
import logging
from pathlib import Path
from pygen import preprocess, codegen
from pygen.utils import parse_args
from package_manager import create_venv_with_package_manager

_ROOT_DIR = Path(__file__).parent.parent

_LOGGER = logging.getLogger(__name__)

if __name__ == "__main__":
    venv_path = _ROOT_DIR / "venv"
    venv_preexists = venv_path.exists()

    assert venv_preexists  # Otherwise install was not done

    venv_context = create_venv_with_package_manager(venv_path)

    if "--debug" in sys.argv or "--debug=true" in sys.argv:
        try:
            import debugpy  # pylint: disable=import-outside-toplevel
        except ImportError:
            raise SystemExit("Please install ptvsd in order to use VSCode debugging")

        # 5678 is the default attach port in the VS Code debug configurations
        debugpy.listen(("localhost", 5678))
        debugpy.wait_for_client()
        breakpoint()  # pylint: disable=undefined-variable

    # run
    args, unknown_args = parse_args()
    preprocess.PreProcessPlugin(output_folder=args.output_folder, cadl_file=args.cadl_file, **unknown_args).process()
    codegen.CodeGenerator(output_folder=args.output_folder, cadl_file=args.cadl_file, **unknown_args).process()
