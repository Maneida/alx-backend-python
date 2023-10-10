#!/usr/bin/env python3
"""
Module for async generator coroutine
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields random floats between 0 and 10.

    This coroutine loops 10 times, asynchronously waiting for 1 second
    each time before yielding a random float.

    Yields:
        float: A random float between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
