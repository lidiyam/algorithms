# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        nestedList.reverse()
        self.stack = nestedList
        self.next_int = -1
        
        
    def next(self):
        return self.next_int
          
        
    def hasNext(self):
        if not self.stack:
            return False
        nested = self.stack.pop(-1)
        if nested.isInteger():
            self.next_int = nested.getInteger()
            return True
        else:
            lst = nested.getList()
            lst.reverse()
            for x in lst:
                self.stack.append(x)
            return self.hasNext()


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
