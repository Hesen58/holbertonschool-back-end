#!/usr/bin/env python3
"""Annotations"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """fixed"""
    return [(i, len(i)) for i in lst]
