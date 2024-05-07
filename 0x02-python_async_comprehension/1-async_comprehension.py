#!/usr/bin/env python3
"""
write a coroutine called async_generator
"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine that will take 10 random numbers
    between 0 and 10 and returns the 10 random numbers
    """
    return [i async for i in async_generator()]
