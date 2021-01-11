# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


def stations_by_distance(stations, p):
    """ Function to calcuate the distannce between a station
    and the coordinate p, and returns a list of the station and
    the distance"""

    resulting_arr = []

    for station in stations:
        coord = station.coord
        distance = haversine(coord, p)

        resulting_arr.append((station, distance))

    return sorted_by_key(resulting_arr, 1, reverse=False)


def stations_within_radius(stations, centre, r):
    """
    Function returns a list of stations which are with a radius r of
    the centre coordinate
    """
    stations_distances = stations_by_distance(stations, centre)
    result_arr = []

    for tuple in stations_distances:
        if tuple[1] <= r:
            result_arr.append(tuple[0].name)
        else:
            break  # can break since the list is ordered by distance

    return result_arr


def rivers_with_station(stations):

    riversWithStation = set()

    for station in stations:
        if station.river is not None:
            riversWithStation.add(station.river)

    return riversWithStation


def stations_by_river(stations):

    riverStations = rivers_with_station(stations)

    stationsOnRiver = dict.fromkeys(riverStations)

    for station in stations:
        if stationsOnRiver[station.river] is not None:
            stationsOnRiver[station.river].append(station)
        else:
            stationsOnRiver[station.river] = [station]
    return stationsOnRiver
