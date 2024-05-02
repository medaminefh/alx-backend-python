#!/usr/bin/env python3
"""
Type annotated function that return the concat of two string
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    return the sum of the list
    """
    return (k, float(v**2))
