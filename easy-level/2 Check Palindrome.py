class Solution:
    def solve(self, s):
        if len(s) < 0:
            return False
        return s == s[-1::-1]