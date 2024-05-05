#!/usr/bin/env python3
"""Annotations"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies"""
    def fun(a: float) -> float:
        return multiplier * a
    return fun
