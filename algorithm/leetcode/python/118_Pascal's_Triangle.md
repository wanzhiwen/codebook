## 118. Pascal's Triangle

### 信息卡片

- 时间：2021-04-04
- 题目链接：https://leetcode.com/problems/pascals-triangle/
- tag：

### 题目描述

```
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
 
Constraints:
1 <= numRows <= 30
```

### 代码

```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            tmp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(res[i - 1][j] + res[i - 1][j - 1])
            res.append(tmp)
        return res
```
