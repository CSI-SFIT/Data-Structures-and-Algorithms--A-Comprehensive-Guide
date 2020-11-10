#Problem link-> https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#Leetcode Problem 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(prices):
        profit = 0
        buy = 0
        sell = 0

        for i in range(len(prices)-1):
          if prices[i+1] - prices[i] >=0:
                buy = prices[i]
                sell = prices[i+1]
                profit += sell -buy
        return profit

    # test the code
    if __name__ == "__main__":
        print(maxProfit([7,1,5,6,4]))