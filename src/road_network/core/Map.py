from dataclasses import dataclass

from gig import Ent, EntType
from utils import Log

from road_network.core.Place import Place

log = Log("Map")


@dataclass
class Map:
    places: list[Place]

    @staticmethod
    def from_ent_type(ent_type: EntType):
        return Map(
            places=[
                Place.from_ent(ent) for ent in Ent.list_from_type(ent_type)
            ]
        )

    def __len__(self):
        return len(self.places)

    def __str__(self):
        return f"Map({len(self)} places)"

    @property
    def details(self):
        return "\n".join(
            [
                str(self),
                *[
                    f"  {item[0]}) {item[1]}"
                    for item in enumerate(self.places, start=1)
                ],
                "-" * 40,
            ]
        )
