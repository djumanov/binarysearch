# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        if node is None:
            return 0
        l = 0
        while node is not None:
            l += 1
            node = node.next
        return l