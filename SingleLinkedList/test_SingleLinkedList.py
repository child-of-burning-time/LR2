import unittest
from SingleLinkedList import SingleLinkedList

class test_SingleLinkedList(unittest.TestCase):

    def test_init(self):
        llist = SingleLinkedList()
        self.assertEqual(llist._length, 0)

    def test_len(self):
        llist = SingleLinkedList()
        self.assertEqual(len(llist), 0)

    def test_is_empty(self):
        llist = SingleLinkedList()
        self.assertTrue(llist.is_empty())
        llist.append(2)
        self.assertFalse(llist.is_empty())

    def test_append(self):
        llist = SingleLinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        self.assertEqual(len(llist), 3)
        self.assertEqual(f"{llist}", "[1, 2, 3]")

    def test_insert(self):
        llist = SingleLinkedList()
        llist.append(1)
        llist.insert(0, 2)
        self.assertEqual(len(llist), 2)
        self.assertEqual(f'{llist}', '[2, 1]')

    def test_str(self):
        llist = SingleLinkedList()
        llist.append(1)
        llist.append(2)
        self.assertEqual(str(llist), '[1, 2]')

    def test_contains(self):
        llist = SingleLinkedList()
        llist.append(1)
        self.assertTrue(llist.contains(1))
        self.assertFalse(llist.contains(2))

    def test_reverse(self):
        llist = SingleLinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.reverse()
        self.assertEqual(f'{llist}', '[3, 2, 1]')

    def test_get(self):
        llist = SingleLinkedList()
        llist.append(3)
        llist.append(8)
        self.assertEqual(llist.get(0), 3)

    def test_remove(self):
        llist = SingleLinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.remove(0)
        llist.remove(1)
        self.assertEqual(len(llist), 1)
        self.assertEqual(f'{llist}', '[2]')

    def test_search(self):
        llist = SingleLinkedList()
        llist.append(1)
        llist.append(2)
        self.assertTrue(llist.search(llist.get_head(), 1))
        self.assertFalse(llist.search(llist.get_head(), 0))

