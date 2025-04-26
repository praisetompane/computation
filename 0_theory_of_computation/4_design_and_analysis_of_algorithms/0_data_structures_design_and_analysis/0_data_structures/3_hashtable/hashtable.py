from typing import Any


class HashTable:
    """Basic Hash table implementation for educational purposes."""

    def __init__(self):
        self._size = 1_000_000
        self._items = [None] * self._size

    def _calculate_hash(self, key: str) -> int:
        """Computes an index in an key for they key

        Args:
            key (str): Item key in dictionary.

        Returns:
            int: Array index.

        Performance Analysis:
            let:
                N = number of character in key.
            then:
                time = O(N)
                space = O(1)
            remarks:
                For fixed length keys, this effectively becomes constant time.
        """
        ascii_ordinal_total = 0
        for c in key:
            ascii_ordinal_total += ord(c)

        return ascii_ordinal_total % self._size

    def __getitem__(self, key: str) -> Any:
        items = self._items[self._calculate_hash(key)]
        if items is None:
            return None
        elif not isinstance(items, list):
            return items[1]
        else:
            for k, v in items:
                if k == key:
                    return v
            return None

    def __setitem__(self, key: str, value: Any) -> None:
        index = self._calculate_hash(key)
        items = self._items[index]
        new_item = (key, value)
        if items is None:
            self._items[index] = new_item
        elif items[0] == key:
            self._items[index] = new_item
        else:
            current_item = self._items[index]
            # Check if it is already chained
            if not isinstance(current_item, list):
                self._items[index] = [current_item, new_item]
            else:
                # Search and update in chain if key-value pair already exists
                for i in range(0, len(self._items[index])):
                    if self._items[index][i][0] == key:
                        self._items[index][i] = new_item
                        return
                self._items[index].append(new_item)

    def __delitem__(self, key: str):
        index = self._calculate_hash(key)
        items = self._items[index]

        if items is not None:
            if not isinstance(items, list):
                del self._items[index]
            else:
                for i in range(0, len(items)):
                    if self._items[index][i][0] == key:
                        del self._items[index][i]
                        return None
        else:
            return None
