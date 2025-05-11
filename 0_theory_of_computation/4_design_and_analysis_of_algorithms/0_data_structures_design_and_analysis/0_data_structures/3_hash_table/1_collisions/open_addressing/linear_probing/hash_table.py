class HashTableLinearProbing:

    def __init__(self):
        self._MAX = 1000_000
        self._items = [None] * self._MAX

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

    def __getitem__(self, key):
        item_index = self._calculate_hash(key)
        item = self._items[item_index]

        if item is None:
            return None
        elif key == item[0]:
            return item[1]
        else:

            def _linear_probe(start, end):
                for i in range(start, end):
                    if self._items[i] is not None:
                        return i
                return None

            probed_idx = _linear_probe(item_index + 1, self._MAX)
            if probed_idx is not None:
                return self._items[probed_idx][1]
            else:
                probed_idx = _linear_probe(0, item_index)
                if probed_idx is not None:
                    return self._items[probed_idx][1]
                return None

    def __setitem__(self, key, value):
        index = self._calculate_hash(key)
        new_item = (key, value)
        if self._items[index] is None:
            self._items[index] = new_item
        elif key == self._items[index][0]:
            self._items[index] = new_item
        else:

            def _linear_probe(start, end):
                for i in range(start, end):
                    if self._items[i] is None:
                        return i
                return None

            probed_idx = _linear_probe(index + 1, self._MAX)
            if probed_idx is not None:
                self._items[probed_idx] = new_item
            else:
                probed_idx = _linear_probe(0, index)
                if probed_idx is not None:
                    self._items[probed_idx] = new_item
                else:
                    self._MAX = self._MAX * 2
                    new_items = [None] * self._MAX

                    for k, v in self._items:
                        new_items[self._calculate_hash(k)] = (k, v)

                    self._items = new_items
                    self._items[self._calculate_hash(key)] = new_item

    def __delitem__(self, key):
        idx = self._calculate_hash(key)
        item = self._items[idx]

        def _validate(v):
            if v is None:
                raise KeyError("No value found with supplied key")

        _validate(item)
        if key == item[0]:
            del self._items[idx]
        else:
            for i in range(idx, self._MAX):
                item = self._items[i]
                _validate(item)
                if key == item[0]:
                    del self._items[i]
                    return
