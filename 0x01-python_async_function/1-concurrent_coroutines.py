#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async
an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random n
times with the specified max_delay.
wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using
sort() because of concurrency.
Funtions:
    wait_n(n: int, max_delay: int) -> float:
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return the list of all the delays
        Parameters:
            n (int): number
            max_delay (int): other number
        Returns:
            list of all the delays
    """
    the_list = []
    for _ in range(n):
        asdf = await asyncio.gather(wait_random(max_delay))
        the_list.append(asdf[0])
    the_list.sort()
    return the_list
