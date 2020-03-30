#!/usr/bin/env python3
'''
@desc    Unitary testing the db.client.DbClient class
@author  SDQ <sdq@afnor.org>
@version 1.0.0
@date    2020-03-30
@note    1.0.0 (2020-03-30) : OK
'''
from typing import List
import sqlite3
from py._path.local import LocalPath
import pytest
from db.client import DbClient


class TestDbClient:
    def test_enter_default(self) -> None:
        with DbClient() as db:
            assert db.db_path == ':memory:'
            assert db.as_dict is True
            assert db.is_connected is True

    def test_enter_with_params(self, tmp_path: LocalPath) -> None:
        dbfile: LocalPath = tmp_path / 'test.db'
        with DbClient(dbfile, as_dict=False) as db:
            assert db.db_path == dbfile
            assert db.as_dict is False
            assert db.is_connected is True
        files: List[LocalPath] = list(tmp_path.iterdir())
        assert len(files) == 1
        assert dbfile in files

    def test_execute(self) -> None:
        with DbClient() as db:
            result: sqlite3.Cursor = db.execute('SELECT 1+1 AS my_sum')
            assert next(result)['my_sum'] == 2

    def test_execute_no_dict(self) -> None:
        with DbClient(as_dict=False) as db:
            result: sqlite3.Cursor = db.execute('SELECT 1+1 AS my_sum')
            assert next(result)[0] == 2
