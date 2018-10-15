"""
e.g. cycle:

1 -> 2 -> 3 -> 4
     ^         |
     |_________|
"""

from python.utils import ListNode


class Solution(object):

    # Uses extra space
    def contains_cycle(self, lst):
        if not lst:
            return False
        visited = set()
        temp = lst

        while temp:
            if temp.val in visited:
                return True
            visited.add(temp.val)
            temp = temp.next
        return False

    def contains_cycle_floyd(self, lst):
        if not lst:
            return False
        slow = lst
        fast = lst.next

        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next

        return False


if __name__ == '__main__':
    linked_list = ListNode(1)
    linked_list.next = ListNode(2)
    linked_list.next.next = ListNode(3)
    linked_list.next.next.next = ListNode(4)
    linked_list.next.next.next.next = linked_list.next

    print Solution().contains_cycle(linked_list)
    print Solution().contains_cycle_floyd(linked_list)
