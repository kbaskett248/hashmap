import unittest
from . import HashMap


class TestHashMap(unittest.TestCase):
    """Test the HashMap class"""

    def test_create(self):
        """Verify a HashMap can be created."""
        hash_map = HashMap()
        self.assertIsNotNone(hash_map)

    def test_create_from_list(self):
        """Verify a HashMap can be created from a list of key-value tuples."""
        l = [("Mazda", "Miata"), ("Toyota", "2000 GT"), ("Subaru", "WRX")]
        hash_map = HashMap(l)
        self.assertIsNotNone(hash_map)

        for key, value in l:
            self.assertEqual(hash_map.get(key), value)

    def test_create_from_kwargs(self):
        """Verify a HashMap can be created using keyword arguments."""
        hash_map = HashMap(Mazda="Miata", Toyota="Celica", Hyundai="Elantra GT")
        self.assertIsNotNone(hash_map)

        self.assertEqual(hash_map.get("Mazda"), "Miata")
        self.assertEqual(hash_map.get("Toyota"), "Celica")
        self.assertEqual(hash_map.get("Hyundai"), "Elantra GT")

    def test_expansion(self):
        """Verify expansion of the HashMap works and maintains existing values."""
        hash_map = HashMap()
        for j in range(2200):
            hash_map[j] = str(j)

        self.assertEqual(len(hash_map), 2200)
        self.assertIn(1234, hash_map)
        self.assertEqual(hash_map[1234], "1234")

    def test_set_and_get(self):
        """Verify set adds or replaces a value and get retrieves a value."""
        hash_map = HashMap()
        hash_map.set("Ford", "Mustang")

        self.assertIn("Ford", hash_map)
        self.assertEqual(hash_map.get("Ford"), "Mustang")
        self.assertEqual(len(hash_map), 1)

        hash_map.set("Ford", "Focus")
        self.assertIn("Ford", hash_map)
        self.assertEqual(hash_map.get("Ford"), "Focus")
        self.assertEqual(len(hash_map), 1)

    def test_get_missing(self):
        """Verify a KeyError is raised when getting a missing key."""
        hash_map = HashMap()
        with self.assertRaises(KeyError):
            hash_map.get("Ferrari")

    def test_get_default(self):
        """Verify getting a missing key with a default specified returns the default."""
        hash_map = HashMap()
        self.assertEqual(hash_map.get("Ferrari", "Testarossa"), "Testarossa")

    def test_delete(self):
        """Verify a value can be deleted."""
        hash_map = HashMap(Nissan="GT-R")
        self.assertIn("Nissan", hash_map)
        self.assertEqual(hash_map.delete("Nissan"), "GT-R")
        self.assertNotIn("Nissan", hash_map)

    def test_delete_missing(self):
        """Verify deleting a missing value will raise a KeyError."""
        hash_map = HashMap()
        with self.assertRaises(KeyError):
            hash_map.delete("Saturn")

    def test_setitem(self):
        """Verify a value can be set using [] syntax."""
        hash_map = HashMap()
        hash_map["Aston Martin"] = "Vanquish"

        self.assertEqual(hash_map.get("Aston Martin"), "Vanquish")

        hash_map["Aston Martin"] = "DB-S"
        self.assertEqual(hash_map.get("Aston Martin"), "DB-S")

    def test_getitem(self):
        """Verify a value can be retrieved using [] syntax."""
        hash_map = HashMap(McLaren="P1")

        self.assertEqual(hash_map["McLaren"], "P1")

    def test_getitem_missing(self):
        """Verify retrieving a missing key with [] syntax raises a KeyError."""
        hash_map = HashMap()

        with self.assertRaises(KeyError):
            hash_map["Fiat"]

    def test_delitem(self):
        """Verify a value can be deleted using [] syntax."""
        hash_map = HashMap(Tesla="Model S")

        del hash_map["Tesla"]
        self.assertNotIn("Tesla", hash_map)

    def test_delitem_missing(self):
        """Verify a KeyError is raised when trying to delete a missing key."""
        hash_map = HashMap()

        with self.assertRaises(KeyError):
            del hash_map["Hennessey"]

    def test_len(self):
        """Verify len() returns the number of items in the HashMap."""
        hash_map = HashMap()
        self.assertEqual(len(hash_map), 0)

        hash_map["Volkswagen"] = "GTI"
        self.assertEqual(len(hash_map), 1)

        del hash_map["Volkswagen"]
        self.assertEqual(len(hash_map), 0)

    def test_iterable(self):
        """Verify a HashMap is iterable and iterates over the key-value pairs."""
        cars = set(
            (("Chrysler", "Crossfire"), ("Dodge", "Viper"), ("Jeep", "Wrangler"))
        )
        hash_map = HashMap(cars)

        self.assertEqual(set((key, value) for key, value in hash_map), cars)

    def test_str(self):
        """Verify the HashMap has a nice string representation."""
        hash_map = HashMap(Audi="Quattro", Mercedes="S Class")
        self.assertEqual(
            str(hash_map), "HashMap('Audi': 'Quattro', 'Mercedes': 'S Class')"
        )


if __name__ == "__main__":
    unittest.main()