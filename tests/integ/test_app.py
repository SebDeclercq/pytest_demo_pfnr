#!/usr/bin/env python3
'''
@desc    description
@author  SDQ <sdq@afnor.org>
@version 0.0.1
@date    2020-03-30
@note    0.0.1 (2020-03-30) : Init file
'''
from py._path.local import LocalPath
from typing import Dict, Iterator
import sqlite3
from db.client import DbClient
from genie2.app import App
from genie2.csv_parser import CsvParser
from genie2.records import File, Standard


class TestApp:
    def test_full_app(
        self, csv_parser: CsvParser, csv_file: LocalPath, tmp_path: LocalPath
    ) -> None:
        app: App = App()
        dest_db_file: LocalPath = tmp_path / 'file.db'
        app.csv_to_db(input=csv_file, output=dest_db_file)
        standards: Dict[str, Standard] = csv_parser.get_standards(csv_file)
        with DbClient(dest_db_file) as db:
            sql: str = 'SELECT * FROM Standard WHERE numdos = ?'
            for numdos, std in standards.items():
                result: Iterator[sqlite3.Row] = db.execute(sql, (numdos,))
                assert next(result)['numdos'] == numdos
                for file_ in std.files:
                    sql = 'SELECT * FROM File WHERE numdosvl = ?'
                    result = db.execute(sql, (file_.numdosvl,))
                    assert next(result)['numdos'] == numdos
