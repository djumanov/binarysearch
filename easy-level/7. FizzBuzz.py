class Solution:
    def solve(self, n):
        response = list()
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                response.append("FizzBuzz")
            elif i % 3 == 0:
                response.append("Fizz")
            elif i % 5 == 0:
                response.append("Buzz")
            else:
                response.append(str(i))
        return response