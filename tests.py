import unittest
from roster_utils import get_roster, get_next_id, add_to_roster

class TestRosterUtils(unittest.TestCase):

    FILEPATH = './test_roster.csv'

    def test_get_roster(self):
        test_roster = get_roster(self.FILEPATH)
        self.assertDictEqual({"id": '1', "first_name": "Fred", "last_name": "Flinstone"}, test_roster[0])
        self.assertDictEqual({"id": '2', "first_name": "Barnie", "last_name": "Rabble"}, test_roster[1])

    def test_get_next_id(self):
        next_id = get_next_id(self.FILEPATH)
        self.assertEqual(3, next_id)