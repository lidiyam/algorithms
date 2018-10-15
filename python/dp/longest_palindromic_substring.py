class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        dp[i][j] = len of s[i:j] palindrome
        dp[i][j] = { dp[i+1][j-1] + 2 }
        """
        if len(s) == 0: return s
        s = ' ' + s
        dp = [[0]*(len(s)) for _ in range((len(s)))]
        for length in range(1, len(s)):
            for i in range(1, len(s)-length+1):
                j = i + length -1
                if i == j:
                    dp[i][j] = 1
                    continue
                if length == 2 and s[i] == s[j]:
                    dp[i][j] = 2
                elif dp[i+1][j-1] > 0 and s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = 0
                  
        max_substr = 0
        max_i, max_j = 0,0
        for i in range(1, len(s)):
            for j in range(1, len(s)):
                if max_substr < dp[i][j]:
                    max_substr = dp[i][j]
                    max_i, max_j = i, j
                
        return s[max_i:max_j+1]
