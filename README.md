# mae

**mae** (前, "before") is a `b4`-inspired contribution workflow tool for
[RenkuOS](https://github.com/RenkuOS/Source).

In renku, the *maeku* is the verse that sets up the next contributor's
response — the thing that comes before. This tool does the same for code:
it manages the lifecycle of a contribution *before* it merges.

## Install

    pip install git+https://github.com/RenkuOS/mae

## Commands

| Command | Description |
|---|---|
| `mae track <pr>` | Track a pull request in the local SQLite DB. |
| `mae list` | Show tracked pull requests. |
| `mae review <pr>` | Print a review summary for a pull request. |
| `mae prep` | Audit the current branch for `Signed-off-by:` / `Assisted-by:`. |

## Configuration

- `GITHUB_TOKEN` — personal access token with `repo` scope.
- `RENKU_REPO` — target repository (default: `RenkuOS/Source`).
