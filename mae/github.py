# SPDX-License-Identifier: MIT
"""Minimal GitHub API wrapper for RenkuOS pull requests."""

import os

import requests

API = "https://api.github.com"
DEFAULT_REPO = "RenkuOS/Source"


def _repo() -> str:
    return os.environ.get("RENKU_REPO", DEFAULT_REPO)


def _headers() -> dict[str, str]:
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def fetch_pr(pr_number: int) -> dict:
    url = f"{API}/repos/{_repo()}/pulls/{pr_number}"
    resp = requests.get(url, headers=_headers(), timeout=30)
    resp.raise_for_status()
    return resp.json()


def fetch_comments(pr_number: int) -> list[dict]:
    url = f"{API}/repos/{_repo()}/issues/{pr_number}/comments"
    resp = requests.get(url, headers=_headers(), timeout=30)
    resp.raise_for_status()
    return resp.json()
