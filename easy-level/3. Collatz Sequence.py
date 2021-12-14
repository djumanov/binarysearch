class Solution:
    def solve(self, n):
        condition = True
        count = 1
        while condition:
            if n == 1:
                break
            elif n%2 == 0:
                n //= 2
            else:
                n = n*3+1
            count += 1
        return count