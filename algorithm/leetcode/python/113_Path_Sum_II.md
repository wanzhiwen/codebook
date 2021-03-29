## 113. Path Sum II

### 信息卡片

- 时间：2021-03-29
- 题目链接：https://leetcode.com/problems/path-sum-ii/
- tag：`tree` `recursion`

### 题目描述

```
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
```

### 代码

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        # if the root is None
        if not root:
            return []
        elif not root.left and not root.right:# if the root is a leaf
            if root.val == targetSum:
                return [[targetSum]]
            else:
                return []
        else:        # if the root is not a leaf
            res = []
            if root.left:
                re = self.pathSum(root.left, targetSum - root.val)
                if len(re) != 0:
                    for i in range(len(re)):
                        tmp = [root.val]
                        tmp.extend(re[i])
                        res.append(tmp)
            if root.right:
                re = self.pathSum(root.right, targetSum - root.val)
                if len(re) != 0:
                    for i in range(len(re)):
                        tmp = [root.val]
                        tmp.extend(re[i])
                        res.append(tmp)
            return res
```