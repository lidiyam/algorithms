
def coin_game(C):
	# C: c1, c2, ..., cN
	N = len(C)

	dp = [[0]*(N+1) for _ in range(N+1)]

	for i in range(N+1):
		dp[0][i] = 0
		dp[i][0] = 0

	C.insert(0,0)
	for i in range(N+1):
		dp[i][i] = C[i]

	total = [[0]*(N+1) for _ in range(N+1)]
	for i in range(1,N+1):
		for j in range(i,N+1):
			total[i][j] = total[i][j-1] + C[j]

	for length in range(2,N+1):
		for i in range(1, N+1-length+1):
			j = i + length - 1
			dp[i][j] = max(C[i] + total[i+1][j] - dp[i+1][j],
						   C[j] + total[i][j-1] - dp[i][j-1])

	return dp[1][N]



if __name__ == '__main__':
	print coin_game([2,4,5,1])