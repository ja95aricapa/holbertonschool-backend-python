#!/usr/bin/env python3
"""Type Checking
Use mypy to validate the following piece of code and
apply any necessary changes.
def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
array = [12, 72, 91]
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3.0)
"""
from typing import Tuple, List, Union, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Type Checking"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
