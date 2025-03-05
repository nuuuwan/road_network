from dataclasses import dataclass
from functools import cached_property

import numpy as np
from utils import Log

from road_network.core.Map import Map
from road_network.core.Road import Road

log = Log("RoadNetwork")


@dataclass
class RoadNetwork:
    map: Map
    roads: list[Road]

    SPEED_WALKING = 5
    SPEED_ON_ROAD = 25

    @staticmethod
    def build_from_map(map: Map):
        # We are going to build RoadNetwork, by adding one Road at a time, such that
        # we pick the Road such that average_traveL_time is minimized.
        return RoadNetwork(map=map, roads=[])

    def __len__(self):

        return len(self.roads)

    def __str__(self):
        return f"RoadNetwork({len(self)} roads)"

    @cached_property
    def details(self):
        return "\n".join(
            [
                str(self),
                *[
                    f"  {item[0]}) {item[1]}"
                    for item in enumerate(self.roads, start=1)
                ],
                f"average_traveL_time={self.average_travel_time:.2f}hr",
                "-" * 40,
            ]
        )

    @cached_property
    def total_population(self) -> int:
        return sum(place.population for place in self.map.places)

    @cached_property
    def total_population2(self) -> int:
        return self.total_population**2

    @cached_property
    def population2_matrix(self) -> np.ndarray:
        n = len(self.map)
        matrix = np.zeros((n, n), dtype=int)
        for i, place1 in enumerate(self.map.places):
            for j, place2 in enumerate(self.map.places):
                matrix[i, j] = place1.population * place2.population
        return matrix

    @cached_property
    def connection_matrix(self) -> np.ndarray:
        n = len(self.map)
        matrix = np.zeros((n, n), dtype=int)
        for road in self.roads:
            i = self.map.places.index(road.place1)
            j = self.map.places.index(road.place2)
            matrix[i, j] = 1
            matrix[j, i] = 1
        return matrix

    @cached_property
    def distance_matrix(self) -> np.ndarray:
        n = len(self.map)
        matrix = np.zeros((n, n), dtype=float)
        for i, place1 in enumerate(self.map.places):
            for j, place2 in enumerate(self.map.places):
                matrix[i, j] = place1.distance(place2)
        return matrix

    @cached_property
    def speed_matrix(self) -> np.ndarray:
        return np.where(
            self.connection_matrix,
            RoadNetwork.SPEED_ON_ROAD,
            RoadNetwork.SPEED_WALKING,
        )

    @cached_property
    def travel_time_matrix(self) -> np.ndarray:
        return self.distance_matrix / self.speed_matrix

    @cached_property
    def average_travel_time(self) -> float:
        # = travel_time_matrix, weighted by population matrix, and averaged

        return (
            np.sum(self.travel_time_matrix * self.population2_matrix)
            / self.total_population2
        )
