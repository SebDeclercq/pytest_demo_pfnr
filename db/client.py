#!/usr/bin/env python3
'''
@desc    Utterly simple client for an SQLite3 database.
@author  SDQ <sdq@afnor.org>
@version 1.0.0
@date    2020-03-30
@note    1.0.0 (2020-03-30) : 1st working version
'''
from __future__ import annotations
from dataclasses import dataclass
from typing import Any
import sqlite3
import traceback


@dataclass
class DbClient:
    '''Client for an SQLite3 database'''

    db_path: str = ':memory:'
    as_dict: bool = True

    def __enter__(self) -> DbClient:
        '''Enter behaviour while using this class in a with statement'''
        self._connection = sqlite3.connect(self.db_path)
        if self.as_dict:
            self._connection.row_factory = sqlite3.Row
        return self

    def __exit__(
        self, exc_type: type, exc_value: Exception, traceback: traceback
    ) -> None:
        '''Exit behaviour'''
        self._connection.commit()
        self._connection.close()

    def __getattr__(self, attr: str) -> Any:
        '''Use a Cursor attribute or method if the requested attr / method
        is not part of the DbClient object'''
        if attr not in dir(self):
            return getattr(self._connection.cursor(), attr)

    def commit(self) -> None:
        self._connection.commit()

    @property
    def is_connected(self) -> bool:
        '''Is the DbClient is connected to a database ?'''
        return hasattr(self, '_connection')
