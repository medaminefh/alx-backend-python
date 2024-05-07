#!/usr/bin/env python3
"""
write a coroutine called async_generator
"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Args:
        n (int): number of coroutines
        max_delay (float): max random delay
    Returns:
        float: time
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start

