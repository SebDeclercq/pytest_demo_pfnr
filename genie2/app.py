#!/usr/bin/env python3
'''
@desc    Main App
@author  SDQ <sdq@afnor.org>
@version 1.0.0
@date    2020-03-31
@note    1.0.0 (2020-03-31) : 1st working version
'''
from pathlib import Path
from typing import Dict
from db.client import DbClient
from genie2.csv_parser import CsvParser
from genie2.records import Standard


class App:
    '''Main App'''

    CREATE_STANDARD_TABLE: str = '''
    CREATE TABLE IF NOT EXISTS Standard (
        numdos TEXT,
        refdoc TEXT,
        datoff INT,
        ancart TEXT
    )
    '''

    CREATE_FILE_TABLE: str = '''
    CREATE TABLE IF NOT EXISTS FILE (
        numdos TEXT,
        numdosvl TEXT,
        format TEXT,
        verling TEXT
    )
    '''

    INSERT_STANDARD: str = '''
    INSERT INTO Standard VALUES (:numdos, :refdoc, :datoff, :ancart)
    '''

    INSERT_FILE: str = '''
    INSERT INTO File VALUES (:numdos, :numdosvl, :format, :verling)
    '''

    def csv_to_db(
        self, input: Path, output: Path = Path('standards.db')
    ) -> None:
        '''Main method'''
        csv_parser: CsvParser = CsvParser()
        standards: Dict[str, Standard] = csv_parser.get_standards(input)
        with DbClient(str(output)) as db:
            self._create_tables(db)
            for _, std in standards.items():
                self.insert_standard(db, std)

    def _create_tables(self, db: DbClient) -> DbClient:
        '''Create tables if not exist'''
        db.execute(self.CREATE_STANDARD_TABLE)
        db.execute(self.CREATE_FILE_TABLE)
        db.commit()
        return db

    def insert_standard(self, db: DbClient, std: Standard) -> DbClient:
        '''Insert standard data in the Standard table and the files
        data in the File table'''
        db.execute(
            self.INSERT_STANDARD,
            (
                {
                    'numdos': std.numdos,
                    'refdoc': std.refdoc,
                    'ancart': std.ancart,
                    'datoff': std.datoff,
                }
            ),
        )
        for file_ in std.files:
            db.execute(
                self.INSERT_FILE,
                (
                    {
                        'numdos': std.numdos,
                        'numdosvl': file_.numdosvl,
                        'format': file_.format,
                        'verling': file_.verling,
                    }
                ),
            )
        return db
