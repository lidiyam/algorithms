import collections
import heapq

class Solution(object):
    
    def buildG(self, times, N, K):
        g = collections.defaultdict(set)
        weights = {}
        for u,v,w in times:
            weights[(u,v)] = w
            g[u].add(v)
            
        return g, weights
    
    def bfs(self, g, weights, times, K, N):
        visited = set()
        inf = float('inf')
        dist = [inf]*(N+1)
        
        times.append((0, K, 0))
        dist[K] = 0
        dist[0] = 0

        heap = [(0, (0, K))]
        heapq.heapify(heap)
        
        while heap:
            w, (u, v) = heapq.heappop(heap)
            dist[v] = min(dist[v], w)
            visited.add(v)
            for out in g[v]:
                if out not in visited:
                    heapq.heappush(heap,(weights[(v,out)]+w, (v, out)))

        return dist
                    
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]] - (u,v,w)
        :type N: int, type K: int
        :rtype: int - the longest min path
        """
        inf = float('inf')
        g, weights = self.buildG(times, N, K)
        received = self.bfs(g, weights, times, K, N)
        
        max_w = -1
        for w in received[1:]:
            if w == -1:
                return -1
            if w > max_w:
                max_w = w
        return max_w if max_w < inf else -1


if __name__ == '__main__':
    print Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) # == 2
    print Solution().networkDelayTime([[1,2,1],[2,1,3]], 2, 2)  # == 3
    print Solution().networkDelayTime([[1,2,1],[2,3,2], [1,3,2]], 3, 1) # == 2
    input1 = [
            [1,4,98],[1,5,54],[1,2,59],[1,3,86],
            [2,4,10],[2,3,61],[2,1,0],[2,5,89],
            [5,2,38],[5,1,34],[5,3,2],[5,4,44],
            [3,4,33],[3,2,64],[3,5,77],[3,1,79],
            [4,2,76],[4,3,46],[4,5,21],[4,1,95]]
    print Solution().networkDelayTime(input1, 5, 1) # == 69

