#!/usr/bin/env python3
"""Type annotations for safely_get_value function"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Returns first element of input list"""
    if key in dct:
        return dct[key]
    else:
        return default
