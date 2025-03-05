from dataclasses import dataclass

from gig import Ent
from utils import LatLng, Log

log = Log("Place")


@dataclass
class Place:
    id: str
    name: str
    population: float
    latlng: LatLng

    @staticmethod
    def from_ent(ent: Ent):
        return Place(
            id=ent.id,
            name=ent.name,
            population=ent.population / 1_000,
            latlng=LatLng(*ent.centroid),
        )

    def __str__(self):
        return f"Place({self.id}, {self.name})"

    def distance(self, other: "Place") -> float:
        return self.latlng.distance(other.latlng)
