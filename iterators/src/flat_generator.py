import types
from typing import Any, Generator, List


def flat_generator(
    list_of_lists: List[List[Any]],
) -> Generator[Any, None, None]:
    """
    function - genegator
    takes a list of lists and returns a sequence of elements
    """

    flat_list: List[Any] = [
        item for sublist in list_of_lists for item in sublist
    ]
    yield from flat_list


def test_2():
    """testing function"""
    list_of_lists_1 = [
        ["a", "b", "c"],
        ["d", "e", "f", "h", False],
        [1, 2, None],
    ]

    for flat_iterator_item, check_item in zip(
        flat_generator(list_of_lists_1),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None],
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "h",
        False,
        1,
        2,
        None,
    ]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
