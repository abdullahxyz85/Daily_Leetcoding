class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_count = {}
        
        for candy in candyType:
            if candy not in candy_count:
                candy_count[candy] = 1
            else:
                candy_count[candy] += 1
        
        uniqueCandies = len(candy_count)
        
        maxAllowed = len(candyType) // 2
        
        if uniqueCandies < maxAllowed:
            return uniqueCandies
        else:
            return maxAllowed

            
# def maxCandies(candyType):
# uniqueCandies = len(set(candyType))
# maxAllowed = len(candyType) // 2
# return min(uniqueCandies, maxAllowed)

