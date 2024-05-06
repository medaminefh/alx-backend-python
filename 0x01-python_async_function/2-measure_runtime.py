from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: float) -> float:
    """
    Args:
        n (int): number of coroutines
        max_delay (float): max random delay
    Returns:
        float: time
    """
    start = time()
    run(wait_n(n, max_delay))
    end = time()
    return end - start
