'''Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction (ie, buy one and
sell one share of the stock), design an algorithm to find the maximum profit.
Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
profit = 6-1 = 5.
Not 7-1 = 6, as selling price needs to be larger than buying price.
'''
import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_profit = sys.maxsize

        for i in range(0, len(prices), 1):
            if prices[i]<min_profit:
                min_profit = prices[i]
            else:
                max_profit = max(max_profit, prices[i]-min_profit)

        return max_profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print Solution().maxProfit(prices)
