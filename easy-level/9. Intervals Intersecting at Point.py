class Solution:
    def solve(self, intervals, point):
        counter = 0
        for interval in intervals:
            if point >= interval[0] and point <= interval[-1]:
                counter += 1
        return counter