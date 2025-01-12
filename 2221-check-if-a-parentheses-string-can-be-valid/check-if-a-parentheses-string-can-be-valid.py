class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False  # Odd length strings can't be valid
        
        # Check left-to-right balance
        open_balance, free_slots = 0, 0
        for i in range(n):
            if locked[i] == '0':
                free_slots += 1
            elif s[i] == '(':
                open_balance += 1
            else:  # s[i] == ')'
                open_balance -= 1
            
            # If there are more ')' than '(' including free slots, invalid
            if open_balance + free_slots < 0:
                return False
        
        # Check right-to-left balance
        close_balance, free_slots = 0, 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '0':
                free_slots += 1
            elif s[i] == ')':
                close_balance += 1
            else:  # s[i] == '('
                close_balance -= 1
            
            # If there are more '(' than ')' including free slots, invalid
            if close_balance + free_slots < 0:
                return False
        
        return True
