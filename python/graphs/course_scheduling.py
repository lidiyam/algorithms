import collections

class Solution(object):

    # BFS to check for cycles
    def canFinish(self, numCourses, prereqs):
        # type numCourses: int, type prerequisites: List[List[int]]
        if numCourses == 0 or len(prereqs) == 0: return True       
        G = collections.defaultdict(set)
        indeg = [0]*numCourses
        
        for u in range(numCourses):
            G[u] = []
        for u,v in prereqs:
            G[v].append(u)
            indeg[u] += 1 
        
        q = []
        for u in range(numCourses):
            if indeg[u] == 0:
                q.append(u)
        
        while q:
            u = q.pop(0)
            for v in G[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
            del G[u]
              
        return len(G) == 0

    # DFS to check for cycles
    def findCycle(self, n, prereqs):
        if n == 0 or len(prereqs) == 0: return True
        G = collections.defaultdict(set)

        for u in range(n):
            G[u] = []
        for u,v in prereqs:
            G[v].append(u)

        visited = [False]*n
        completed = []

        def can_complete(i):
            if i in completed: # already checked
                return True
            elif visited[i] == True:  # found a cycle
                return False

            visited[i] = True
            for u in G[i]:
                if not can_complete(u):
                    return False

            completed.append(i)
            return True

        for i in range(n):
            if not can_complete(i):
                return False
        return True


if __name__ == '__main__':
    print Solution().canFinish(2, [[0,1],[1,0]])
    print Solution().findCycle(2, [[0,1],[1,0]])


