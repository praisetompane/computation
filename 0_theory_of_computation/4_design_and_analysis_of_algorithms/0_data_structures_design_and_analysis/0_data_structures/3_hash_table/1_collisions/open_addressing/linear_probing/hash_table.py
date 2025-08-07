class HashTableLinearProbing:

    def __init__(self):
        self._MAX = 1000_000
        self._items = [None] * self._MAX

    def __getitem__(self, key):
        item_index = self._calculate_hash(key)

        if self._items[item_index] is None:
            return None
        elif key == self._items[item_index][0]:
            return self._items[item_index][1]
        else:
            for probe_idx in self._calculate_index_exploration_order(item_index):
                if self._items[probe_idx] is None:
                    return None
                elif key == self._items[probe_idx][0]:
                    return self._items[probe_idx][1]
            return None

    def __setitem__(self, key, value):
        item_index = self._calculate_hash(key)
        new_item = (key, value)

        if self._items[item_index] is None:
            self._items[item_index] = new_item
        elif key == self._items[item_index][0]:
            self._items[item_index] = new_item
        else:
            for probe_idx in self._calculate_index_exploration_order(item_index):
                if self._items[probe_idx] is None:
                    self._items[probe_idx] = new_item
                    return

            self._resize_hash_table()
            self._items[self._calculate_hash(key)] = new_item

    def __delitem__(self, key):
        item_index = self._calculate_hash(key)

        if self._items[item_index] is None:
            return None
        elif key == self._items[item_index][0]:
            del self._items[item_index]
        else:
            for probe_idx in self._calculate_index_exploration_order(item_index):
                if self._items[probe_idx] is None:
                    return None
                elif key == self._items[probe_idx][0]:
                    del self._items[probe_idx]
                    return

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

    def _calculate_index_exploration_order(self, start_index):
        return [*range(start_index, self._MAX)] + [*range(0, start_index)]

    def _resize_hash_table(self):
        """Resize hashtable to double its size and recompute hashes for existing values"""
        self._MAX = self._MAX * 2
        new_items = [None] * self._MAX

        for k, v in self._items:
            new_items[self._calculate_hash(k)] = (k, v)

        self._items = new_items
