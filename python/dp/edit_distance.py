class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        # dp[i][j] = edit distance between word1[0..i] and word2[0..j]
        dp = [[0]*(n+1) for _ in range(m+1)]

        # source can be transformed into target prefix by inserting  
        # all of the characters in the prefix  
        for i in range(1, n+1):
            dp[0][i] = i
 
        # source prefixes can be transformed into empty string by  
        # by deleting all of the characters  
        for i in range(1, m+1):
            dp[i][0] = i
        
        word1 = ' ' + word1
        word2 = ' ' + word2
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # min(delete, insert, replace)
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)
        return dp[m][n]


if __name__ == '__main__':
    print Solution().minDistance("sitting", "kitten")