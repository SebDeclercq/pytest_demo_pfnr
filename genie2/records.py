#!/usr/bin/env python3
'''
@desc    description
@author  SDQ <sdq@afnor.org>
@version 0.0.1
@date    2020-03-27
@note    0.0.1 (2020-03-27) : Init file
'''
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class File:
    numdosvl: str
    format: str
    verling: str


@dataclass
class Standard:
    numdos: str
    refdoc: str
    datoff: int
    ancart: str
    files: List[File] = field(default_factory=list)

    def add_file(self, file_: File) -> Standard:
        '''Add a file to the Standard'''
        self.files.append(file_)
        return self
