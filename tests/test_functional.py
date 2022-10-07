import unittest

from datacapture import DataCapture


class TestStats(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_example(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        assert 2 == stats.less(4)
        assert 4 == stats.between(3, 6)
        assert 1 == stats.between(5, 6)
        assert 0 == stats.between(7, 8)
        assert 2 == stats.greater(4)
        assert 5 == stats.greater(-1)
        assert 5 == stats.greater(-10)
        assert 5 == stats.greater(0)

    def test_between(self):
        capture = DataCapture()
        capture.add(2)
        capture.add(7)
        capture.add(2)
        capture.add(2)
        stats = capture.build_stats()
        assert 0 == stats.between(3, 4)
        assert 0 == stats.between(3, 6)
        assert 0 == stats.between(1, 1)
        assert 3 == stats.between(2, 2)
        assert 1 == stats.between(3, 7)


if __name__ == '__main__':
    unittest.main()
