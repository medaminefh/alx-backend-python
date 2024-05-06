#!/usr/bin/env python3
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> list:
    """
    Args:
        n (int): number of coroutines
        max_delay (int): max random delay
    Returns:
        list: list of delays
    """
    delays = [(task_wait_random(max_delay))
              for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
