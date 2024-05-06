#!/usr/bin/env python3
""" 
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

Use the random module.
"""
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
