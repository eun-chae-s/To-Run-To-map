"""CSC111 Winter 2021 Project: To-Run-To Map

Instructions (READ THIS FIRST!)
===============================

This Python module contains the function that returns the time for traveling a distance
by the different modes of transportation.
The distance will be given in the unit of meter while the time will be returned in the unit of
seconds. The speed of transportation will be in unit of meter per second.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students and TAs
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) 2021 Jihyuk Yoon, Yeong Jae Ryu, Eunchae Seong, and Taewoong Oh.
"""


def vehicle_mode_time(distance: float, mode: str) -> float:
    """returns a time to travel a distance using a certain transportation
        Preconditions:
            - mode in {'walking', 'car', 'bicycle'}
    >>> vehicle_mode_time(108.0, 'car')
    7.775993779204977
    >>> vehicle_mode_time(108.0, 'bicycle')
    19.439984448012442
    >>> vehicle_mode_time(108.0, 'walking')
    108.0
    """
    if mode == 'car':
        return distance / 13.8889
    elif mode == 'bicycle':
        return distance / 5.55556
    elif mode == 'walking':
        return distance / 1
    else:
        raise ValueError


def min_sec(time: float) -> tuple[int, int]:
    """Return the time in the format of minute-seconds
    >>> min_sec(vehicle_mode_time(108.0, 'car'))
    (0, 7)
    >>> min_sec(vehicle_mode_time(108.0, 'bicycle'))
    (0, 19)
    >>> min_sec(vehicle_mode_time(108.0, 'walking'))
    (1, 48)
    """
    minute = int(time // 60)
    secs = int(60 * (time / 60 - time // 60))
    return (minute, secs)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['python_ta.contracts'],
        'disable': ['E1136', 'W0221']
    })
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    import doctest

    doctest.testmod()
