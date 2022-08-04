#!/usr/bin/env python3
"""Complex types - mixed list
a type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float.
Functions:
    sum_mixed_list(mxd_lst: List[int]) -> float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returns their sum as a float.
        Parameters:
            mxd_lst (List[int]): numbers integers
        Returns:
            their sum as a float.
    """
    return float(sum(mxd_lst))
