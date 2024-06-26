#!/usr/bin/env python3
"""
Type annotated function that return the concat of two string
"""
from typing import Union, Any, Mapping, TypeVar


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
