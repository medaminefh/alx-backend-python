#!/usr/bin/env python3
"""
Type annotated function that return the concat of two string
"""
from typing import Union, Any, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
