"""CSC111 Winter 2021 Project: To-Run-To Map

Module Description
==================
This python module contains the load_weighted_graph() function. This function takes the
directory of the UofTMap.json file and the directory of the full_corner.json file and returns
a MapGraph instance.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Jihyuk Yoon, Yeong Jae Ryu, Eunchae Seong, and Taewoong Oh.
"""
from __future__ import annotations
import json
from map_graph import MapGraph
from distance import distance


def load_weighted_graph(building_file: str, corner_file: str) -> MapGraph:
    """Return a MapGraph corresponding to

    Precondition:
        - building_file is the path to a JSON file containing the data on the coordinates
          of the buildings.
        - corner_file is the path to JSON file containing the data of the coordinates
          of the 'corners' which are intersections of each street.

    >>> g = load_weighted_graph('Data/UofTMap.json', 'Data/full_corner.json')
    >>> len(g.get_all_vertices('building'))
    450
    >>> len(g.get_all_vertices('corner'))
    1076
    """
    # Initialize MapGraph
    g = MapGraph()

    with open(corner_file) as json_file:
        data = json.load(json_file)
        for p in data:
            nodes = p['nodes'][0].split('-')
            coords = p['coordinates']

            # Only add the vertex if is not already in the graph (avoid duplicates)
            if nodes[0] not in g.get_all_vertices('corner'):
                g.add_vertex(nodes[0], tuple(coords[0]), 'corner')

            if nodes[1] not in g.get_all_vertices('corner'):
                g.add_vertex(nodes[1], tuple(coords[1]), 'corner')

            # In case the JSON file has a node that connects to itself
            if nodes[0] != nodes[1]:
                # Get the distance directly from the JSON File
                dist = int(p["distance_metres"][0])
                g.add_edge(nodes[0], nodes[1], dist)

    with open(building_file) as json_file:
        data = json.load(json_file)
        for p in data:
            if p['name'] not in g.get_all_vertices('building'):
                g.add_vertex(p['name'], (p['lat'], p['lng']), 'building')
                # Find the closest three corner vertices to connect to
                closest = g.find_closest_vertex(p['name'])
                for v in closest:
                    # Get the location of the corner vertex to measure the distance
                    location = g.get_location(v)

                    # Calculate the distance using the distance() function
                    dist = distance(p['lng'], location[1], p['lat'], location[0])
                    g.add_edge(p['name'], v, dist)

    return g


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['json', 'map_graph', 'distance'],
        'allowed-io': ['load_weighted_graph'],
        'max-line-length': 100,
        'disable': ['E1136']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()
