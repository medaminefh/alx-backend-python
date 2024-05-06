#!/usr/bin/env python3
""" 
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

Use the random module.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Args:
        max_delay (int): max random delay
    Returns:
        asyncio.Task: task
    """
    return asyncio.create_task(wait_random(max_delay))
