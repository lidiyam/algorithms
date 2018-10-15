class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        hashset = {}
        i = 0
        head = Node('')
        prev = head
        while i < len(words):
            word = words[i]
            if len(word) == 0:
                i += 1
                continue
            curr = Node(word[0])
            hashset[word[0]] = curr
            words[i] = word[i:]
            if prev.val != curr.val:
                if prev.next != None: return ""
                prev.next = curr
                prev = curr
            i += 1
        res = ""
        c = head
        while c:
            res += c.val
            c = c.next
        return res

if __name__ == '__main__':
    print(Solution().alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"]))
"""
t>f
w>e>r
r>t
"""