class Solution:
    def repeatedCharacter(self, s: str) -> str:

       empty_set = set()
       for i in s:
        if i in empty_set:
            return i

        empty_set.add(i)
        