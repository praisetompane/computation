class HashTable:
    """Basic Hash table implementation for educational purposes."""

    def __init__(self):
        self.size = 1_000_000
        self.items = [None] * self.size

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

        return ascii_ordinal_total % self.size

    def __getitem__(self, key):
        return self.items[self._calculate_hash(key)]

    def __setitem__(self, key, item):
        self.items[self._calculate_hash(key)] = item
