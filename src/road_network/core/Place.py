from dataclasses import dataclass

from gig import Ent
from utils import LatLng, Log

log = Log("Place")


@dataclass
class Place:
    id: str
    name: str
    population: int
    latlng: LatLng

    @staticmethod
    def from_ent(ent: Ent):
        return Place(
            id=ent.id,
            name=ent.name,
            population=ent.population,
            latlng=LatLng(*ent.centroid),
        )

    def __str__(self):
        return f"Place({self.id}, {self.name})"
