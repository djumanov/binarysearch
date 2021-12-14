class Solution:
    def solve(self, n):
        if n > 0: return sum([i for i in range(1, n*2, 2)])
        else: return 0