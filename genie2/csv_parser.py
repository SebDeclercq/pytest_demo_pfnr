#!/usr/bin/env python3
'''
@desc    description
@author  SDQ <sdq@afnor.org>
@version 0.0.1
@date    2020-03-27
@note    0.0.1 (2020-03-27) : Init file
'''
from pathlib import Path
from typing import Dict, Iterator
import csv


class CsvParser:
    def parse(
        self, file_path: Path, delimiter='\t'
    ) -> Iterator[Dict[str, str]]:
        '''Parse a CSV file and yield a dictionary with the values
        
        Params:
            file_path: the path to file to parse
            delimiter: the delimiter (duh) to split on, default is \t
        '''
        with file_path.open() as fh:
            csv_reader: csv.DictReader = csv.DictReader(
                fh, delimiter=delimiter
            )
            for line in csv_reader:
                yield line
