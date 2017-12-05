
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def append(self, node):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def toLinkedList(self, arr):
        if not arr:
            raise Exception
        start = ListNode(arr.pop(0))
        head = start
        curr = head
        while arr:
            curr.next = ListNode(arr.pop(0))
            curr = curr.next
        self.head = head

    def printLL(self):
        temp = self.head
        while temp:
            print str(temp.val) + ' '
            temp = temp.next