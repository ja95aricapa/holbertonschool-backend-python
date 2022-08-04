#!/usr/bin/env python3
"""Let's duck type an iterable object
Annotate the below function’s parameters and return values
with the appropriate types
Functions:
    def element_length(lst: Iterable[Sequence]) ->List[Tuple[Sequence, int]]:
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list
        Parameters:
            lst (Iterable[Sequence]): numbers
        Returns:
            a list
    """
    return [(i, len(i)) for i in lst]
