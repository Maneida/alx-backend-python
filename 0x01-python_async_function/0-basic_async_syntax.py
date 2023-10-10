#!/usr/bin/env python3
"""
An asynchronous coroutine with random delay
"""
import random
import asyncio


async def wait_random(max_delay=10):
    """
    Waits for a random delay between 0 and max_delay seconds (inclusive).

    Args:
        max_delay (float, optional): M
        aximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
