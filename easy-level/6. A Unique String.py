class Solution:
    def solve(self, s):
        st = list()
        for i in s:
            st.append(i)  
        return len(set(st)) == len(s)