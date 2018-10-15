from utils import ListNode, LinkedList

class Solution(object):
    def removeNthFromEnd(self, head, n):
        first, second = head, None
        count = 0
        while first:
            if count == n and not second:
                second = head
            elif count > n:
                second = second.next
            first = first.next
            count += 1
        if not second: return head.next
        second.next = second.next.next
        return head

if __name__ == '__main__':
    ll = LinkedList()
    ll.toLinkedList([1,2,3,4,5])
    res = Solution().removeNthFromEnd(ll.head, 2)
    resLL = LinkedList(res)
    resLL.printLL()