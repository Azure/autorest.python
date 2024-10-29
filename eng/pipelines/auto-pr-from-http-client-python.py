#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import os
import argparse
from pathlib import Path
import logging
import json
import re
from github import Github, Auth
from functools import wraps
from subprocess import check_call, CalledProcessError
from datetime import datetime

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def log_call(command: str):
    logger.info(f"=== {command} ===")
    check_call(command, shell=True)


def return_origin_path(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        current_path = os.getcwd()
        result = func(*args, **kwargs)
        os.chdir(current_path)
        return result

    return wrapper


def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def install_and_build():
    log_call("pnpm install --no-frozen-lockfile")
    log_call("pnpm run build")
    log_call("git add .")
    try:
        log_call(f'git commit -m "Update dependencies ({get_current_time()})"')
    except CalledProcessError:
        logger.info("No changes to commit.")


def regen_for_typespec_python():
    log_call(
        "cd packages/typespec-python && find test/azure/generated -type f ! -name '*apiview_mapping_python.json*' -delete"
    )
    log_call(
        "cd packages/typespec-python && find test/unbranded/generated -type f ! -name '*apiview_mapping_python.json*' -delete"
    )
    log_call("cd packages/typespec-python && npm run regenerate")
    log_call("git add .")
    try:
        log_call(f'git commit -m "Regenerate for typespec-python ({get_current_time()})"')
    except CalledProcessError:
        logger.info("No changes to commit.")


def regen_for_autorest_python():
    log_call("cd packages/autorest.python && . venv/bin/activate && inv regenerate")
    log_call(". packages/autorest.python/venv/bin/activate && black .")
    log_call("git add .")
    try:
        log_call(f'git commit -m "Regenerate for autorest.python ({get_current_time()})"')
    except CalledProcessError:
        logger.info("No changes to commit.")


def git_push():
    log_call("git push origin HEAD")


class Repo:
    def __init__(self, pull_url: str, repo_token: str, typespec_repo_path: str, artifacts_url: str):
        self.pull_url = pull_url
        self.repo_token = repo_token
        self.typespec_repo_path = typespec_repo_path
        self.artifacts_url = artifacts_url
        self._tsp_repo = None
        self._autorest_repo = None
        self._pull = None
        self._http_client_python_json = None
        self.new_branch_name = None

    @property
    def tsp_repo(self):
        if not self._tsp_repo:
            self._tsp_repo = Github(auth=Auth.Token(self.repo_token)).get_repo("microsoft/typespec")
        return self._tsp_repo

    @property
    def autorest_repo(self):
        if not self._autorest_repo:
            self._autorest_repo = Github(auth=Auth.Token(self.repo_token)).get_repo("Azure/autorest.python")
        return self._autorest_repo

    @property
    def pull(self):
        if not self._pull:
            pull_number = re.findall(r"pull/\d+", self.pull_url)[0].replace("pull/", "")
            logger.info(f"Pull number: {pull_number}")
            self._pull = self.tsp_repo.get_pull(int(pull_number))
        return self._pull

    @property
    def source_branch_name(self):
        return self.pull.head.ref

    def checkout_branch(self):
        self.new_branch_name = f"auto-{self.source_branch_name.replace(':', '-')}"
        try:
            log_call(f"git checkout {self.new_branch_name}")
        except CalledProcessError:
            logger.info(f"Branch {self.new_branch_name} does not exist. Creating a new branch.")
            log_call(f"git checkout -b {self.new_branch_name}")

    @return_origin_path
    def http_client_python_json(self):
        if not self._http_client_python_json:
            os.chdir(self.typespec_repo_path)
            if ":" in self.source_branch_name:
                user_name = self.source_branch_name.split(":")[0]
                branch_name = self.source_branch_name.split(":")[1]
                log_call(f"git remote add {user_name} https://github.com/{user_name}/typespec.git")
                log_call(f"git fetch {user_name} {branch_name}")
                log_call(f"git checkout {branch_name}")
            else:
                log_call(f"git checkout {self.source_branch_name}")
            with open(Path("packages/http-client-python/package.json"), "r") as f:
                self._http_client_python_json = json.load(f)

        return self._http_client_python_json

    def update_dependency_http_client_python(self):
        for package in ["autorest.python", "typespec-python"]:
            package_path = Path(f"packages/{package}")
            package_json = package_path / "package.json"
            with open(package_json, "r") as f:
                package_data = json.load(f)
            package_data["dependencies"]["@typespec/http-client-python"] = self.artifacts_url
            with open(package_json, "w") as f:
                json.dump(package_data, f, indent=2)

    def update_other_dependencies(self):
        target_json = Path("packages/typespec-python/package.json")
        source_json = self.http_client_python_json()
        with open(target_json, "r") as f:
            package_data = json.load(f)
        for dependency in ["devDependencies", "peerDependencies"]:
            source = source_json[dependency]
            target = package_data[dependency]
            for k, v in source.items():
                if k in target:
                    logger.info(f"{dependency}: Update {k} from {target[k]} to {v}")
                    target[k] = v
        with open(target_json, "r") as f:
            json.dump(package_data, f, indent=2)

    def update_dependency(self):
        self.update_dependency_http_client_python()
        self.update_other_dependencies()

    # prepare pr for autorest.python repo
    def prepare_pr(self):
        install_and_build()
        regen_for_typespec_python()
        regen_for_autorest_python()
        git_push()

    # create PR in autorest.python repo
    def create_pr(self):
        has_existing_pr = (
            len(list(self.autorest_repo.get_pulls(state="open", head=self.new_branch_name, base="main"))) > 0
        )
        if has_existing_pr:
            logger.info(f"PR already exists for {self.pull_url}")
        else:
            self.autorest_repo.create_pull(
                base="main",
                head=self.new_branch_name,
                title=f"Auto PR for {self.pull_url}",
                body=f"Auto PR for {self.pull_url}",
                maintainer_can_modify=True,
                draft=True,
            )

    def run(self):
        self.checkout_branch()
        self.update_dependency()
        self.prepare_pr()
        self.create_pr()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--pull-url",
        help="Pull request url",
        type=str,
    )

    parser.add_argument(
        "--repo-token",
        help="Token to access the repository",
        type=str,
    )

    parser.add_argument(
        "--typespec-repo-path",
        help="microsft/typespec repo path",
        type=str,
    )

    parser.add_argument(
        "--artifacts-url",
        help="Artifacts url",
        type=str,
    )

    args = parser.parse_args()
    repo = Repo(args.pull_url, args.repo_token, args.typespec_repo_path, args.artifacts_url)
    repo.run()
