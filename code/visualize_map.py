"""CSC111 Winter 2021 Project: To-Run-To Map

Module Description
==================
This module contains the function to visualize the map showing the shortest path
between two points selected by the user.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Jihyuk Yoon, Yeong Jae Ryu, Eunchae Seong, and Taewoong Oh.
"""
import os
import webbrowser
import folium
from dijkstra import shortest_path
from vehicle_return_time import vehicle_mode_time, min_sec
from map_graph import MapGraph


def visualize_map_graph(starting_point: str, end_point: str, graph: MapGraph) -> None:
    """return the map visualization of the graph
    """
    coordinates = []
    total_distance = 0.0
    path = shortest_path(starting_point, end_point, graph)
    coordinates.append(list(graph.get_location(path[0])))

    # Get the list of coordinates from the shortest path between two places
    for i in range(1, len(path)):
        curr_loc = graph.get_location(path[i])
        coordinates.append(list(curr_loc))
        total_distance += graph.get_distance(path[i], path[i - 1])

    times = {'car': min_sec(vehicle_mode_time(total_distance, 'car')),
             'bicycle': min_sec(vehicle_mode_time(total_distance, 'bicycle')),
             'walking': min_sec(vehicle_mode_time(total_distance, 'walking'))}

    # Create a Map with two markers
    m = folium.Map(location=coordinates[0], zoom_start=17)  # Adjusted according to the UofT Map
    folium.Marker(
        location=coordinates[0],
        popup=folium.Popup("<b>Departure:</b> {start}<br>".format(start=starting_point),
                           max_width=160),
        icon=folium.Icon(color='blue')
    ).add_to(m)

    message = ("<b>Destination:</b> {end}<br>"
               "<b>Transportation:</b> <br>"
               "<i>Car:</i> {car_m} m {car_s} s<br>"
               "<i>Bicycle</i>: {bi_m} m {bi_s} s<br>"
               "<i>Walking</i>: {w_m} m {w_s} s<br>").format(end=end_point,
                                                             car_m=str(times['car'][0]),
                                                             car_s=str(times['car'][1]),
                                                             bi_m=str(times['bicycle'][0]),
                                                             bi_s=str(times['bicycle'][1]),
                                                             w_m=str(times['walking'][0]),
                                                             w_s=str(times['walking'][1]))

    folium.Marker(
        location=coordinates[-1],
        popup=folium.Popup(html=message, max_width=160, sticy=True),
        icon=folium.Icon(color='red')
    ).add_to(m)

    # Add a colored line of the shortest path between two points
    my_polyline = folium.PolyLine(locations=coordinates, color='black', weight=5)
    m.add_child(my_polyline)
    output = 'UofTMap.html'
    m.save(output)      # save the HTML file of the map

    # Open a map
    url = 'file://{path}/{mapfile}'.format(path=os.getcwd(), mapfile=output)
    webbrowser.open(url, new=1)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'allowed-io': ['get_the_right_name'],
        'max-line-length': 100,
        'extra-imports': ['python_ta.contracts', 'typing', 'os', 'webbrowser',
                          'folium', 'dijkstra', 'vehicle_return_time', 'map_graph', 'difflib'],
        'disable': ['E1136', 'W0221']
    })
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    import doctest

    doctest.testmod()
