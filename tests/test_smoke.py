# SPDX-License-Identifier: MIT
from pathlib import Path

from mae import db


def test_db_roundtrip(tmp_path: Path) -> None:
    conn = db.get_conn(tmp_path / "t.db")
    conn.execute(
        "INSERT INTO series (pr_number, title, url, state, updated) "
        "VALUES (1, 'title', 'url', 'open', '2025-01-01')"
    )
    conn.commit()
    row = conn.execute("SELECT title FROM series WHERE pr_number = 1").fetchone()
    assert row is not None
    assert row[0] == "title"
    conn.close()
