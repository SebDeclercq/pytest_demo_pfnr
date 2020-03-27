#!/usr/bin/env python3
'''
@desc    description
@author  SDQ <sdq@afnor.org>
@version 0.0.1
@date    2020-03-27
@note    0.0.1 (2020-03-27) : Init file
'''
from py._path.local import LocalPath
import pytest
from genie2.csv_parser import CsvParser


EXAMPLE_CSV_CONTENT: str = (
    '''numdos	refdoc	datoff	ancart	numdosvl	format	verling
XS126450	ISO 14001:2015	20150915	ISO14001	XS126450	PDFC	F
XS126450	ISO 14001:2015	20150915	ISO14001	XE126450	PDFC	E
XS022560	ISO 9001:2015	20150915	ISO9001	XS022560	PDFC	F
XS022560	ISO 9001:2015	20150915	ISO9001	XE022560	PDFC	E
XS022560	ISO 9001:2015	20150915	ISO9001	XE022560	XML	E
XS022560	ISO 9001:2015	20150915	ISO9001	XS022560	XML	F
XS126450	ISO 14001:2015	20150915	ISO14001	XS126450	XML	F
XS126450	ISO 14001:2015	20150915	ISO14001	XE126450	XML	E'''
)


@pytest.fixture
def csv_file(tmp_path: LocalPath) -> LocalPath:
    csv_file = tmp_path / 'standards.csv'
    csv_file.write_text(EXAMPLE_CSV_CONTENT)
    return csv_file


@pytest.fixture
def csv_parser() -> CsvParser:
    return CsvParser()
