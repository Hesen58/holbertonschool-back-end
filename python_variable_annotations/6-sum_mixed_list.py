#!/usr/bin/env python3
"""Annotations"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum function"""
    total = 0
    for i in mxd_lst:
        total += i
    return total
