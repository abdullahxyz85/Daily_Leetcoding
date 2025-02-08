import collections
import sortedcontainers

class NumberContainers:
    def __init__(self):
        self.index_map = {}  # Maps index -> number
        self.number_map = collections.defaultdict(sortedcontainers.SortedSet)  # Maps number -> sorted set of indices

    def change(self, index: int, number: int) -> None:
        if index in self.index_map:
            old_number = self.index_map[index]
            if old_number in self.number_map:
                self.number_map[old_number].discard(index)  # Remove old index from its previous number's set

        self.index_map[index] = number
        self.number_map[number].add(index)  # Add new index to the number's sorted set

    def find(self, number: int) -> int:
        if number in self.number_map and self.number_map[number]:
            return next(iter(self.number_map[number]))  # Return the smallest index
        return -1
