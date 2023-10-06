#!/usr/bin/env python3
"""
Augmented code with duck-typed annotations for safe_first_element function
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns first element of input list"""
    if lst:
        return lst[0]
    else:
        return None
