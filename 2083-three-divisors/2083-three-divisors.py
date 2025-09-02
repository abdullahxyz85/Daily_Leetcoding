class Solution:
    def isThree(self, n: int) -> bool:
        root = int(n ** 0.5)
        
        if root * root != n:
            return False
        
        if root < 2:
            return False
        for i in range(2, root):
            if root % i == 0:
                return False
        
        return True
