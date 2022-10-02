from typing import List


class Stats:
    def __init__(self, counter_list: List[int]):
        self.counter_list = counter_list

    @staticmethod
    def _get_lower_limit(lower: int) -> int:
        return lower if lower > 0 else 0

    def _stored_numbers_equals_to_lower(self, lower_limit: int) -> int:
        return self.counter_list[lower_limit] - self.counter_list[max(0, lower_limit - 1)]

    def _get_remaining_numbers_from_lower_to_upper(self, lower_limit: int, upper: int) -> int:
        return self.counter_list[upper] - self.counter_list[lower_limit]

    def less(self, number: int) -> int:
        if number <= 0:
            return 0

        return self.counter_list[number - 1]

    def between(self, lower: int, upper: int) -> int:
        lower_limit = self._get_lower_limit(lower)
        counter_lower = self._stored_numbers_equals_to_lower(lower_limit)
        remaining_numbers = self._get_remaining_numbers_from_lower_to_upper(lower_limit, upper)
        return counter_lower + remaining_numbers

    def greater(self, number: int) -> int:
        if number <= 0:
            return self.counter_list[number]
        return self.counter_list[-1] - self.counter_list[number]
