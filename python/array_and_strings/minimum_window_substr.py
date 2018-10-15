class Solution(object):
    def minWindow(self, s, t):
        tmap = {}
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            tmap[c] = 1

        i = 0
        j = 0
        d = float('inf')
        counter = len(s)
        head = 0
        while j < len(s):
            if tmap[s[j]] > 0:
                tmap[s[j]] -= 1
                j += 1
                counter -= 1
            while counter == 0:
                if (j - i) < d:
                    d = j - i
                    head = i
                if tmap[s[i]] == 0:
                    tmap[s[i]] += 1
                    i += 1
                    counter += 1
        return s[i:d] if d != float('inf') else ""

                

if __name__ == '__main__':
    print Solution().minWindow("ADOBECODEBANC", "ABC")
