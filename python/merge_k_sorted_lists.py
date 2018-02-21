import heapq
from utils import ListNode

class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        res = ListNode(0)
        tail = res
                
        heap = []
        heapq.heapify(heap)
        
        for indx in range(k):
            if not lists[indx]: continue
            node = lists[indx]
            heapq.heappush(heap, (node.val, indx))
            lists[indx] = node.next

        while heap:                
            item, indx = heapq.heappop(heap)
            tail.next = ListNode(item)
            tail = tail.next
            if lists[indx]:
                heapq.heappush(heap, (lists[indx].val, indx))
                lists[indx] = lists[indx].next
            
        return res.next
    
    def merge_k_lists(self, lists):
        """
        :type lists: List[List[Int]]
        :rtype: List[Int]
        """
        k = len(lists)
        length = 0
        for i, lst in enumerate(lists):
            if not lst: continue
            length += len(lst)
        res = [0]*length
                
        heap = []
        heapq.heapify(heap)
        indices = list(range(k))
    
        for i in range(length):  
            while indices:
                indx = indices.pop(0)
                if not lists[indx]: continue
                item = lists[indx].pop(0)
                heapq.heappush(heap, (item,indx)) 
                
            item, indx = heapq.heappop(heap)
            res[i] = item
            indices.append(indx)
            
        return res


if __name__ == '__main__':
    print Solution().merge_k_lists([[2,7],[1,3,4],[6,8]])