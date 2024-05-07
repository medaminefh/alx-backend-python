#!/usr/bin/env python3
"""
write a coroutine called async_generator
"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    coroutine that will loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random()
