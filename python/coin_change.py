import sys

class Solution(object):
    def coinChange_greedy(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = sorted(coins)
        count = 0
        i = len(coins) - 1
        while i >= 0:
            max_coin = coins[i]
            count += amount / max_coin
            amount = amount % max_coin
            i -= 1
        if amount == 0:
            return count
        else: 
            return -1
    """
    def coinChange2(self, coins, amount):
        if amount == 0: return 0
        coins.sort()
        coins.insert(0,0)
        n = len(coins)
        T = [[0]*(amount+1) for _ in range(n)]

        for i, coin in enumerate(coins):
            for amt in range(1,amount+1):
                if i == 0 or amt == 0: continue
                count = amt / coin
                left = amt % coin
                if left != 0 and T[i][left] == 0:
                    T[i][amt] = T[i-1][amt]
                else:
                    if T[i-1][amt] == 0:
                        T[i][amt] = count + T[i][left] 
                    else:
                        T[i][amt] = min(count + T[i][left], T[i-1][amt])
        # res = T[n-1][amount]
        return -1 if T[n-1][amount] == 0 else T[n-1][amount]
    """

    # Time Limit exceeded
    def coinChange_dp(self, coins, amount):
        if amount <= 0 or len(coins) == 0: return 0
        coins.insert(0,0)
        n = len(coins)
        T = [[float('inf') for _ in range(amount + 1)] for i in range(n)]
        
        for i in range(n):
            for amt in range(amount + 1):
                if i == 0 or amt == 0: continue
                if amt == coins[i]:
                    T[i][amt] = 1
                if coins[i] <= amt:
                    T[i][amt] = min( T[i][amt], T[i - 1][amt], T[i][amt - coins[i]] + 1)
                else:
                    T[i][amt] = T[i - 1][amt]

        return -1 if T[n-1][amount] == float('inf') else T[n-1][amt]

    def coinChange(self, coins, amount):
        if amount <= 0 or len(coins) == 0: return 0
        T = [(amount+1) for _ in range(amount + 1)]
        T[0] = 0

        for i in range(amount+1):
            for coin in coins:
                if coin <= i:
                    T[i] = min(T[i], T[i-coin] + 1)
        return -1 if T[amount] > amount else T[amount]


if __name__ == "__main__":
    print Solution().coinChange([1,2,5], 11) # == 3
    print Solution().coinChange([4,2,5], 7) # == 2
    print Solution().coinChange([2], 1) # == -1
    print Solution().coinChange([2,5,9], 45) # == 5
    print Solution().coinChange([1,4,6], 8) # == 2
    print Solution().coinChange([3,8], 9)
    print Solution().coinChange([1,5,6,8], 11)
    print Solution().coinChange([7,2,3,6], 13)
    print Solution().coinChange([83,186,408,419], 6249)
    print Solution().coinChange([186,419,83,408], 6249) # == 20?
