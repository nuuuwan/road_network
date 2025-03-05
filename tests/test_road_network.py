import unittest

from gig import EntType

from road_network import Map, RoadNetwork


class TestCase(unittest.TestCase):
    def test(self):
        map = Map.from_ent_type(EntType.PROVINCE)
        road_network = RoadNetwork.build_from_map(map)
        self.assertEqual(len(road_network), 1)
        print(road_network.details)
