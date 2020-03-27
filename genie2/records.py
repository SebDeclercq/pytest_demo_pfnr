#!/usr/bin/env python3
'''
@desc    description
@author  SDQ <sdq@afnor.org>
@version 0.0.1
@date    2020-03-27
@note    0.0.1 (2020-03-27) : Init file
'''
from dataclasses import dataclass, field
from typing import List


@dataclass
class File:
    pass


@dataclass
class Standard:
    numdos: str
    refdoc: str
    datoff: int
    ancart: str
    files: List[File] = field(default_factory=list)
