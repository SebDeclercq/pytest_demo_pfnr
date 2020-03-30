#!/usr/bin/env python3
'''
@desc    description
@author  SDQ <sdq@afnor.org>
@version 0.0.1
@date    2020-03-27
@note    0.0.1 (2020-03-27) : Init file
'''
from pathlib import Path
from typing import Any, Dict, Iterator
import csv
from genie2.records import File, Standard


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

    def get_standards(
        self, file_path: Path, delimiter='\t'
    ) -> Dict[str, Standard]:
        '''Main method iterating on the CSV data and parsing it
        into `Standards` instances.'''
        standards: Dict[str, Standard] = {}
        for record in self.parse(file_path, delimiter):
            numdos: str = record['numdos']
            if numdos not in standards:
                self.add_standard(standards=standards, **record)
            self.add_file(standards=standards, **record)
        return standards

    def add_standard(
        self,
        standards: Dict[str, Standard],
        numdos: str,
        refdoc: str,
        datoff: str,
        ancart: str,
        **kwargs: Any
    ) -> Dict[str, Standard]:
        '''Instanciate a new `Standard` and add it to the `Standard`s list'''
        standards[numdos] = Standard(
            numdos=numdos, refdoc=refdoc, datoff=int(datoff), ancart=ancart
        )
        return standards

    def add_file(
        self,
        standards: Dict[str, Standard],
        numdos: str,
        numdosvl: str,
        format: str,
        verling: str,
        **kwargs: Any
    ) -> Dict[str, Standard]:
        '''Instanciate a new `File` and add it to the `File`s list
        of the corresponding `Standard` object.'''
        standards[numdos].add_file(File(numdosvl, format, verling))
        return standards
