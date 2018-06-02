from utils import ListNode, LinkedList

class Solution(object):
    def length(self, lst):
        curr, size = lst, 0
        while curr:
            size += 1
            curr = curr.next
        return size
    
    def pad(self, lst, res_len):
        curr, size = lst, 1
        while curr.next:
            size += 1
            curr = curr.next
        while size < res_len:
            curr.next = ListNode(0)
            curr = curr.next
            size += 1
        return lst

    def addTwoNumbers(self, l1, l2):
        l1_len = self.length(l1)
        l2_len = self.length(l2)
        res_len = max(l1_len, l2_len)
        if l1_len < res_len:
            l1 = self.pad(l1, res_len)
        if l2_len < res_len:
            l2 = self.pad(l2, res_len)
        
        res, over = ListNode(0), 0
        curr = res
        while l2:
            nxt_val = l1.val + l2.val + over
            over, nxt_val = nxt_val / 10, nxt_val % 10
            curr.next = ListNode(nxt_val)
            curr = curr.next
            l1, l2 = l1.next, l2.next
            
        if over > 0:
            curr.next = ListNode(over)
        return res.next if res.next else None


if __name__ == '__main__':
    # l1 = 2 -> 4 -> 3
    # l2 = 5 -> 6 -> 4
    # ans = 7 -> 0 -> 8
    l1 = LinkedList()
    l1.toLinkedList([2,4,3])
    l2 = LinkedList()
    l2.toLinkedList([5,6,4])

    l1.toLinkedList([3,4])
    l2.toLinkedList([8,6,0,0,5])
    resNode = Solution().addTwoNumbers(l1.head, l2.head)
    res = LinkedList(resNode)
    res.printLL()

    l1.toLinkedList([1,8])
    l2.toLinkedList([0])
    resNode = Solution().addTwoNumbers(l1.head, l2.head)
    res = LinkedList(resNode)
    res.printLL()
