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
    log_call("find test/azure/generated -type f ! -name '*apiview_mapping_python.json*' -delete")
    log_call("find test/unbranded/generated -type f ! -name '*apiview_mapping_python.json*' -delete")
    log_call("npm run regenerate")
    log_call('git add . && git commit -m "Regenerate for typespec-python"')

class Repo:
    def __init__(self, pull_url: str, repo_token: str, pipeline_token: str, typespec_repo_path: str):
        self.pull_url = pull_url
        self.repo_token = repo_token
        self.pipeline_token = pipeline_token
        self.typespec_repo_path = typespec_repo_path
        self._repo = None
        self._pull = None
        self._http_client_python_json = None

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
            self._pull = self.repo.get_pull(pull_number)
        return self._pull
    
    @property
    def source_bracnch_name(self):
        return self.pull.head.ref
    
    def checkout_branch(self):
        branch_name = f"auto-{self.source_bracnch_name}"
        try:
            log_call(f"git checkout {branch_name}")
        except CalledProcessError:
            logger.info(f"Branch {branch} does not exist. Creating a new branch.")
            log_call(f"git checkout -b {branch_name}")

    @return_origin_path
    def http_client_python_json(self):
        if not self._http_client_python_json:
            os.chdir(self.typespec_repo_path)
            log_call(f"git checkout {self.source_bracnch_name}")
            with open(Path("packages/http-client-python/package.json"), "r") as f:
                self._http_client_python_json = json.load(f)

        return self._http_client_python_json
    
    def get_artifact_url(self):
        # get build_id
        build_id = None
        commit = self.repo.get_commit(self.pull.head.sha)
        for item in list(commit.get_check_runs()):
            if "Python" in item.name and item.conclusion == "success":
                build_id = re.findall(r'buildId=\d+', item.details_url)[0]
                break
        if not build_id:
            raise Exception("No successful Python build found.")
        logger.info(f"Build id: {build_id}")

        # get artifact url
        client = BuildClient(base_url="https://dev.azure.com/azure-sdk", creds=BasicAuthentication(self.pipeline_token, ""))
        artifact = client.get_artifact(
            project="internal",
            build_id=build_id,
            artifact_name="http-client-python",
        )
        resource_url = artifact.resource.download_url

        source_json = self.http_client_python_json()
        http_client_python_version = source_json["version"]

        package_name = f"typespec-http-client-python-{http_client_python_version}.tgz"
        url = resource_url.replace("=zip", f"=file&subPath=%2F{package_name}")
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
            for k, v in source.items:
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

    def run(self):
        self.checkout_branch()
        url = self.get_artifact_url()
        self.update_dependency(url)
        self.prepare_pr()
        self.create_pr()


def get_package_json(package_path: str, branch_name: str) -> Dict[str, Any]:
    original_path = os.getcwd()
    log_call(f"cd {package_path}")
    log_call(f"git checkout {branch_name}")
    with open(package_path, "r") as f:
        data = json.load(f)

    os.chdir(original_path)
    return data


def get_pull():
    repo = Github(auth=Auth.Token(repo_token)).get_repo("microsoft/typespec")
    pull_number = re.findall(r"pull/\d+", pull_url)[0].replace("pull/", "")
    pull = repo.get_pull(pull_number)

def update_dependency(url: str):
    for package in ["autorest.python", "typespec-python"]:
        package_path = Path(f"packages/{package}")
        package_json = package_path / "package.json"
        with open(package_json, "r") as f:
            package_data = json.load(f)
        package_data["dependencies"]["@typespec/http-client-python"] = url
        with open(package_json, "w") as f:
            json.dump(package_data, f, indent=2)



def get_repo(repo_token: str):
    return Github(auth=Auth.Token(repo_token)).get_repo("microsoft/typespec")

def get_pull():
    repo = get_repo(repo_token)
    pull_number = re.findall(r"pull/\d+", pull_url)[0].replace("pull/", "")
    return repo.get_pull(pull_number)

def get_branch_name(repo_token: str, pull_url: str):
    repo = get_repo(repo_token)
    pull_number = re.findall(r"pull/\d+", pull_url)[0].replace("pull/", "")
    pull = repo.get_pull(pull_number)
    return pull.head.ref

def get_build_id():
    pull = repo.get_pull(pull_number)
    commit = repo.get_commit(pull.head.sha)
    branch_name = pull.head.ref
    logger.info(f"Commit sha: {commit.sha}")
    check_runs = commit.get_check_runs()
    build_id = None
    for item in list(check_runs):
        if "Python" in item.name and item.conclusion == "success":
            build_id = re.findall(r'buildId=\d+', item.details_url)[0]
            break
    if not build_id:
        raise Exception("No successful Python build found.")
    logger.info(f"Build id: {build_id}")

def get_artifact_url():

    get_build_id()
    client = BuildClient(base_url="https://dev.azure.com/azure-sdk", creds=BasicAuthentication(pipeline_token, ""))
    artifact = client.get_artifact(
        project="internal",
        build_id=build_id,
        artifact_name="http-client-python",
    )
    resource_url = artifact.resource.download_url

    # get package.json of http-client-python in microsoft/typespec repo
    source_json = get_package_json(typespec_repo_path, branch_name)
    http_client_python_version = source_json["version"]

    package_name = f"typespec-http-client-python-{http_client_python_version}.tgz"
    url = resource_url.replace("=zip", f"=file&subPath=%2F{package_name}")
    logger.info(f"Download url of {package_name}: {url}")



def main(pull_url: str, repo_token: str, pipeline_token: str, typespec_repo_path: str):
    # get repo instance
    repo = get_repo(repo_token)
    pull_number = re.findall(r"pull/\d+", pull_url)[0].replace("pull/", "")
    pull = repo.get_pull(pull_number)
    commit = repo.get_commit(pull.head.sha)
    branch_name = pull.head.ref
    logger.info(f"Commit sha: {commit.sha}")
    check_runs = commit.get_check_runs()


    # checkout new branch
    checkout_branch(branch_name)

    # get download url of http-client-python
    client = BuildClient(base_url="https://dev.azure.com/azure-sdk", creds=BasicAuthentication(pipeline_token, ""))
    artifact = client.get_artifact(
        project="internal",
        build_id=build_id,
        artifact_name="http-client-python",
    )
    resource_url = artifact.resource.download_url

    # get package.json of http-client-python in microsoft/typespec repo
    source_json = get_package_json(typespec_repo_path, branch_name)
    http_client_python_version = source_json["version"]

    package_name = f"typespec-http-client-python-{http_client_python_version}.tgz"
    url = resource_url.replace("=zip", f"=file&subPath=%2F{package_name}")
    logger.info(f"Download url of {package_name}: {url}")

    # update dependency "http-client-python" for autorest.python and typespec-python
    update_dependency(url)

    # update other dependencies for typespec-python
    update_other_dependencies(source_json)


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
