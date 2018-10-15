class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            max_profit = max(max_profit, price - min_price)
        return max_profit

if __name__ == '__main__':
    arr = [2,1,2,1,0,1,2]
    print Solution().maxProfit(arr)