#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WRS 2018 (navigation_planner).
This module is designed for navigation planning in virtual and real space.
This module is composed of functions allowing  to define the waypoints
to input to the navigation_stack module
Latest update: 04/04/18
Authors: A. Magassouba

"""

import json


def load_dict(loaded_file):
    """Load a dictionary

    :param loaded_file:

    """
    with open(loaded_file, encoding='utf-8') as data_file:
        loaded_dict = json.loads(data_file.read())
    return loaded_dict


def pos_to_room_id(env, pos):
    """Get the room in which the robot is located

    :param env:
    :param pos:

    """
    for item in env:
        if(pos["x"] > item["tl_x"] and pos["x"] < item["br_x"] and
           pos["y"] > item["tl_y"] and pos["y"] < item["br_y"]):
            return item["id"]
    return None


def reverse_w_pt(w_pt):
    """Reverse the trajectory waypoints and orientation angle in rad

    :param w_pt:

    """
    reversed_w_pt = list(reversed(w_pt))
    for item in reversed_w_pt:
        if item["theta"] == 0:
            item["theta"] = 3.14
        else:
            item["theta"] = -item["theta"]
    return reversed_w_pt


def room_to_room_navigation(way_points_file, source, goal):
    """From a waypoints file return the waypoint trajectory
       from the source to the goal

    :param way_points_file:
    :param source:
    :param goal:

    """
    for item in way_points_file:
        if source == item["source"] and goal == item["goal"]:
            return item["path"]
        if source == item["goal"] and goal == item["source"]:
            return reverse_w_pt(item["path"])


if __name__ == '__main__':
    # get target  instance ID from task info
    # (unity->)message #json
    ENV = load_dict('map.dat')
    # get target position in the scene
    PATH = load_dict('navigation_path.json')
    print("----Navigation from lobby to living room----")

    WPTS = room_to_room_navigation(PATH, "lobby", "living room")
    print(WPTS)
