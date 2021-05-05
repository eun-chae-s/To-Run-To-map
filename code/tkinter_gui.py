"""CSC111 Winter 2021 Project: To-Run-To Map

Module Description
==================
This module contains the functions for running the TKinter graphic user interface. It handles
clicking buttons, writing inputs, and clicking Radiobutton. It displays a pop up interface for
users to input their departure and destination.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Jihyuk Yoon, Yeong Jae Ryu, Eunchae Seong, and Taewoong Oh.
"""
from difflib import get_close_matches
from tkinter import Tk, Label, Button, Entry, StringVar, Radiobutton
from visualize_map import visualize_map_graph
from map_graph import MapGraph


def gui_generator(graph: MapGraph, building_lst: list) -> None:
    """ Runs the TKinter. Initializes the TKinter, adds labels, and
    Calls on functions for handling
    """
    root = Tk()

    root.title("To-Run-To Map")

    intro_label = Label(root, text="To-Run-To Map", font=("American Typewriter", 18, 'bold'),
                        fg='RoyalBlue4')
    intro_label.pack()

    msg_label = Label(root, text="Please enter the full name of the building you are searching for",
                      font=("Helvetica", 12, "italic"))
    msg_label.pack()

    # Entry Box for Search Start
    e1 = Entry(root, width=50)
    e1.pack()

    # Variable for Radiobutton for departure
    r1 = StringVar()

    # Search Button for start departure
    Button(root, text="Search Start",
           command=lambda: search_start(root, e1, r1, building_lst)).pack(pady=4)

    # Entry Box for Search Destination
    e2 = Entry(root, width=50)
    e2.pack()

    # Variable for Radiobutton for destination
    r2 = StringVar()

    # Search Button for destination
    Button(root, text="Search Destination",
           command=lambda: search_destination(root, e2, r2, building_lst)).pack(pady=4)

    ending_label = Label(root, text="Click 'Open Map' after you have selected the start and "
                                    "end points")
    ending_label.pack()

    # Open Map Button
    Button(root, text="Open Map", command=lambda: clicked(r1, r2, graph, root),
           bg="ghost white", fg="cornflower blue", font=("Helvetica", 14, "bold")).pack(pady=2)

    root.mainloop()


def search_start(root: Tk, e1: Entry, r1: StringVar, building_lst: list) -> None:
    """Function for handling the event of clicking on the "Search start" button.
    Opens a set of Radiobutton for options as destinations.
    """
    t = e1.get()
    # If the search entry is less than 3 letters, ask to add more words
    if len(t) < 3:
        my_label = Label(root, text="Please enter a minimum of 3 letters.",
                         fg="FireBrick4", font=("Helvetica", 12, "italic"))
        my_label.pack()
        return

    # Using the difflib library to get the closest words
    options = get_close_matches(t, building_lst)

    # Finding buildings in the list that contains the word that has been typed
    for b in building_lst:
        if t.lower() in b.lower() and b not in options:
            options.append(b)

    options = options[:5]

    # If options is empty, ask the user to re-input the search
    if options == []:
        my_label = Label(root, text="* This does not exist, please search again",
                         fg="FireBrick4", font=("Helvetica", 12, "italic"))
        my_label.pack()

    # Otherwise, go through the words in the options and make Radiobuttons for them
    else:
        depart = Label(root,
                       text="------------------------- Departure -------------------------",
                       font=("Helvetica", 14, 'bold'), fg='RoyalBlue4')
        depart.pack()

        # Initialize a list to save the Radiobutton
        rb_lst = []
        i = 0
        for opt in options:
            rb1 = Radiobutton(root, text=opt, variable=r1, value=opt)
            rb1.pack()
            rb_lst.append(rb1)
            i += 1
        my_label = Label(root, text="* If the option you were looking for is not in the list \n"
                                    "please search again", fg="firebrick4",
                         font=("Helvetica", 12, "italic"))
        my_label.pack()
        clear_button = \
            Button(root, text="Clear",
                   command=lambda: clear_items(depart, my_label, rb_lst, clear_button), fg="grey17")
        clear_button.pack()


def search_destination(root: Tk, e2: Entry, r2: StringVar, building_lst: list) -> None:
    """Function for handling the event of clicking on the "Search Destination" button.
    Opens a set of Radiobuttons for options as destinations.
    """
    t2 = e2.get()

    # If the search entry is less than 3 letters, ask to add more words
    if len(t2) < 3:
        my_label = Label(root, text="Please enter a minimum of 3 letters.",
                         fg="FireBrick4", font=("Helvetica", 12, "italic"))
        my_label.pack()
        return

    # Using the difflib library to get the closest words
    options = get_close_matches(t2, building_lst)

    # Finding buildings in the list that contains the word that has been typed
    for b in building_lst:
        if t2.lower() in b.lower() and b not in options:
            options.append(b)

    options = options[:5]

    # If options is empty, ask the user to re-input the search
    if options == []:
        my_label = Label(root, text="* This does not exist, please search again", fg="FireBrick4",
                         font=("Helvetica", 12, "italic"))
        my_label.pack()

    # Otherwise, go through the words in the options and make Radiobuttons for them
    else:
        destin = Label(root,
                       text="-------------------------- Destination --------------------------",
                       font=("Helvetica", 14, 'bold'), fg='RoyalBlue4')
        destin.pack()

        # Initialize a list to save the Radiobutton
        rb_lst = []
        i = 0
        for opt in options:
            rb1 = Radiobutton(root, text=opt, variable=r2, value=opt)
            rb1.pack()
            rb_lst.append(rb1)
            i += 1

        my_label = Label(root, text="* If the option you were looking for is not in the list \n"
                                    "please search again", fg="firebrick4",
                         font=("Helvetica", 12, "italic"))

        my_label.pack()

        clear_button = \
            Button(root, text="Clear",
                   command=lambda: clear_items(destin, my_label, rb_lst, clear_button), fg="grey17")
        clear_button.pack()


def clear_items(label1: Label, label2: Label, rb_lst: list, forget_button: Button) -> None:
    """Hopefully deletes it when I click clear."""
    label1.destroy()
    label2.destroy()
    for rb in rb_lst:
        rb.destroy()
    forget_button.destroy()


def clicked(val1: StringVar, val2: StringVar, graph: MapGraph, root: Tk) -> None:
    """Function for handling the event of clicking the "Open Map" button.
    Visualizes the map.
    """
    val1_str = str(val1.get())
    val2_str = str(val2.get())
    if val1_str == '' or val2_str == '':
        my_label = Label(root, text="Please select both the departure and the destination"
                                    " before clicking Open Map", fg='firebrick4',
                         font=("Helvetica", 12, "italic"))
        my_label.pack()
    else:
        visualize_map_graph(val1_str, val2_str, graph)


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['python_ta.contracts', 'typing', 'distance', 'tkinter', 'visualize_map',
                          'map_graph', 'difflib'],
        'disable': ['E1136', 'W0221', 'R0914']
    })
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    import doctest

    doctest.testmod()
