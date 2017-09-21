
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
    def __init__(self):
        self.head = None

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
        while arr:
            head.next = ListNode(arr.pop(0))
            head = head.next
        self.head = start

    def printLL(self):
        temp = self.head
        while temp:
            print str(temp.val) + ' '
            temp = temp.next