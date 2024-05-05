#!/usr/bin/env python3
"""Annotations"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns string and a number"""
    return (k, v ** 2)
