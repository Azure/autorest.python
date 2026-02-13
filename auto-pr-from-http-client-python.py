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
from datetime import datetime, timedelta
import time
import random

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
    log_call(
        "cd packages/typespec-python && . venv/bin/activate && black test/azure/mock_api_tests test/generic_mock_api_tests test/unbranded/mock_api_tests -l 120"
    )

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
    def __init__(
        self,
        pull_url: str,
        repo_token: str,
        typespec_repo_path: str,
        artifacts_url: str,
        ado_token: str,
        pipeline_link: str = None,
    ):
        self.pull_url = pull_url
        self.repo_token = repo_token
        self.typespec_repo_path = typespec_repo_path
        self.artifacts_url = artifacts_url
        self.ado_token = ado_token
        self.pipeline_link = pipeline_link
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

            if self.pull_url:
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
            else:
                logger.info("No pull URL, reading package.json from current typespec repo state (main).")

            with open(Path("packages/http-client-python/package.json"), "r") as f:
                self._http_client_python_json = json.load(f)

        return self._http_client_python_json

    def get_ado_pipeline_build_id(self, commit_sha: str = None) -> str:
        """
        Get Azure DevOps pipeline build ID from GitHub commit check runs.
        Returns the build ID from the 'Python - Build' check run.
        If commit_sha is not provided, uses the PR head SHA.
        """
        try:
            # Get the head commit
            sha = commit_sha or self.pull.head.sha
            head_commit = self.tsp_repo.get_commit(sha)
            logger.info(f"Looking up check runs for SHA: {sha}")

            # Wait for Python - Build check runs to appear
            timeout = timedelta(minutes=10)
            start_time = datetime.now()
            python_build_runs = []

            logger.info("Looking for 'Python - Build' check runs...")
            while not python_build_runs and (datetime.now() - start_time) < timeout:
                check_runs = head_commit.get_check_runs()
                check_runs_list = list(check_runs)
                python_build_runs = [run for run in check_runs_list if "Python - Build" in run.name]

                if not python_build_runs:
                    logger.info("No 'Python - Build' check runs found yet, waiting 30 seconds...")
                    time.sleep(30)

            if not python_build_runs:
                logger.error("Timeout: No 'Python - Build' check runs found after 10 minutes")
                raise Exception("No 'Python - Build' check runs found")

            logger.info(f"Found {len(python_build_runs)} 'Python - Build' check runs")

            # Wait for all Python - Build checks to complete
            logger.info("Waiting for all Python - Build checks to complete...")
            start_time = datetime.now()

            while (datetime.now() - start_time) < timeout:
                # Refresh check runs status
                check_runs = head_commit.get_check_runs()
                check_runs_list = list(check_runs)
                python_build_runs = [run for run in check_runs_list if "Python - Build" in run.name]

                all_completed = all(run.status == "completed" for run in python_build_runs)

                if all_completed:
                    if any(run.conclusion != "success" for run in python_build_runs):
                        raise Exception(f"Check run {run.name} failed with conclusion: {run.conclusion}")
                    logger.info("All Python - Build checks completed!")
                    break

                in_progress = sum(1 for run in python_build_runs if run.status != "completed")
                logger.info(f"{in_progress} check(s) still in progress...")
                time.sleep(30)
            else:
                logger.warning("Timeout: Not all checks completed after 10 minutes")

            # Extract build ID from details_url
            for run in python_build_runs:
                logger.info(f"Check run: {run.name} - Status: {run.status} - Conclusion: {run.conclusion}")
                details_url = run.details_url
                if details_url:
                    # Extract buildId using regex pattern like buildId=5692673
                    match = re.search(r"buildId=(\d+)", details_url)
                    if match:
                        build_id = match.group(1)
                        logger.info(f"Found Build ID: {build_id}")
                        logger.info(f"Details URL: {details_url}")
                        return build_id
                    else:
                        logger.warning(f"No build ID found in URL: {details_url}")
                else:
                    logger.warning(f"No details URL available for check run: {run.name}")

            logger.error("Could not extract build ID from any Python - Build check run")
            return None

        except Exception as e:
            logger.error(f"Error getting ADO pipeline build ID: {e}")
            return None

    @return_origin_path
    def get_http_client_python_version(self, commit_sha: str = None) -> str:
        os.chdir(self.typespec_repo_path)
        # get content of packages/http-client-python/package.json with tsp_repo from target commit id
        commit_id = commit_sha or self.pull.head.sha
        file_content = self.tsp_repo.get_contents("packages/http-client-python/package.json", ref=commit_id)
        package_data = json.loads(file_content.decoded_content.decode("utf-8"))
        return package_data["version"]

    def get_artifacts_url_from_ado_pipeline(self, build_id: str, commit_sha: str = None) -> str:
        """
        Get the artifacts URL from Azure DevOps pipeline build.
        Returns the URL to download the typespec-http-client-python package.
        """

        from azure.devops.connection import Connection
        from msrest.authentication import BasicAuthentication

        # Configuration
        ARTIFACT_NAME = "build_artifacts_python"

        # Connection Setup
        credentials = BasicAuthentication("", self.ado_token)
        connection = Connection(base_url="https://dev.azure.com/azure-sdk", creds=credentials)
        build_client = connection.clients.get_build_client()

        # Get the artifact details using the SDK client
        logger.info(f"Fetching artifact '{ARTIFACT_NAME}' from build {build_id}")
        artifact = build_client.get_artifact(project="public", build_id=int(build_id), artifact_name=ARTIFACT_NAME)

        # Extract the download URL from the artifact resource
        if artifact and artifact.resource and artifact.resource.download_url:
            download_url = artifact.resource.download_url
            logger.info(f"Artifact download URL: {download_url}")

            # Get the version of http-client-python package
            version = self.get_http_client_python_version(commit_sha=commit_sha)
            logger.info(f"http-client-python version: {version}")

            # Replace part of URL to get specific download URL of the component
            if download_url.endswith("content?format=zip"):
                target_url = download_url.replace(
                    "content?format=zip",
                    f"content?format=file&subPath=%2Fpackages%2Ftypespec-http-client-python-{version}.tgz",
                )
                logger.info(f"Target artifact URL: {target_url}")
                return target_url
            else:
                error_msg = f"Unexpected artifact download URL format: {download_url}"
                logger.error(error_msg)
                raise ValueError(error_msg)
        else:
            error_msg = f"Artifact '{ARTIFACT_NAME}' not found or no download URL available."
            logger.error(error_msg)
            raise Exception(error_msg)

    def get_artifacts_url_from_pull_request(self):
        build_id = self.get_ado_pipeline_build_id()
        self.artifacts_url = self.get_artifacts_url_from_ado_pipeline(build_id)

    def update_dependency_http_client_python(self):
        if not self.artifacts_url:
            logger.info("No artifacts URL provided, try to get from PR.")
            self.get_artifacts_url_from_pull_request()

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

    def sync_from_typespec(self):
        script_path = Path(__file__).resolve().parent / "eng" / "scripts" / "sync_from_typespec.py"
        log_call(f"python {script_path} {self.typespec_repo_path}")
        log_call("git add .")
        try:
            log_call(f'git commit -m "Sync shared files from typespec repo ({get_current_time()})"')
            git_push()
        except CalledProcessError:
            logger.info("No changes to commit.")

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
            # Include pipeline link in PR body for traceability
            pr_body = f"Auto PR for {self.pull_url}"
            if self.pipeline_link:
                pr_body += f"\n\nThis PR is generated from the [pipeline]({self.pipeline_link}) triggered manually."
            self.autorest_repo.create_pull(
                base="main",
                head=self.new_branch_name,
                title=self.pull_title,
                body=pr_body,
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

            # commit changelogs
            log_call("git add .chronus/")
            log_call(f'git commit -m "Add changelog"')
            git_push()

        except Exception as e:
            logger.warning(f"error occurs when adding changelog: {e}")

    def run(self):
        if not self.pull_url:
            self.run_from_main()
        elif "https://github.com/microsoft/typespec" in self.pull_url:
            self.checkout_branch()
            self.update_dependency()
            self.sync_from_typespec()
            self.add_changelog()
            self.create_pr()
            self.prepare_pr()
        elif "https://github.com/Azure/autorest.python" in self.pull_url:
            # regenerate for autorest.python PR then commit and push
            self.checkout_branch(prefix="")
            self.prepare_pr()

    def get_latest_http_client_python_commit_sha(self) -> str:
        """Get the latest commit SHA that touches packages/http-client-python on main."""
        commits = self.tsp_repo.get_commits(sha="main", path="packages/http-client-python")
        latest = commits[0]
        logger.info(f"Latest commit for packages/http-client-python: {latest.sha}")
        return latest.sha

    def get_artifacts_url_from_main(self):
        """Get the artifacts URL from the latest main branch commit."""
        commit_sha = self.get_latest_http_client_python_commit_sha()
        self._main_commit_sha = commit_sha
        build_id = self.get_ado_pipeline_build_id(commit_sha=commit_sha)
        self.artifacts_url = self.get_artifacts_url_from_ado_pipeline(build_id, commit_sha=commit_sha)

    def run_from_main(self):
        """Sync from the main branch of typespec repo when no PR is given."""
        logger.info("No pull URL provided. Syncing from main branch of typespec repo.")

        # Generate branch name: auto-microsoft-main-YYYY-MM-DD-NNNNNN
        date_str = datetime.now().strftime("%Y-%m-%d")
        random_suffix = f"{random.randint(0, 999999):06d}"
        self.new_branch_name = f"auto-microsoft-main-{date_str}-{random_suffix}"
        logger.info(f"Creating branch: {self.new_branch_name}")
        log_call(f"git checkout -b {self.new_branch_name}")

        # Get artifacts URL from latest main commit
        if not self.artifacts_url:
            self.get_artifacts_url_from_main()

        # Update dependency in both packages
        for package in ["autorest.python", "typespec-python"]:
            package_json = Path(f"packages/{package}/package.json")
            with open(package_json, "r") as f:
                package_data = json.load(f)
            package_data["dependencies"]["@typespec/http-client-python"] = self.artifacts_url
            with open(package_json, "w") as f:
                json.dump(package_data, f, indent=2)

        # Sync other dependencies from typespec repo's package.json
        self.update_other_dependencies()

        try:
            log_call("git add .")
            log_call('git commit -m "Update dependencies"')
            git_push()
        except CalledProcessError:
            logger.info("No changes about dependencies to commit.")

        # Sync shared files from typespec repo
        self.sync_from_typespec()

        # Build, regenerate, and push
        self.prepare_pr()

        # Create PR
        commit_sha_short = self._main_commit_sha[:7]
        pr_title = f"Sync from typespec main ({date_str}) ({commit_sha_short})"
        pr_body = f"Auto PR syncing from typespec main branch\n\nSource commit: https://github.com/microsoft/typespec/commit/{self._main_commit_sha}"
        if self.pipeline_link:
            pr_body += f"\n\nThis PR is generated from the [pipeline]({self.pipeline_link}) triggered manually."
        self.autorest_repo.create_pull(
            base="main",
            head=self.new_branch_name,
            title=pr_title,
            body=pr_body,
            maintainer_can_modify=True,
            draft=True,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--pull-url",
        help="Pull request url (if not provided, syncs from main branch)",
        type=str,
        required=False,
        default=None,
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
        "--ado-token",
        help="Azure DevOps token",
        type=str,
    )

    parser.add_argument(
        "--artifacts-url",
        help="Artifacts url",
        type=str,
        required=False,
        default=None,
    )

    parser.add_argument(
        "--pipeline-link",
        help="Azure DevOps pipeline link",
        type=str,
        required=False,
        default=None,
    )

    args = parser.parse_args()
    repo = Repo(
        args.pull_url, args.repo_token, args.typespec_repo_path, args.artifacts_url, args.ado_token, args.pipeline_link
    )
    repo.run()
