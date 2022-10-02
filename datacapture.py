from typing import List

from stats import Stats


class DataCaptureException(Exception):
    pass


class DataCapture:
    def __init__(self):
        self.max = 0
        self.captured_numbers = {}

    def _update_max(self, number: int) -> None:
        if number > self.max:
            self.max = number

    def add(self, number: int) -> None:
        if number > 0:
            self.captured_numbers[number] = self.captured_numbers.get(number, 0) + 1
            self._update_max(number)

    def _get_updated_counter(self, index: int, counter_list: List[int]) -> List[int]:
        if index == 0:  # We will not process the 0 index as it represents the number zero, which is not positive
            return counter_list

        if self.captured_numbers.get(index) is not None:
            counter_list[index] = self.captured_numbers[index] + counter_list[max(0, index - 1)]
        else:
            counter_list[index] = counter_list[max(0, index - 1)]

        return counter_list

    def _build_counter_list(self) -> List[int]:
        # adds 1 as python lists indexes starts at 0, and this is not a positive number
        counter_list = [0] * (self.max + 1)
        for index, _ in enumerate(counter_list):
            counter_list = self._get_updated_counter(index, counter_list)
        return counter_list

    def build_stats(self) -> Stats:
        if not self.captured_numbers:
            raise DataCaptureException("You have not added any valid number")
        counter_list = self._build_counter_list()
        return Stats(counter_list)
