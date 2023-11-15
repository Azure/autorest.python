import os
import sys
import subprocess
import time
import argparse

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..", ".."))


# from https://stackoverflow.com/a/43357954/1233374
# allow for boolean arguments as switches or with values
# parser.add_argument("--nice", type=str2bool, nargs='?',
#                     const=True, default=False,
#                     help="Activate nice mode.")
# --nice, --nice=true, --nice 1
# --nice false, --nice no, --nice 0
def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")

def is_pipeline_build():
    return not not os.environ.get("TF_BUILD", "")

def call(cmd:str, cwd=root_dir, suppress_failures=False, capture_output=False):
    print("\n============================================================")
    print(f"From {cwd}\n> {cmd}")
    print("============================================================", flush=True)

    start_time = time.time()

    process = subprocess.run(
        cmd,
        cwd=cwd,
        shell=True,
        text=True,
        stdout=subprocess.PIPE if capture_output else None,
        stderr=subprocess.STDOUT if capture_output else None,
    )

    returncode = process.returncode

    if(capture_output):
        print(process.stdout.rstrip(), flush=True)

    elapsed_time = time.time() - start_time

    command_failed = returncode != 0 and not suppress_failures
    
    print("------------------------------------------------------------")
    if command_failed:
        print(f"##[error]Command failed: {cmd}")
    else:
        print(f"End: {cmd}")
    print(f"Exit code {returncode}, Duration: {elapsed_time:.3f}s")
    print("------------------------------------------------------------\n", flush=True)

    if command_failed:
        sys.exit(returncode)

    return process.stdout
