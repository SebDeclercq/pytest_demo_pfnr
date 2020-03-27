#!/usr/bin/env python3
'''
@desc    description
@author  SDQ <sdq@afnor.org>
@version 0.0.1
@date    2020-03-27
@note    0.0.1 (2020-03-27) : Init file
'''
from typing import Dict, Union
from _pytest.monkeypatch import MonkeyPatch
from genie2.records import File, Standard
import genie2


class TestStandard:
    def test_init(self, monkeypatch: MonkeyPatch) -> None:
        data: Dict[str, Union[str, int]] = {
            'numdos': 'XS126450',
            'refdoc': 'ISO 14001:2015',
            'datoff': 20150915,
            'ancart': 'ISO14001',
        }
        std: Standard = Standard(**data)
        for attr, val in data.items():
            assert getattr(std, attr) == val
        assert std.files == []


class TestFile:
    def test_init(self) -> None:
        data: Dict[str, str] = {
            'numdosvl': 'XS126450',
            'format': 'PDFC',
            'verling': 'F',
        }
        file_: File = File(**data)
        for attr, val in data.items():
            assert getattr(file_, attr) == val
