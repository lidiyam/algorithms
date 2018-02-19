class Solution(object):
    def wordBreak(self, s, wordDict):
    	d = set(wordDict)
    	dp = [False]*(len(s)+1)
    	dp[0] = True

    	for i in range(1,len(s)+1):
    		for j in range(i):
				if s[j:i] in d and dp[j]:
					dp[i] = True
					break

    	return dp[len(s)]

if __name__ == '__main__':
	print Solution().wordBreak("leetcode", ["leet", "code"])
	print Solution().wordBreak("pokemon", ["poke", "kemon"])