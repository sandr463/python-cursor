import logging
from typing import Iterable, Union, List
import unittest


def increase_each_element(data: Union[List, ]) -> List:
    """
    Iterate throw data and increase each element on one.
    No react on invalid data
    Args:
        data: inout data
    Raises:
    Returns:

    """
    try:
        data = list(map(lambda x: x + 1, data))
    except Exception as e:
        pass
    return data


class TestThisShit(unittest.TestCase):

    def test_increase_each_element(self):
        input_data = [1, 2, 3, 4, 5]

        new_data = increase_each_element(input_data)
        self.assertEqual(sum(new_data), sum(input_data) + len(input_data))
        return

    def test_increase_not_valid_data(self):
        return

    def test_increase_empty_data(self):
        return

    def test_increase_dict_provided(self):
        return


if __name__ == "__main__":
    unittest.main()