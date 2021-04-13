## 123. Best Time to Buy and Sell Stock III

### 信息卡片

- 时间：2021-04-12
- 题目链接：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
- tag：`dp`

### 题目描述

```
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Example 4:
Input: prices = [1]
Output: 0
 
Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^5
```

### 代码

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0
        dp = [[0]*length for _ in range(3)]
        for k in range(1, 3):
            t=prices[0]
            for i in range(1, length):
                t = min(t, prices[i] - dp[k-1][i - 1])
                dp[k][i] = max(dp[k][i-1], prices[i]-t)
        return dp[2][length-1]
```
