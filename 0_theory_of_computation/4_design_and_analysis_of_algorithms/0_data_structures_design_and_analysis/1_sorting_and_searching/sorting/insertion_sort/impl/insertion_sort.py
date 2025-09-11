from typing import List, Any


def sort(values: List[Any]):
    _sorted_values = []
    for v in values:
        for _v in _sorted_values:
            if v < _v:
