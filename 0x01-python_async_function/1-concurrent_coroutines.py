#!/usr/bin/env python3
"""
A module for asynchronous tasks using asyncio.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for `n` random amounts of time up to `max_delay` seconds.
    Returns a list of the wait times, sorted in ascending order.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    for i in range(len(wait_times)):
        for j in range(len(wait_times) - 1 - i):
            if wait_times[j] > wait_times[j + 1]:
                wait_times[j], wait_times[j + 1] = wait_times[j + 1], wait_times[j]
    return wait_times
