# Leetcode
# 547. Friend Circles

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = set()
        ans = 0
        for i, friends in enumerate(M):
            if i not in visited:
                ans += 1
                visited.add(i)
                self.visit(i, visited, M)
        return ans
    
    def visit(self, i, visited, M):
        for j in range(len(M)):
            if M[i][j] == 1 and j not in visited:
                visited.add(j)
                self.visit(j, visited, M)
