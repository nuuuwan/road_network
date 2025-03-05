from dataclasses import dataclass

from utils import Log

from road_network.core.Place import Place

log = Log("Road")


@dataclass
class Road:
    place1: Place
    place2: Place

    def __str__(self):
        return f"Road({self.place1} -> {self.place2})"
