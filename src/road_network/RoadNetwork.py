from dataclasses import dataclass

from utils import Log

from road_network.core.Map import Map
from road_network.core.Road import Road

log = Log("RoadNetwork")


@dataclass
class RoadNetwork:
    roads: list[Road]

    @staticmethod
    def build_from_map(map: Map):  # dummy
        return RoadNetwork(
            roads=[
                Road(map.places[0], map.places[1]),
            ]
        )

    def __len__(self):
        return len(self.roads)

    def __str__(self):
        return f"RoadNetwork({len(self)} roads)"

    @property
    def details(self):
        return "\n".join(
            [
                str(self),
                *[
                    f"  {item[0]}) {item[1]}"
                    for item in enumerate(self.roads, start=1)
                ],
                "-" * 40,
            ]
        )
