import unittest
from taxi import manhattan_distance, visited_twice


class TestCase(unittest.TestCase):
    def test_manhattan_distance(self):
        self.assertEqual(5, manhattan_distance('R2, L3'))
        self.assertEqual(2, manhattan_distance('R2, R2, R2'))
        self.assertEqual(12, manhattan_distance('R5, L5, R5, R3'))

    def test_visited_twice(self):
        self.assertEqual(4, visited_twice('R8, R4, R4, R8'))


if __name__ == '__main__':
    unittest.main()
