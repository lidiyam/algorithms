def maxSaving(N, M, p, p1):
    dp = [[0]*(M+1) for _ in range(N+1)]

    p.insert(0,0)
    p1.insert(0,0)
    v = [p1[i]-p[i] for i in range(N+1)]

    for i in range(N+1):
        for j in range(M+1):
            if i == 0 or j == 0: 
                continue
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            if p[i] <= j:
                dp[i][j] = max(v[i] + dp[i][j-p[i]], dp[i][j])
    return dp[N][M]


if __name__ == '__main__':
    print maxSaving(4,5,[1,2,3,1],[1,3,5,4])
