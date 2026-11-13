# SPDX-License-Identifier: MIT
"""SQLite tracking database, inspired by b4 review's persistence layer."""

import sqlite3
from pathlib import Path

DB_PATH = Path.home() / ".local" / "share" / "mae" / "tracking.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS series (
    pr_number INTEGER PRIMARY KEY,
    title     TEXT NOT NULL,
    url       TEXT NOT NULL,
    state     TEXT NOT NULL DEFAULT 'open',
    updated   TEXT
);
CREATE TABLE IF NOT EXISTS comments (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    pr_number  INTEGER NOT NULL,
    body       TEXT NOT NULL,
    author     TEXT,
    created    TEXT,
    FOREIGN KEY (pr_number) REFERENCES series(pr_number)
);
"""


def get_conn(path: Path | None = None) -> sqlite3.Connection:
    path = path or DB_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.executescript(SCHEMA)
    return conn


def track_pr(pr_number: int, title: str, url: str, state: str, updated: str) -> None:
    with get_conn() as conn:
        conn.execute(
            """
            INSERT INTO series (pr_number, title, url, state, updated)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(pr_number) DO UPDATE SET
                title=excluded.title,
                url=excluded.url,
                state=excluded.state,
                updated=excluded.updated
            """,
            (pr_number, title, url, state, updated),
        )


def list_prs() -> list[tuple]:
    with get_conn() as conn:
        return conn.execute(
            "SELECT pr_number, title, state, updated FROM series ORDER BY updated DESC"
        ).fetchall()
