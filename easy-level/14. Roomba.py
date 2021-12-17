class Solution:
    def solve(self, moves, x, y):
        currX, currY = 0, 0
        d = {
            "EAST": (1, 0),
            "WEST": (-1, 0),
            "NORTH": (0, 1),
            "SOUTH": (0, -1),
        }
        for i in moves:
            dX, dY = d[i]
            currX += dX
            currY += dY
        if currX == x and currY == y:
            return True
        return False