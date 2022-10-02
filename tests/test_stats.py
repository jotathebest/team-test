import unittest
from unittest.mock import patch

from stats import Stats


class TestStats(unittest.TestCase):
    def setUp(self) -> None:
        #                   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.counter_list = [0, 0, 0, 2, 3, 3, 4, 4, 4, 5]
        self.test_instance = Stats(self.counter_list)

    def test_less(self):
        number = 0
        assert not self.test_instance.less(number)
        number = 4
        assert 2 == self.test_instance.less(number)

    def test_get_lower_limit(self):
        lower = -1
        assert 0 == self.test_instance._get_lower_limit(lower)
        lower = 1
        assert 1 == self.test_instance._get_lower_limit(lower)

    def test__stored_numbers_equals_to_lower(self):
        lower_limit = 0
        assert 0 == self.test_instance._stored_numbers_equals_to_lower(lower_limit)
        lower_limit = 4
        assert 1 == self.test_instance._stored_numbers_equals_to_lower(lower_limit)

    def test__get_remaining_numbers_from_lower_to_upper(self):
        lower = 1
        upper = 2
        assert 0 == self.test_instance._get_remaining_numbers_from_lower_to_upper(lower, upper)
        upper = 5
        assert 3 == self.test_instance._get_remaining_numbers_from_lower_to_upper(lower, upper)

    @patch.object(Stats, "_get_remaining_numbers_from_lower_to_upper")
    @patch.object(Stats, "_stored_numbers_equals_to_lower")
    @patch.object(Stats, "_get_lower_limit")
    def test_between(self,
                     mock__get_lower_limit,
                     mock__stored_numbers_equals_to_lower,
                     mock__get_remaining_numbers_from_lower_to_upper):
        lower = 3
        upper = 6
        counter_lower = 1
        remaining_numbers = 2
        mock__get_lower_limit.return_value = lower
        mock__stored_numbers_equals_to_lower.return_value = counter_lower
        mock__get_remaining_numbers_from_lower_to_upper.return_value = remaining_numbers
        result = self.test_instance.between(lower, upper)
        mock__get_lower_limit.assert_called_with(lower)
        mock__stored_numbers_equals_to_lower.assert_called_with(lower)
        mock__get_remaining_numbers_from_lower_to_upper.assert_called_with(lower, upper)
        assert result == counter_lower + remaining_numbers

    def test_greater(self):
        number = -1
        assert self.counter_list[-1] == self.test_instance.greater(number)
        number = 4
        assert 2 == self.test_instance.greater(number)


if __name__ == '__main__':
    unittest.main()
