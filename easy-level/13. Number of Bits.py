class Solution:
    def solve(self, n):
        c = 0
        while n != 0:
            if n % 2 != 0:
                c += 1
            n //= 2
        return c