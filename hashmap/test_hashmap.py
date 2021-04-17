import unittest
from . import HashMap


class TestHashMap(unittest.TestCase):
    """Test the HashMap class"""

    def test_create(self):
        hash_map = HashMap()
        self.assertIsNotNone(hash_map)

    def test_create_from_list(self):
        hash_map = HashMap([("a", 1), ("b", 2), ("c", 3)])
        self.assertIsNotNone(hash_map)

    def test_create_from_kwargs(self):
        hash_map = HashMap(a=1, b=2, c=3)
        self.assertIsNotNone(hash_map)

    def test_set(self):
        hash_map = HashMap()
        hash_map.set("Ford", "Mustang")

        self.assertIn("Ford", hash_map)
        self.assertEqual(hash_map.get("Ford"), "Mustang")

        hash_map.set("Ford", "Focus")
        self.assertIn("Ford", hash_map)
        self.assertEqual(hash_map.get("Ford"), "Focus")


if __name__ == "__main__":
    unittest.main()