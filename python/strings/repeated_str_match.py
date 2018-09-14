class Solution(object):
    # repeat A ? times to get B
    def repeatedStringMatch(self, A, B):
        s = ""
        res = 0
        while len(s) < len(B)+2*len(A):
            s += A
            res += 1
            if B in s:
                return res
        return -1

if __name__ == '__main__':
    A="abcd"
    B="cdabcdab"
    # A="a"
    # B="aa"
    print(Solution().repeatedStringMatch(A, B))