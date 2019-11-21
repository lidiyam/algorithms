# 841. Keys and Rooms

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        N = len(rooms)
        visited = set()
        def dfs(node):
            visited.add(node)
            if len(visited) == N:
                return True
            for nei in rooms[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True
            return False

        return dfs(0)
