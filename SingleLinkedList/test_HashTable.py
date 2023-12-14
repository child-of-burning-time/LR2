import unittest
from HashTable import HashTable

class test_HashTable(unittest.TestCase):

    def test_init(self):
        hash_table = HashTable(5)
        self.assertEqual(hash_table._size, 0)

    def test_hash(self):
        hash_table = HashTable(5)
        a = hash_table._hash("q")
        b = hash_table._hash("q")
        self.assertEqual(a, b)

    def test_size(self):
        hash_table = HashTable(5)
        hash_table.put("qwerty", 35566)
        self.assertEqual(hash_table.size(), 1)

    def test_get(self):
        hash_table = HashTable(5)
        hash_table.put("qwerty", 35566)
        self.assertEqual(hash_table.get("qwerty"), 35566)

    def test_put(self):
        hash_table = HashTable(5)
        hash_table.put("qwerty", 35566)
        self.assertEqual(hash_table.size(), 1)
        self.assertEqual(hash_table.get("qwerty"), 35566)

    def test_remove(self):
        hash_table = HashTable(5)
        hash_table.put("qwerty", 35566)
        hash_table.remove("qwerty")
        self.assertEqual(hash_table.size(), 0)

    def test_str(self):
        hash_table = HashTable(5)
        hash_table.put("qwerty", 35566)
        self.assertEqual(str(hash_table), '(qwerty, 35566) ')

    def test_resize(self):
        hash_table = HashTable(5)
        hash_table.put("qwerty", 35566)
        hash_table.put("qaz", 644)
        hash_table.put("xyz", 7888552)
        hash_table.put("rfkngrgr", 979898998)
        hash_table.put("dighdhpj", 35554654536545)
        self.assertEqual(hash_table._capacity, 10)

    def test_contains(self):
        hash_table = HashTable(5)
        hash_table.put("qwerty", 35566)
        self.assertTrue(hash_table.contains("qwerty"))
        self.assertFalse(hash_table.contains("xihgidgjidjg"))
