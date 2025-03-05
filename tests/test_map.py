import unittest

from gig import EntType

from road_network import Map


class TestCase(unittest.TestCase):
    def test(self):
        ent_type = EntType.PROVINCE
        map = Map.from_ent_type(ent_type)
        self.assertEqual(len(map), 9)
        print(map.details)
