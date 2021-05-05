"""CSC111 Winter 2021 Project: To-Run-To Map

Module Description
==================
This module contains the building_list() function. This function takes the directory for the
UofTMap.json file and returns a list of the names of the buildings in the JSON file.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Jihyuk Yoon, Yeong Jae Ryu, Eunchae Seong, and Taewoong Oh.
"""
import json


def buildings_list(building_file: str) -> list:
    """Return the list of the names of the buildings of the JSON file
    Precondition:
        - building_file is the path to a JSON file containing the data on the coordinates
          of the buildings.
    """
    buildings_so_far = []
    with open(building_file) as json_file:
        data = json.load(json_file)
        for p in data:
            # Append only if it does not already exist in the list.
            if p['name'] not in buildings_so_far:
                buildings_so_far.append(p['name'])

    return buildings_so_far


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['json'],
        'allowed-io': ['buildings_list'],
        'max-line-length': 100,
        'disable': ['E1136']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()
