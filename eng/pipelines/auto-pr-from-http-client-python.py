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
from typing import Dict, Any
from functools import wraps

from subprocess import check_call, CalledProcessError
from msrest.authentication import BasicAuthentication
from azure.devops.v7_1.build import BuildClient

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


def install_and_build():
    log_call("pnpm install --no-frozen-lockfile")
    log_call("pnpm run build")
    log_call('git add . && git commit -m "Update dependencies"')


def regen_for_typespec_python():
    log_call(
        "cd packages/typespec-python && find test/azure/generated -type f ! -name '*apiview_mapping_python.json*' -delete"
    )
    log_call(
        "cd packages/typespec-python && find test/unbranded/generated -type f ! -name '*apiview_mapping_python.json*' -delete"
    )
    log_call("cd packages/typespec-python && npm run regenerate")
    log_call('git add . && git commit -m "Regenerate for typespec-python"')


def regen_for_autorest_python():
    log_call("cd packages/autorest.python && source venv/bin/activate && inv regenerate")
    log_call("source packages/autorest.python/venv/bin/activate && black .")
    log_call('git add . && git commit -m "Regenerate for autorest.python"')


def git_push():
    log_call("git push origin HEAD")


class Repo:
    def __init__(self, pull_url: str, repo_token: str, pipeline_token: str, typespec_repo_path: str):
        self.pull_url = pull_url
        self.repo_token = repo_token
        self.pipeline_token = pipeline_token
        self.typespec_repo_path = typespec_repo_path
        self._repo = None
        self._pull = None
        self._http_client_python_json = None
        self.new_branch_name = None

    @property
    def repo(self):
        if not self._repo:
            self._repo = Github(auth=Auth.Token(self.repo_token)).get_repo("microsoft/typespec")
        return self._repo

    @property
    def pull(self):
        if not self._pull:
            pull_number = re.findall(r"pull/\d+", self.pull_url)[0].replace("pull/", "")
            logger.info(f"Pull number: {pull_number}")
            self._pull = self.repo.get_pull(int(pull_number))
        return self._pull

    @property
    def source_branch_name(self):
        return self.pull.head.ref

    def checkout_branch(self):
        self.new_branch_name = f"auto-{self.source_branch_name}"
        try:
            log_call(f"git checkout {self.new_branch_name}")
        except CalledProcessError:
            logger.info(f"Branch {self.new_branch_name} does not exist. Creating a new branch.")
            log_call(f"git checkout -b {self.new_branch_name}")

    @return_origin_path
    def http_client_python_json(self):
        if not self._http_client_python_json:
            os.chdir(self.typespec_repo_path)
            log_call(f"git checkout {self.source_branch_name}")
            with open(Path("packages/http-client-python/package.json"), "r") as f:
                self._http_client_python_json = json.load(f)

        return self._http_client_python_json

    def get_artifact_url(self):
        # get build_id
        build_id = None
        commit = self.repo.get_commit(self.pull.head.sha)
        for item in list(commit.get_check_runs()):
            if "Python" in item.name and item.conclusion == "success":
                build_id = int(re.findall(r"buildId=\d+", item.details_url)[0].replace("buildId=", ""))
                break
        if not build_id:
            raise Exception("No successful Python build found.")
        logger.info(f"Build id: {build_id}")

        # get artifact url
        client = BuildClient(
            base_url="https://dev.azure.com/azure-sdk", creds=BasicAuthentication(self.pipeline_token, "")
        )
        artifact = client.get_artifact(
            project="internal",
            build_id=build_id,
            artifact_name="build_artifacts_python",
        )
        resource_url = artifact.resource.download_url

        source_json = self.http_client_python_json()
        http_client_python_version = source_json["version"]

        package_name = f"typespec-http-client-python-{http_client_python_version}.tgz"
        url = resource_url.replace("=zip", f"=file&subPath=%2Fpackages%2F{package_name}")
        logger.info(f"Download url of {package_name}: {url}")
        return url

    def update_dependency_http_client_python(self, url: str):
        for package in ["autorest.python", "typespec-python"]:
            package_path = Path(f"packages/{package}")
            package_json = package_path / "package.json"
            with open(package_json, "r") as f:
                package_data = json.load(f)
            package_data["dependencies"]["@typespec/http-client-python"] = url
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
                    target[k] = v
        with open(target_json, "r") as f:
            package_data = json.load(f)

    def update_dependency(self, url: str):
        self.update_dependency_http_client_python(url)
        self.update_other_dependencies()

    # prepare pr for autorest.python repo
    def prepare_pr(self):
        install_and_build()
        regen_for_typespec_python()
        regen_for_autorest_python()
        git_push()

    # create PR in autorest.python repo
    def create_pr(self):
        self.repo.create_pull(
            base="main",
            head=self.new_branch_name,
            title=f'Auto PR for "{self.pull_url}"',
            body=f'Auto PR for "{self.pull_url}"',
            maintainer_can_modify=True,
            draft=False,
        )

    def run(self):
        self.checkout_branch()
        url = self.get_artifact_url()
        self.update_dependency(url)
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
        "--pipeline-token",
        help="Token to access the pipeline",
        type=str,
    )

    parser.add_argument(
        "--typespec-repo-path",
        help="microsft/typespec repo path",
        type=str,
    )

    args = parser.parse_args()
    repo = Repo(args.pull_url, args.repo_token, args.pipeline_token, args.typespec_repo_path)
    repo.run()
