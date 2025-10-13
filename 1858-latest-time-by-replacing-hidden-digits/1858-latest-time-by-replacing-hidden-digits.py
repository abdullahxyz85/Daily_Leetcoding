class Solution:
    def maximumTime(self, time: str) -> str:
        t = list(time)
        if t[0] == '?':
            if t[1] == '?' or t[1] <= '3':
                t[0] = '2'
            else:
                t[0] = '1'
        if t[1] == '?':
            if t[0] == '2':
                t[1] = '3'
            else:
                t[1] = '9'
        if t[3] == '?':
            t[3] = '5'
        if t[4] == '?':
            t[4] = '9'
        return "".join(t)