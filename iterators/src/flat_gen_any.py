import types
from typing import Any, Generator, List


def get_list(lists: List[Any]) -> List[Any]:
    """takes a list any nesting and returns this list flat"""

    flat_list: List[Any] = []
    for el in lists:
        if isinstance(el, list):
            flat_list.extend(get_list(el))
        else:
            flat_list.append(el)
    return flat_list


def flat_generator(
    list_of_lists: List[Any],
) -> Generator[Any, None, None]:
    """
    function - genegator
    takes a list any nesting and returns a sequence of elements
    """

    flat_list: List[Any] = get_list(list_of_lists)
    yield from flat_list


def test_4():
    """testing function"""
    list_of_lists_2 = [
        [["a"], ["b", "c"]],
        ["d", "e", [["f"], "h"], False],
        [1, 2, None, [[[[["!"]]]]], []],
    ]

    for flat_iterator_item, check_item in zip(
        flat_generator(list_of_lists_2),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None, "!"],
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == [
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
        "!",
    ]

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)
