# SPDX-License-Identifier: MIT
"""CLI entry point for mae."""

import argparse
import sys

from . import db, github, trailers


def cmd_track(args: argparse.Namespace) -> int:
    pr = github.fetch_pr(args.pr_number)
    db.track_pr(
        pr_number=pr["number"],
        title=pr["title"],
        url=pr["html_url"],
        state=pr["state"],
        updated=pr["updated_at"],
    )
    print(f"tracked PR #{pr['number']}: {pr['title']}")
    return 0


def cmd_list(_args: argparse.Namespace) -> int:
    rows = db.list_prs()
    if not rows:
        print("no tracked pull requests")
        return 0
    for number, title, state, updated in rows:
        print(f"#{number:<5} [{state}] {title}  (updated {updated})")
    return 0


def cmd_review(args: argparse.Namespace) -> int:
    pr = github.fetch_pr(args.pr_number)
    comments = github.fetch_comments(args.pr_number)
    print(f"PR #{pr['number']}: {pr['title']}")
    print(f"  state:    {pr['state']}")
    print(f"  url:      {pr['html_url']}")
    print(f"  comments: {len(comments)}")
    if comments:
        latest = comments[-1]
        print("  latest comment:")
        print(f"    {latest['user']['login']}: {latest['body'][:200]}")
    return 0


def cmd_prep(_args: argparse.Namespace) -> int:
    issues = trailers.audit_branch()
    if not issues:
        print("no trailer issues found")
        return 0
    for issue in issues:
        print(f"warning: {issue}")
    return 1


def cmd_sync(_args: argparse.Namespace) -> int:
    print("mae sync: placeholder for Haiku-upstream synchronisation")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="mae",
        description="mae — a b4-inspired contribution workflow tool for RenkuOS",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_track = sub.add_parser("track", help="track a pull request")
    p_track.add_argument("pr_number", type=int)
    p_track.set_defaults(func=cmd_track)

    p_list = sub.add_parser("list", help="list tracked pull requests")
    p_list.set_defaults(func=cmd_list)

    p_review = sub.add_parser("review", help="review a pull request")
    p_review.add_argument("pr_number", type=int)
    p_review.set_defaults(func=cmd_review)

    p_prep = sub.add_parser("prep", help="audit current branch for trailers")
    p_prep.set_defaults(func=cmd_prep)

    p_sync = sub.add_parser("sync", help="sync with Haiku upstream (placeholder)")
    p_sync.set_defaults(func=cmd_sync)

    args = parser.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
