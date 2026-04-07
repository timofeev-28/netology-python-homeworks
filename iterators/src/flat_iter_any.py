from typing import Iterator, List, Any


class FlatIterator:
    """takes a list any nesting and returns a sequence of elements"""

    @staticmethod
    def _get_list(lists: List[Any]) -> List[Any]:
        flat_list: List[Any] = []
        for el in lists:
            if isinstance(el, list):
                flat_list.extend(FlatIterator._get_list(el))
            else:
                flat_list.append(el)
        return flat_list

    def __init__(self, list_of_list):
        self.cursor: int = -1
        self.list = FlatIterator._get_list(list_of_list)

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        self.cursor += 1
        if self.cursor == len(self.list):
            raise StopIteration
        return self.list[self.cursor]


def test_3():
    """testing function"""
    list_of_lists_2 = [
        [["a"], ["b", "c"]],
        ["d", "e", [["f"], "h"], False],
        [1, 2, None, [[[[["!"]]]]], []],
    ]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_2),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None, "!"],
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == [
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
