class Solution(object):
    def isInterleave(self, s1, s2, s3):
        
        m = len(s1)
        n = len(s2)
        # dp[i][j] = s1[0..i] and s2[0..j] are interleaving to s3[0..i+j]
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][0] = 1
        
        if len(s3) != m+n:
            return False
        
        s1 = ' ' + s1
        s2 = ' ' + s2
        s3 = ' ' + s3
        
        for i in range(1,m+1):
            dp[i][0] = dp[i-1][0] and s1[i] == s3[i]
            
        for j in range(1,n+1):
            dp[0][j] = dp[0][j-1] and s2[j] == s3[j]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (s1[i] == s3[i+j]) and (s2[j] == s3[i+j]):
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif (s1[i] == s3[i+j]):
                    dp[i][j] = dp[i-1][j]
                elif (s2[j] == s3[i+j]):
                    dp[i][j] = dp[i][j-1]
                    
        return True if dp[m][n] == 1 else False
