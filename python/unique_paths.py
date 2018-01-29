class Solution(object):
    def uniquePaths(self, m, n):
        arr = [[0]*n for _ in range(m)]
        arr[0] = [1]*n
        for r in range(1,m):
            for c in range(n):
                total = 0
                if r > 0:
                    total += arr[r-1][c]
                if c > 0:
                    total += arr[r][c-1]
                arr[r][c] = total
        return arr[m-1][n-1]


if __name__ == '__main__':
    print Solution().uniquePaths(3,3)