#!/usr/bin/env python3
"""
Type annotated function that return the concat of two string
"""
from typing import List


def sum_mixed_list(mxd_lst: List[int, float]) -> float:
    """
    return the sum of the list
    """
    return sum(mxd_lst)
