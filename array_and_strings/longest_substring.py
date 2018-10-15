class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1: return len(s)
        i = 0
        j = 1
        n = len(s)
        seen = set(s[i])
        maxlen = 1
        curlen = 1
        while j < n:
            if s[i] == s[j]:
                i += 1
                j += 1
            elif s[j] in seen:
                maxlen = max(maxlen, curlen)
                curlen = 1
                i += 1
                j = i + 1
                seen = set(s[i])
            else:
                seen.add(s[j])
                j += 1
                curlen += 1
        return max(maxlen,curlen)

if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring("abcabcbb")
    print Solution().lengthOfLongestSubstring("ohvqnhjdml")
    print Solution().lengthOfLongestSubstring("pwwkew")
    print Solution().lengthOfLongestSubstring("abccccabbbbcbb")