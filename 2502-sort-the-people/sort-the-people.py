class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        
        indexes = []
        for i in range(n):
            indexes.append(i)
        
        for i in range(n):
            for j in range(i + 1, n):
                if heights[indexes[i]] < heights[indexes[j]]:
                    indexes[i], indexes[j] = indexes[j], indexes[i]
        
        sorted_names = []
        for i in range(n):
            sorted_names.append(names[indexes[i]])
        
        return sorted_names