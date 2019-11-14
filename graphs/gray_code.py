# Leetcode
# 89. Gray Code

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0: return [0]
        num = "0"*n
        queue = [num]
        visited = set()
        ans = []
        while queue:
            node = queue.pop(-1)
            if node in visited:
                continue
            visited.add(node)
            ans.append(int(node,2))
            queue.extend(self.get_nbrs(node, n))

        return ans

    def get_nbrs(self, num, n):
        res = []
        for i in range(n):
            if num[i] == '1':
                res.append(num[:i]+'0'+num[i+1:])
            else:
                res.append(num[:i]+'1'+num[i+1:])
        return res
