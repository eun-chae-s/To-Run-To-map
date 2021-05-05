"""CSC111 Winter 2021 Project: To-Run-To Map

Module Description
==================
This file contains the main code to run the map from the beginning to the end.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Jihyuk Yoon, Yeong Jae Ryu, Eunchae Seong, and Taewoong Oh.
"""
from load_weighted_graph import load_weighted_graph
from buildings_list import buildings_list
from tkinter_gui import gui_generator

if __name__ == '__main__':
    building_file = 'Data/UofTMap.json'
    corner_file = 'Data/full_corner.json'

    graph = load_weighted_graph(building_file, corner_file)
    building_lst = buildings_list(building_file)

    # Open GUI and get the map between two places
    gui_generator(graph, building_lst)
