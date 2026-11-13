# mae

[![ci](https://github.com/vanmassey/mae/actions/workflows/ci.yml/badge.svg)](https://github.com/vanmassey/mae/actions/workflows/ci.yml)

**mae** (前, "before") is a `b4`-inspired contribution workflow tool for
[RenkuOS](https://github.com/RenkuOS/Source).

In renku, the *maeku* is the verse that sets up the next contributor's
response — the thing that comes before. This tool does the same for code:
it manages the lifecycle of a contribution *before* it merges.

## Install

    pip install git+https://github.com/vanmassey/mae

Or for development:

    git clone https://github.com/vanmassey/mae
    cd mae
    python -m venv .venv && source .venv/bin/activate
    pip install -e ".[dev]"

## Configuration

- `GITHUB_TOKEN` — personal access token with `repo` scope.
- `RENKU_REPO` — target repository (default: `RenkuOS/Source`).

## Commands

| Command | Description |
|---|---|
| `mae track <pr>` | Track a pull request in the local SQLite DB. |
| `mae list` | Show tracked pull requests. |
| `mae review <pr>` | Print a review summary for a pull request. |
| `mae prep` | Audit the current branch for `Signed-off-by:` / `Assisted-by:`. |

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the commit rules — in particular
the `Signed-off-by:` and `Assisted-by:` trailer requirements.

## License

MIT. See [`LICENSE`](LICENSE).
