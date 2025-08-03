class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]

        for i in range(len(encoded)):
            previous_number = arr[i]

            next_number = previous_number ^ encoded[i]

            arr.append(next_number)

        return arr