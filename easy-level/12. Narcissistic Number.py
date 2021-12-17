class Solution:
    def solve(self, n):
        s = 0
        l = len(str(n))
        x = n
        while n != 0:
            s += pow(n%10, l)
            n //= 10
        return s == x