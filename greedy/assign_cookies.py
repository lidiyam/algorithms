# 455. Assign Cookies

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        n, m = len(g), len(s)
        if n == 0 or m == 0: return 0
        res = 0
        s.sort()
        g.sort()
        i, j = 0, 0
        while i < n and j < m:
            if g[i] <= s[j]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        return res
