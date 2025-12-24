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
    log_call("pnpm format")
    log_call("black packages/typespec-python/test/azure/mock_api_tests -l 120")
    log_call("black packages/typespec-python/test/generic_mock_api_tests -l 120")
    log_call("black packages/typespec-python/test/unbranded/mock_api_tests -l 120")
    log_call("git add .")
    try:
        log_call(f'git commit -m "Update dependencies ({get_current_time()})"')
        git_push()
    except CalledProcessError:
        logger.info("No changes to commit.")


def regen_for_typespec_python():
    log_call("cd packages/typespec-python && npm run regenerate")
    log_call("git add .")
    try:
        log_call(f'git commit -m "Regenerate for typespec-python ({get_current_time()})"')
        git_push()
    except CalledProcessError:
        logger.info("No changes to commit.")


def regen_for_autorest_python():
    log_call("cd packages/autorest.python && . venv/bin/activate && inv regenerate")
    log_call(". packages/autorest.python/venv/bin/activate && black .")
    log_call("git add .")
    try:
        log_call(f'git commit -m "Regenerate for autorest.python ({get_current_time()})"')
        git_push()
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
    def is_pull_merged(self):
        return self.pull.merged

    @property
    def pull(self):
        if not self._pull:
            pull_number = re.findall(r"pull/\d+", self.pull_url)[0].replace("pull/", "")
            logger.info(f"Pull number: {pull_number}")
            repo = self.tsp_repo if "microsoft/typespec" in self.pull_url else self.autorest_repo
            self._pull = repo.get_pull(int(pull_number))
        return self._pull

    @property
    def source_branch_name(self):
        return self.pull.head.label

    @property
    def pull_title(self):
        return self.pull.title

    def checkout_branch(self, prefix: str = "auto-"):
        if prefix:
            self.new_branch_name = f"{prefix}{self.source_branch_name.replace(':', '-')}"
        else:
            self.new_branch_name = self.source_branch_name.split(":")[-1]
        try:
            log_call(f"git checkout {self.new_branch_name}")
        except CalledProcessError:
            logger.info(f"Branch {self.new_branch_name} does not exist. Creating a new branch.")
            log_call(f"git checkout -b {self.new_branch_name}")

    @return_origin_path
    def http_client_python_json(self):
        if not self._http_client_python_json:
            os.chdir(self.typespec_repo_path)
            logging.info(f"branch name for PR {self.pull_url}: {self.source_branch_name}")

            if not self.is_pull_merged:
                user_name = self.source_branch_name.split(":")[0]
                branch_name = self.source_branch_name.split(":")[1]
                if user_name != "microsoft":
                    log_call(f"git remote add {user_name} https://github.com/{user_name}/typespec.git")
                    log_call(f"git fetch {user_name} {branch_name}")
                log_call(f"git checkout {branch_name}")
            else:
                logger.info(f"PR {self.pull_url} is already merged.")

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
        for dependency in ["dependencies", "devDependencies", "peerDependencies"]:
            source = source_json[dependency]
            target = package_data[dependency]
            for k, v in source.items():
                if k in target:
                    logger.info(f"{dependency}: Update {k} from {target[k]} to {v}")
                    target[k] = v
        with open(target_json, "w") as f:
            json.dump(package_data, f, indent=2)

    def update_dependency(self):
        self.update_dependency_http_client_python()
        self.update_other_dependencies()
        try:
            log_call("git add .")
            log_call('git commit -m "Update dependencies"')
            git_push()
        except:
            logger.info("No changes about dependencies to commit.")

    # prepare pr for autorest.python repo
    def prepare_pr(self):
        install_and_build()
        regen_for_typespec_python()
        regen_for_autorest_python()
        git_push()

    # create PR in autorest.python repo
    def create_pr(self):
        existing_pr = list(
            self.autorest_repo.get_pulls(state="open", head=f"Azure:{self.new_branch_name}", base="main")
        )
        if len(existing_pr) > 0:
            logger.info(f"PR already exists for {self.pull_url}")
            for item in existing_pr:
                logger.info(f"Existing PR: {item.html_url}")
        else:
            self.autorest_repo.create_pull(
                base="main",
                head=self.new_branch_name,
                title=self.pull_title,
                body=f"Auto PR for {self.pull_url}",
                maintainer_can_modify=True,
                draft=True,
            )

    @staticmethod
    def replace_package_name_in_changelog(content: str) -> str:
        return content.replace(
            '  - "@typespec/http-client-python"',
            '  - "@autorest/python"\n  - "@azure-tools/typespec-python"',
        )

    @staticmethod
    def has_only_http_client_python(changelog_data: str) -> bool:
        # extract all package names from the following changelog_data like
        # ```md
        # ---
        # changeKind: internal
        # packages:
        # - "@typespec/http-client-python"
        # ---

        # bump dev version of azure-http-specs to fix nightly build failure
        # ````
        changelog_data_lines = changelog_data.splitlines()
        package_names = []
        for line in changelog_data_lines:
            if line.strip().startswith('- "@'):
                package_name = line.replace('"', "").strip().strip("- ").strip()
                package_names.append(package_name)
        return package_names == ["@typespec/http-client-python"]

    # return dict is "file_name -> content"
    @return_origin_path
    def select_changelogs_from_http_client_python(self, autorest_repo_existing_changelog_content) -> dict[str, str]:
        os.chdir(self.typespec_repo_path)
        changelog_dir = Path(".chronus/changes")
        if changelog_dir.exists():
            tsp_changelog_files = [file for file in changelog_dir.iterdir() if file.is_file()]
        else:
            tsp_changelog_files = []

        added_changelog_map = {}
        # select changelog files that packages equal to "@typespec/http-client-python"
        for changelog_file in tsp_changelog_files:
            with open(changelog_file, "r") as f:
                file_content = f.read()
            # if file_content only contain changelog of @typespec/http-client-python
            if not self.has_only_http_client_python(file_content):
                logger.info(f"Skipping changelog not only for http-client-python: {changelog_file.name}")
                continue

            # Check if this changelog is already in autorest_repo_existing_changelog_content
            changelog_data = self.replace_package_name_in_changelog(file_content)
            if changelog_data not in autorest_repo_existing_changelog_content:
                logger.info(f"copy changelog file {changelog_file.name}")
                added_changelog_map[changelog_file.name] = changelog_data

        return added_changelog_map

    def add_changelog(self):
        logger.info("Adding changelog...")

        try:
            changelog_dir = Path(".chronus/changes")
            autorest_repo_existing_changelog_content = ""
            if changelog_dir.exists():
                for existing_file in changelog_dir.iterdir():
                    if existing_file.is_file():
                        with open(existing_file, "r") as f:
                            autorest_repo_existing_changelog_content += f.read()
                logger.info(f"Existing changelogs in .chronus/changes:\n{autorest_repo_existing_changelog_content}")

            os.makedirs(".chronus/changes", exist_ok=True)
            changelog_map = self.select_changelogs_from_http_client_python(autorest_repo_existing_changelog_content)
            for file_name, content in changelog_map.items():
                changelog_path = changelog_dir / file_name
                with open(changelog_path, "w") as f:
                    f.write(content)
                logger.info(f"Added changelog file: {changelog_path}")

        except Exception as e:
            logger.warning(f"Failed to process main branch changelogs: {e}")
        else:
            # commit changelogs
            log_call("git add .chronus/")
            log_call(f'git commit -m "Add changelog"')
            git_push()

    def run(self):
        if "https://github.com/microsoft/typespec" in self.pull_url:
            self.checkout_branch()
            self.update_dependency()
            self.add_changelog()
            self.create_pr()
            self.prepare_pr()
        elif "https://github.com/Azure/autorest.python" in self.pull_url:
            # regenerate for autorest.python PR then commit and push
            self.checkout_branch(prefix="")
            self.prepare_pr()


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
