## 115. Distinct Subsequences

### 信息卡片

- 时间：2021-03-31
- 题目链接：https://leetcode.com/problems/distinct-subsequences/
- tag：`string` `dynamic programming`

### 题目描述

```
Given two strings s and t, return the number of distinct subsequences of s which equals t.
A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).
It is guaranteed the answer fits on a 32-bit signed integer.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
(r)(a)(b)(b)b(i)(t)
(r)(a)(b)b(b)(i)(t)
(r)(a)b(b)(b)(i)(t)

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
(b)(a)b(g)bag
(b)(a)bgba(g)
(b)abgb(a)(g)
ba(b)gb(a)(g)
babg(b)(a)(g)

Constraints:
1 <= s.length, t.length <= 1000
s and t consist of English letters.
```

### 代码

```python
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_len = len(s) + 1
        t_len = len(t) + 1
        dp = [[1]*t_len for _ in range(s_len)]
        for i in range(1, t_len):
            dp[0][i] = 0
        for i in range(1, s_len):
            for j in range(1, t_len):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] #core
                else:
                    dp[i][j] = dp[i -1][j]
        return dp[s_len - 1][t_len - 1]
```