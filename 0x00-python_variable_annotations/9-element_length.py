#!/usr/bin/env python3
"""
Annotations for element_length function
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a tuple with its length"""
    return [(i, len(i)) for i in lst]
