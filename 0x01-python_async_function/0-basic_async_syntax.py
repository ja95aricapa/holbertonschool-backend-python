import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random amount of time between 0 and max_delay
    and return the time spend in seconds

    Parameters:
            max_delay (int): number of seconds to wait
    Return:
        seconds
    """
    i = max_delay * random.random()
    await asyncio.sleep(i)
    return i
