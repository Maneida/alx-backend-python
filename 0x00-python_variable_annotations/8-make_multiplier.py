#!/usr/bin/env python3
"""
type annotations for make_multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def multiply(n: float) -> float:
        """Returns a float of multiple of n and multiplier"""
        return n * multiplier
    return multiply
