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
