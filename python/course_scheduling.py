class Solution(object):
    def canFinish(self, numCourses, prereqs):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
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