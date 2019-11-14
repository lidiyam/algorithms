 # Leetcode #678

 class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # diff = count of '(' minus count of ')'
        # min_diff = min possible diff
        # max_diff = max possible diff
        min_diff = max_diff = 0
        for c in s:
            if c == '(' or c == '*':
                max_diff += 1
            else:
                max_diff -= 1
            if c == ')' or c == '*':
                min_diff -= 1
            else:
                min_diff += 1
            if max_diff < 0: return False
            min_diff = max(0, min_diff)

        return min_diff == 0

