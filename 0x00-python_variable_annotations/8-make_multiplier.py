#!/usr/bin/env python3
"""
Type annotated function that return the concat of two string
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return the sum of the list
    """
    return lambda k: k * multiplier
