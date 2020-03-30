#!/usr/bin/env python3
'''
@desc    description
@author  SDQ <sdq@afnor.org>
@version 0.0.1
@date    2020-03-27
@note    0.0.1 (2020-03-27) : Init file
'''
from typing import Dict
import re
from py._path.local import LocalPath
from genie2.csv_parser import CsvParser
from genie2.records import File, Standard


class TestCsvParser:
    def test_get_standards(
        self, csv_parser: CsvParser, csv_file: LocalPath
    ) -> None:
        std: Standard = csv_parser.get_standards(csv_file)['XS126450']
        assert isinstance(std, Standard)
        assert std.refdoc == 'ISO 14001:2015'
        assert isinstance(std.datoff, int)
        assert len(std.files) == 4
        assert isinstance(std.files[0], File)
        assert re.match(r'^X[ES]\d{6}', std.files[0].numdosvl)
