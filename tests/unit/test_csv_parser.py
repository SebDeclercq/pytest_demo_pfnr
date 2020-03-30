#!/usr/bin/env python3
'''
@desc    Testing the genie2.csv_parser.CsvParser class
@author  SDQ <sdq@afnor.org>
@version 1.0.0
@date    2020-03-30
@note    0.0.1 (2020-03-27) : Init file
@note    1.0.0 (2020-03-30) : OK
'''
from typing import Dict
from py._path.local import LocalPath
from genie2.csv_parser import CsvParser


class TestCsvParser:
    def test_parse_csv(
        self, csv_parser: CsvParser, csv_file: LocalPath
    ) -> None:
        record: Dict[str, str] = next(csv_parser.parse(csv_file))
        assert isinstance(record, dict)
        assert record['refdoc'] == 'ISO 14001:2015'
