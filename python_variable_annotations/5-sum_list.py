#!/usr/bin/env python3
"""Annotations"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums list"""
    total = 0
    for i in input_list:
        total += i
    return total
