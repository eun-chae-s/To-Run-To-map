"""CSC111 Winter 2021 Project: To-Run-To Map

Module Description
==================
This python module contains the PriorityQueue class that we use to store vertices with the priority
of distance and methods involving Dijkstra's algorithm in order to return the list showing the
shortest path from starting vertex to destination vertex.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Jihyuk Yoon, Yeong Jae Ryu, Eunchae Seong, and Taewoong Oh.
"""
import math
from typing import Any, Dict
from heapq import heapify, heappush, heappop
from map_graph import MapGraph


class NoShortestPathError(Exception):
    """Exception raised when there is no shortest path between the two vertices."""
    def __str__(self) -> str:
        """Return a string representation of this error."""
        return 'There is no possible shortest path between the two vertices'


class EmptyPriorityQueueError(Exception):
    """Exception raised when calling pop on an empty stack."""

    def __str__(self) -> str:
        """Return a string representation of this error."""
        return 'You called dequeue on an empty priority queue.'


class PriorityQueue:
    """A queue of items that can be dequeued in priority order.

    When removing an item from the queue, the highest-priority item is the one
    that is removed.
    """

    # Private Instance Attributes:
    #   - _items: a list of the items in this priority queue
    _items: list[list[Any, str]]

    def __init__(self) -> None:
        """Initialize a new and empty priority queue."""
        self._items = []

    def enqueue(self, item: Any) -> None:
        """Add the given item with the given priority to this priority queue.
        """
        heappush(self._items, item)

    def dequeue(self) -> Any:
        """Remove and return the item with the highest priority.

        Raise an EmptyPriorityQueueError when the priority queue is empty.
        """
        if self.is_empty():
            raise EmptyPriorityQueueError
        else:
            return heappop(self._items)[1]

    def is_empty(self) -> bool:
        """Return whether this priority queue contains no items.
        """
        return self._items == []

    def update_items_order(self, item: str, priority: float) -> None:
        """Update the order of items list by assigning a priority for the item with
        the given key and convert the list into heap.
        """
        for i in self._items:
            if i[1] == item:
                i[0] = priority
        heapify(self._items)


def dijkstra(map_graph: MapGraph, start_vertex: str) -> Dict:
    """Return a dictionary for the minimum path that took to reach each vertex.

        Preconditions:
            - start_vertex in map_graph.get_all_vertices()
    >>> g = MapGraph()
    >>> g.add_vertex('A', (0, 0), 'corner')
    >>> g.add_vertex('B', (0, 0), 'corner')
    >>> g.add_vertex('C', (0, 0), 'corner')
    >>> g.add_vertex('D', (0, 0), 'corner')
    >>> g.add_edge('A', 'B', 10)
    >>> g.add_edge('A', 'C', 7)
    >>> g.add_edge('B', 'D', 2)
    >>> g.add_edge('C', 'D', 3)
    >>> dijkstra(g, 'A') == {'C': 'A', 'D': 'C', 'A': None, 'B': 'A'}
    True
    """
    pq = PriorityQueue()  # priority queue of vertices in the format of [[distance, vertex]]
    d = dict.fromkeys(map_graph.get_all_vertices(), math.inf)  # distance pair with initial d = inf
    path_via = dict.fromkeys(map_graph.get_all_vertices(), None)
    # dictionary for the path for reaching a vertex
    d[start_vertex] = 0
    # we set the distance for starting vertex to equal 0
    for v in map_graph.get_all_vertices():
        pq.enqueue([d[v], v])

    while not pq.is_empty():
        # for first iteration, the starting vertex with d = 0 will be popped for dequeue
        i = pq.dequeue()
        for v in map_graph.get_neighbours(i):
            if d[v] > d[i] + map_graph.get_distance(i, v):
                d[v] = d[i] + map_graph.get_distance(i, v)
                pq.update_items_order(v, d[v])
                path_via[v] = i
    return path_via


def shortest_path(start_vertex: str, end_vertex: str, g: MapGraph) -> list:
    """Return an ordered list of path with the element at zero index as the starting vertex.
    Raise NoShortestPathError when there is no possible shortest path between the two vertices
        Preconditions:
            - start_vertex in g.get_all_vertices() and end_vertex in g.get_all_vertices()
    >>> g = MapGraph()
    >>> g.add_vertex('A', (0, 0), 'corner')
    >>> g.add_vertex('B', (0, 0), 'corner')
    >>> g.add_vertex('C', (0, 0), 'corner')
    >>> g.add_vertex('D', (0, 0), 'corner')
    >>> g.add_vertex('E', (0, 0), 'corner')
    >>> g.add_vertex('F', (0, 0), 'corner')
    >>> g.add_vertex('G', (0, 0), 'corner')
    >>> g.add_vertex('H', (0, 0), 'corner')
    >>> g.add_vertex('I', (0, 0), 'corner')
    >>> g.add_vertex('J', (0, 0), 'corner')
    >>> g.add_vertex('K', (0, 0), 'corner')
    >>> g.add_vertex('L', (0, 0), 'corner')
    >>> g.add_vertex('S', (0, 0), 'corner')
    >>> g.add_edge('S', 'A', 7)
    >>> g.add_edge('S', 'B', 2)
    >>> g.add_edge('S', 'C', 3)
    >>> g.add_edge('C', 'L', 2)
    >>> g.add_edge('L', 'I', 4)
    >>> g.add_edge('L', 'J', 4)
    >>> g.add_edge('I', 'J', 6)
    >>> g.add_edge('I', 'K', 4)
    >>> g.add_edge('J', 'K', 4)
    >>> g.add_edge('K', 'E', 5)
    >>> g.add_edge('E', 'G', 2)
    >>> g.add_edge('G', 'H', 2)
    >>> g.add_edge('H', 'F', 3)
    >>> g.add_edge('H', 'B', 1)
    >>> g.add_edge('F', 'D', 5)
    >>> g.add_edge('B', 'D', 4)
    >>> g.add_edge('B', 'A', 3)
    >>> shortest_path('S', 'E', g) == ['S', 'B', 'H', 'G', 'E']
    True
    """
    path_via = dijkstra(g, start_vertex)
    path = [end_vertex]
    curr = end_vertex

    while path_via[curr]:
        path.insert(0, path_via[curr])
        curr = path_via[curr]
    if start_vertex not in path:
        raise NoShortestPathError
    else:
        return path


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['python_ta.contracts', 'typing', 'math', 'map_graph', 'heapq'],
        'disable': ['R1705', 'C0200']
    })
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    import doctest

    doctest.testmod()
    import pytest
    pytest.main(['dijkstra.py'])
