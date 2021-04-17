import unittest
from . import HashMap


class TestHashMap(unittest.TestCase):
    """Test the HashMap class"""

    def test_create(self):
        hash_map = HashMap()
        self.assertIsNotNone(hash_map)

    def test_create_from_list(self):
        l = [("Mazda", "Miata"), ("Toyota", "2000 GT"), ("Subaru", "WRX")]
        hash_map = HashMap(l)
        self.assertIsNotNone(hash_map)

        for key, value in l:
            self.assertEqual(hash_map.get(key), value)

    def test_create_from_kwargs(self):
        hash_map = HashMap(Mazda="Miata", Toyota="Celica", Hyundai="Elantra GT")
        self.assertIsNotNone(hash_map)

        self.assertEqual(hash_map.get("Mazda"), "Miata")
        self.assertEqual(hash_map.get("Toyota"), "Celica")
        self.assertEqual(hash_map.get("Hyundai"), "Elantra GT")

    def test_set_and_get(self):
        hash_map = HashMap()
        hash_map.set("Ford", "Mustang")

        self.assertIn("Ford", hash_map)
        self.assertEqual(hash_map.get("Ford"), "Mustang")

        hash_map.set("Ford", "Focus")
        self.assertIn("Ford", hash_map)
        self.assertEqual(hash_map.get("Ford"), "Focus")


if __name__ == "__main__":
    unittest.main()