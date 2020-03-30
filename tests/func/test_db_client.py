#!/usr/bin/env python3
'''
@desc    Testing that DbClient is fully functional w/ CREATE, INSERT, SELECT
@author  SDQ <sdq@afnor.org>
@version 1.0.0
@date    2020-03-30
@note    1.0.0 (2020-03-30) : OK
'''
from typing import Sequence, Tuple
from db.client import DbClient


class TestDbClient:
    def test_create_insert_and_select(self) -> None:
        values: Sequence[Tuple[int, int]] = ((1, 2,), (3, 4,), (5, 6,))
        with DbClient() as db:
            db.execute('CREATE TABLE t (a INT, b INT);')
            db.executemany('INSERT INTO t VALUES (?, ?);', values)
            for row in db.execute('SELECT rowid, * FROM t;'):
                idx: int = row['rowid'] - 1
                assert row['a'] == values[idx][0]
                assert row['b'] == values[idx][1]
