## 120. Triangle

### 信息卡片

- 时间：2021-04-05
- 题目链接：https://leetcode.com/problems/triangle/
- tag：`dynamic programming`

### 题目描述

```
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10

Constraints:
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-10^4 <= triangle[i][j] <= 10^4
```

### 代码

```python
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        depth = len(triangle)
        for i in range(depth):
            for j in range(depth - i):
                if i != 0:
                    m = min(triangle[depth - i][j], triangle[depth - i][j + 1])
                    triangle[depth - i - 1][j] = triangle[depth - i - 1][j] + m
        return triangle[0][0]
```
