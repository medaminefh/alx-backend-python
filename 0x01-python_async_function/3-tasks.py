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