# Contributing to mae

Thanks for wanting to help. `mae` is a small tool with a narrow job: make
contributing to RenkuOS less painful. Contributions that keep it small and
sharp are more welcome than contributions that make it broad.

This document covers the rules that are specific to this repo. For the
project-wide contribution rules that apply to RenkuOS itself, see
[RenkuOS's `AGENTS.md`](https://github.com/RenkuOS/Source/blob/main/AGENTS.md).

## Development setup

    git clone https://github.com/vanmassey/mae
    cd mae
    python -m venv .venv
    source .venv/bin/activate      # Windows: .venv\Scripts\activate
    pip install -e ".[dev]"

Before opening a PR, run the same checks CI runs:

    ruff format .
    ruff check .
    pytest -q

## Commit rules

Every commit in this repo must:

1. **Carry a `Signed-off-by:` trailer.** Use `git commit -s`. This is the
   Developer Certificate of Origin — by signing off you certify you have the
   right to submit the code under this repo's license. Do not sign off on
   someone else's work.

2. **Carry an `Assisted-by:` trailer if AI helped write it.** This mirrors the
   rule RenkuOS enforces on its own tree: if an AI model produced more than
   roughly 20 lines of the commit, or made a design decision, name the model.
   Format:

       Assisted-by: <model name>

   Example:

       Assisted-by: DeepSeek

   If no AI was involved, omit the trailer. Do not add a placeholder.

3. **Use a clear subject line.** Imperative mood, no trailing period, 50
   characters or fewer. The body explains *why*, not *what*.

A conforming commit looks like this:

    Add trailer audit to mae prep

    Walk the commits between main and HEAD and warn on missing
    Signed-off-by, and on likely AI-assisted commits missing
    Assisted-by. The heuristic is deliberately conservative.

    Signed-off-by: Your Name <you@example.com>
    Assisted-by: DeepSeek

You can check your branch before pushing with:

    mae prep

It is not a substitute for reading the rules above — it is a backstop.

## SPDX headers

Every new source file needs a license identifier on its first line:

    # SPDX-License-Identifier: MIT

Files without one will be flagged in review.

## Pull requests

- One logical change per PR. If you find yourself writing "and also…" in the
  description, split it.
- Update `README.md` if you add or change a user-facing command.
- Add a test for any new command or non-trivial logic. The `cli` CI job exists
  to catch wiring bugs; it will not catch logic bugs for you.
- Reference the issue you are fixing, if there is one.
- Do not bump the version in `pyproject.toml` — that happens at release time.

## Scope

`mae` covers the *pre-merge* half of the contribution lifecycle: track,
review, prepare, and audit a change before it lands. Anything that only makes
sense *after* a merge — upstream sync with Haiku, changelog generation,
backports — belongs in a future `ato` companion tool, not here. If you think a
post-merge feature belongs in `mae`, open an issue and argue for it rather
than opening a PR.

## Licensing

By contributing, you agree your contribution is licensed under the MIT license
in [`LICENSE`](LICENSE). See the `Signed-off-by:` rule above for the DCO
mechanism.

## Reporting bugs

Open an issue with:

- The command you ran
- The output you got
- The output you expected
- Your Python version and OS
- `mae --help` output, if the issue is about a command not appearing

Please do not include your `GITHUB_TOKEN` in bug reports.
