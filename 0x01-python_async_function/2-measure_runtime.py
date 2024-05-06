#!/usr/bin/env python3
""" 
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

Use the random module.
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: float) -> float:
    """
    Args:
        n (int): number of coroutines
        max_delay (float): max random delay
    Returns:
        float: time
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return end - start
