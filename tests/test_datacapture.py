import unittest
from unittest.mock import patch

from datacapture import DataCapture, DataCaptureException
from stats import Stats


class TestDataCapture(unittest.TestCase):
    def setUp(self) -> None:
        self.test_instance = DataCapture()

    def test_add_does_not_update_stored_numbers(self):
        error_message = "Only numbers greater than zero are allowed"
        with self.assertRaises(DataCaptureException) as context:
            number = 0
            self.test_instance.add(number)
        assert error_message in context.exception.args[0]
        with self.assertRaises(DataCaptureException) as context:
            number = -1
            self.test_instance.add(number)
        assert error_message in context.exception.args[0]

    def test_add_updates_stored_numbers(self):
        number = 2
        self.test_instance.add(number)
        assert self.test_instance.captured_numbers[number] == 1
        self.test_instance.add(number)
        assert self.test_instance.captured_numbers[number] == 2
        number_2 = 3
        self.test_instance.add(number_2)
        assert self.test_instance.captured_numbers[number_2] == 1

    @patch.object(DataCapture, "_update_max")
    def test_add_updates_max(self, mock__update_max):
        number = 2
        mock__update_max.return_value = None
        self.test_instance.add(number)
        mock__update_max.assert_called_with(number)

    def test__update_max(self):
        number = self.test_instance.max + 1
        self.test_instance._update_max(number)
        assert self.test_instance.max == number

    def test__build_counter_list_do_not_add_not_inserted_numbers(self):
        self.test_instance.max = 9
        self.test_instance.captured_numbers = {3: 2, 4: 1, 9: 1, 6: 1}
        # counter [0, 0, 0, 2, 3, 3, 4, 4, 4, 5]
        # numbers [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = [0, 0, 0, 2, 3, 3, 4, 4, 4, 5]
        result = self.test_instance._build_counter_list()
        assert expected == result

    def test__build_counter_list_adds_limit_number_counters(self):
        self.test_instance.max = 9
        self.test_instance.captured_numbers = {1: 5, 9: 1}
        # counter [0, 5, 5, 5, 5, 5, 5, 5, 5, 6]
        # numbers [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = [0, 5, 5, 5, 5, 5, 5, 5, 5, 6]
        result = self.test_instance._build_counter_list()
        assert expected == result

    @patch.object(DataCapture, "_get_updated_counter")
    def test__build_counter_list_invokes_get_updated_counter(self, mock__get_updated_counter):
        mock__get_updated_counter.return_value = []
        self.test_instance.captured_numbers = {1: 2}
        self.test_instance.max = 1
        self.test_instance._build_counter_list()
        mock__get_updated_counter.assert_called()

    def test__get_updated_counter_item_zero(self):
        counter_list = [0, 0]
        index = 0
        self.test_instance.captured_numbers = {}
        result = self.test_instance._get_updated_counter(index, counter_list)
        assert result == counter_list

        self.test_instance.captured_numbers = {0: 10}
        result = self.test_instance._get_updated_counter(index, counter_list)
        assert result == [0, 0]

    def test__get_updated_counter(self):
        counter_list = [0, 0]
        index = 1
        self.test_instance.captured_numbers = {}
        result = self.test_instance._get_updated_counter(index, counter_list)
        assert result == counter_list

        self.test_instance.captured_numbers = {1: 20}
        result = self.test_instance._get_updated_counter(index, counter_list)
        assert result == [0, 20]

    def test_build_stats(self):
        self.test_instance.add(5)
        stats = self.test_instance.build_stats()
        assert isinstance(stats, Stats)

    def test_build_stats_raises_exception_if_there_are_not_stored_numbers(self):
        with self.assertRaises(DataCaptureException) as context:
            self.test_instance.build_stats()
            assert "You have not added any valid number" in context


if __name__ == '__main__':
    unittest.main()
