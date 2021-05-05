"""CSC111 Winter 2021 Project: To-Run-To Map

Module Description
==================
This module contains the Graph and _Vertex classes that we use to create a map, called
To-Run-To Map that finds the fastest route between two places in the
University of Toronto St. George campus.

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
from typing import Any, Union
from distance import distance


class _LocationVertex:
    """A vertex in a map graph, used to represent a building or corner in the campus.

    Each vertex item is either a name of the building or the corner.
    Both are represented as strings, even though we've kept the type annotation as Any
    to be consistent with lecture.

    Instance Attributes:
        - name: The name of the building or the corner.
        - location: The latitude and longitude of the building/corner.
        - kind: The type of this vertex: 'building' or 'corner'.
        - neighbours: The vertices that are adjacent to this vertex, and their corresponding
            distance.

    Representation Invariants:
        - self not in self.neighbours
        - all(self in u.neighbours for u in self.neighbours)
        - self.kind in {'building', 'corner'}
    """
    name: str
    location: tuple[float, float]
    kind: str
    neighbours: dict[_LocationVertex, Union[int, float]]

    def __init__(self, name: Any, location: tuple[float, float], kind: str) -> None:
        """Initialize a new vertex with the given item and kind.

        This vertex is initialized with no neighbours.

        Preconditions:
            - kind in {'building', 'corner'}
        """
        self.name = name
        self.location = location
        self.kind = kind
        self.neighbours = {}

    def degree(self) -> int:
        """Return the degree of this vertex."""
        return len(self.neighbours)

    def get_distance(self, other: _LocationVertex) -> float:
        """Return the distance between this vertex and other vertex."""
        lat1, long1 = self.location  # latitude and longitude of self vertex
        lat2, long2 = other.location  # latitude and longitude of other vertex
        return distance(long1, long2, lat1, lat2)


class MapGraph:
    """A weighted graph used to represent a map of the University of Toronto St. George campus.
    """
    # Private Instance Attributes:
    #     - _vertices:
    #         A collection of the vertices contained in this graph.
    #         Maps name to _LocationVertex object.
    _vertices: dict[Any, _LocationVertex]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._vertices = {}

    def add_vertex(self, name: Any, location: tuple[float, float], kind: str) -> None:
        """Add a vertex with the given name and kind to this graph.

        The new vertex is not adjacent to any other vertices.
        Do nothing if the given item is already in this graph.

        Preconditions:
            - kind in {'building', 'corner'}
        """
        if name not in self._vertices:
            self._vertices[name] = _LocationVertex(name, location, kind)

    def add_edge(self, name1: Any, name2: Any, dist: Union[int, float]) -> None:
        """Add an edge between the two vertices with the given names in this graph,
        with the given distance.

        Raise a ValueError if name1 or name2 do not appear as vertices in this graph.

        Preconditions:
            - name1 != name2
        """
        if name1 in self._vertices and name2 in self._vertices:
            v1 = self._vertices[name1]
            v2 = self._vertices[name2]

            # Add the new edge
            v1.neighbours[v2] = dist
            v2.neighbours[v1] = dist
        else:
            # We didn't find an existing vertex for both items.
            raise ValueError

    def get_distance(self, name1: Any, name2: Any) -> Union[int, float]:
        """Return the weight of the edge between the given items.

        Return 0 if item1 and item2 are not adjacent.

        Preconditions:
            - item1 and item2 are vertices in this graph
        """
        v1 = self._vertices[name1]
        v2 = self._vertices[name2]
        return v1.neighbours.get(v2, 0)

    def adjacent(self, name1: Any, name2: Any) -> bool:
        """Return whether name1 and name2 are adjacent vertices in this graph.

        Return False if name1 or name2 do not appear as vertices in this graph.
        """
        if name1 in self._vertices and name2 in self._vertices:
            v1 = self._vertices[name1]
            return any(v2.name == name2 for v2 in v1.neighbours)
        else:
            return False

    def get_neighbours(self, name: Any) -> set:
        """Return a set of the neighbours of the given name.

        Note that the *names* are returned, not the _Vertex objects themselves.

        Raise a ValueError if item does not appear as a vertex in this graph.
        """
        if name in self._vertices:
            v = self._vertices[name]
            return {neighbour.name for neighbour in v.neighbours}
        else:
            raise ValueError

    def get_all_vertices(self, kind: str = '') -> set:
        """Return a set of all vertex items in this graph.

        If kind != '', only return the items of the given vertex kind.

        Preconditions:
            - kind in {'', 'corner', 'building'}
        """
        if kind != '':
            return {v.name for v in self._vertices.values() if v.kind == kind}
        else:
            return set(self._vertices.keys())

    def find_closest_vertex(self, name: str) -> list[str]:
        """Return the list of names of (at most) three corner vertex that is closest
        to the vertex with the given building name.

        Preconditions:
            - name in self._vertices
            - self._vertices[name].kind == 'building'
        """
        dist_so_far = []
        corners = self.get_all_vertices('corner')
        b = self._vertices[name]

        for c_name in corners:
            c = self._vertices[c_name]
            dist = b.get_distance(c)
            dist_so_far.append((c_name, dist))

        # Sort the list based on the distance (minimum)
        dist_so_far.sort(key=lambda x: x[1])

        return [dist_so_far[i][0] for i in range(3)]

    def get_location(self, name: str) -> tuple:
        """Return the location attribute of the given vertex

        Preconditions:
            - name in self._vertices
        """
        return self._vertices[name].location


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['python_ta.contracts', 'typing', 'distance'],
        'disable': ['E1136', 'W0221']
    })
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    import doctest

    doctest.testmod()
