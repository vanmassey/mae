# SPDX-License-Identifier: MIT
"""Audit commits for RenkuOS-mandated trailers (Signed-off-by, Assisted-by)."""

import subprocess

AI_MARKERS = (
    "co-authored-by: claude",
    "co-authored-by: copilot",
    "co-authored-by: chatgpt",
    "co-authored-by: gemini",
    "generated-by:",
)


def audit_branch(base: str = "main", branch: str = "HEAD") -> list[str]:
    """Return human-readable trailer issues for commits between base and branch."""
    try:
        log = subprocess.run(
            ["git", "log", "--format=%H%x00%B%x00", f"{base}..{branch}"],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        stderr = exc.stderr.strip() if exc.stderr else "unknown git error"
        return [f"git log failed: {stderr}"]

    issues: list[str] = []
    entries = [e for e in log.stdout.split("\x00") if e.strip()]
    for i in range(0, len(entries), 2):
        sha = entries[i][:8]
        body = entries[i + 1]
        if "Signed-off-by:" not in body:
            issues.append(f"{sha}: missing Signed-off-by")
        if "Assisted-by:" not in body and _looks_ai_assisted(body):
            issues.append(f"{sha}: likely AI-assisted but missing Assisted-by")
    return issues


def _looks_ai_assisted(body: str) -> bool:
    lowered = body.lower()
    return any(marker in lowered for marker in AI_MARKERS)
