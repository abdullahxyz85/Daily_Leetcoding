class Solution:
    def repeatedCharacter(self, s: str) -> str:
        empty_set = []
        for i in s:
            found = False
            for char in empty_set:
                if char == i:
                    found = True
                    break
            if found:
                return i
            empty_set.append(i)
        