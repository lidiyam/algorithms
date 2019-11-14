# Leetcode #20

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for c in s:
            if c in d.keys():
                stack.append(c)
            elif stack:
                top = stack.pop(-1)
                if d[top] != c:
                    return False
            else:
                return False
        return len(stack) == 0

