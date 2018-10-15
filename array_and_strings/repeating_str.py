class Solution(object):
    # repeat A ? times to get B
    def repeatedStringMatch(self, A, B):
        i, j = 0, 0
        res = 1
        while i < len(A) and j <= len(B):
            if j == len(B): 
                return -1
            if A[i] == B[j]:
                i += 1
                j += 1
                if i == len(A):
                    return res
                if j == len(B):
                    i = 0
                    res += 1
            else:
                j = 0
                i += 1
            
        return res

if __name__ == '__main__':
    print Solution().repeatedStringMatch("abcd","cdabcdab")
    print Solution().repeatedStringMatch("xyz","azyxy")
    print Solution().repeatedStringMatch("a","aa")
    print Solution().repeatedStringMatch("aaac", "aac")