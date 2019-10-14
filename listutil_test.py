import unittest
from listutil import unique


class ListUtilTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual([], unique([]))

    def test_single_item_list(self):
        self.assertListEqual(['hi'], unique(['hi']))
        self.assertListEqual([0], unique([0]))

    def test_single_item_many_times(self):
        self.assertListEqual([0], unique([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        self.assertListEqual(['a'], unique(
            ['a', 'a', 'a', 'a', 'a', 'a', 'a']))

    def test_two_items_many_times_many_orders(self):
        self.assertListEqual(['love', 'you'], unique(
            ['love', 'you', 'you', 'you', 'love', 'you', 'love']))
        self.assertListEqual([0, 4], unique([0, 0, 4, 4, 0, 4, 0, 4, 4, 4]))

    def test_argument_not_a_list(self):
        self.assertListEqual([5, 4, 6, [1, 3, 2]],
                             unique([5, 4, 6, [1, 3, 2]]))

    def test_many_items_not_duplicates(self):
        self.assertListEqual(['M', 'A', 'R', 'K'],
                             unique(['M', 'A', 'R', 'K']))

    def test_many_items_duplicates(self):
        self.assertListEqual(['s', 'k', 'e'], unique(
            ['s', 'k', 'k', 'e', 'e', 'e']))


if __name__ == '__main__':
    unittest.main()
