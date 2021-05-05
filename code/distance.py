"""CSC111 Winter 2021 Project: To-Run-To Map

Module Description
===============================

This Python module contains the function to get the distance between the two points.
The function will obtain distance between the two points using longitudes and latitudes
of the two points. The value gained from this function will be be used to constructing graphs
and visualization

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students and TAs
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) 2021 Jihyuk Yoon, Yeong Jae Ryu, Eunchae Seong, and Taewoong Oh.
"""
import math


def distance(long1: float, long2: float, lat1: float, lat2: float) -> float:
    """Return a distance between two points of location in float
    >>> distance(43.66170149580518, 43.6620507644913, -79.3951503932476, -79.39372479915619)
    158.85423099904
    """
    r = 6.378e+6  # This constant is a radius of Earth
    phi1 = lat1 * math.pi / 180
    phi2 = lat2 * math.pi / 180
    diff_lam = (long2 - long1) * math.pi / 180
    return math.acos(math.sin(phi1) * math.sin(phi2)
                     + math.cos(phi1) * math.cos(phi2) * math.cos(diff_lam)) * r


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['math'],
        'disable': ['R1705', 'C0200']
    })
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    import doctest

    doctest.testmod()
    import pytest
    pytest.main(['distance.py'])
