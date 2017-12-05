from python.utils import LinkedList, ListNode


class Solution(object):

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next and head.next.next:
            odd_tail = head
            even = head.next
            even_tail = head.next
            curr = head.next.next
        else:
            return head

        while curr:
            even_tail.next = curr.next
            curr.next = even
            odd_tail.next = curr
            odd_tail = curr
            even_tail = even_tail.next
            if even_tail and even_tail.next:
                curr = even_tail.next
            else:
                break

        return head

if __name__ == '__main__':
    input_lst = LinkedList()
    input_lst.toLinkedList([1,2,3,4,5,6,7,8])
    result = Solution().oddEvenList(input_lst.head)
    result = LinkedList(result)
    result.printLL()