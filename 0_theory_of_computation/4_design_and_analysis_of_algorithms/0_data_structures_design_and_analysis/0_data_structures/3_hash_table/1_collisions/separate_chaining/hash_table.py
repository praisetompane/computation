from typing import Any


class HashTable:
    """Basic Hash table implementation for educational purposes."""

    def __init__(self):
        self._MAX = 1_000_000
        self._items = [[] for _ in range(self._MAX)]

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

        return ascii_ordinal_total % self._MAX

    def __getitem__(self, key: str) -> Any:
        index = self._calculate_hash(key)

        for k, v in self._items[index]:
            if k == key:
                return v
        return None

    def __setitem__(self, key: str, value: Any) -> None:
        index = self._calculate_hash(key)
        new_item = (key, value)

        for idx, (k, _) in enumerate(self._items[index]):
            if k == key:
                self._items[index][idx] = new_item
                return

        self._items[index].append(new_item)

    def __delitem__(self, key: str):
        index = self._calculate_hash(key)

        for idx, (k, _) in enumerate(self._items[index]):
            if k == key:
                del self._items[index][idx]
