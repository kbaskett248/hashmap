import unittest
from . import HashMap
import hashmap


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

    def test_get_missing(self):
        hash_map = HashMap()
        with self.assertRaises(KeyError):
            hash_map.get("Ferrari")

    def test_get_default(self):
        hash_map = HashMap()
        self.assertEqual(hash_map.get("Ferrari", "Testarossa"), "Testarossa")

    def test_delete(self):
        hash_map = HashMap(Nissan="GT-R")
        self.assertEqual(hash_map.delete("Nissan"), "GT-R")
        self.assertNotIn("Nissan", hash_map)

    def test_delete_missing(self):
        hash_map = HashMap(Chevrolet="Corvette")
        self.assertEqual(hash_map.delete("Chevrolet"), "Corvette")
        self.assertNotIn("Chevrolet", hash_map)

    def test_setitem(self):
        hash_map = HashMap()
        hash_map["Aston Martin"] = "Vanquish"

        self.assertEqual(hash_map.get("Aston Martin"), "Vanquish")

    def test_getitem(self):
        hash_map = HashMap(McLaren="P1")

        self.assertEqual(hash_map["McLaren"], "P1")

    def test_getitem_missing(self):
        hash_map = HashMap()

        with self.assertRaises(KeyError):
            hash_map["Fiat"]

    def test_delitem(self):
        hash_map = HashMap(Tesla="Model S")

        del hash_map["Tesla"]
        self.assertNotIn("Tesla", hash_map)

    def test_delitem_missing(self):
        hash_map = HashMap()

        with self.assertRaises(KeyError):
            del hash_map["Hennessey"]


if __name__ == "__main__":
    unittest.main()