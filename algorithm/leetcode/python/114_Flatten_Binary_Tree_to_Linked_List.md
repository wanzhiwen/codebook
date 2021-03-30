## 114. Flatten Binary Tree to Linked List

### 信息卡片

- 时间：2021-03-30
- 题目链接：https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
- tag：`tree` `recursion`

### 题目描述

```
Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
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
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        elif root.left and root.right:
            r = self.flatten(root.right)
            l = self.flatten(root.left)
            root.right = l
            t = l
            while t.right:
                t = t.right
            t.right = r
            root.left = None
        elif root.left and not root.right:
            l = self.flatten(root.left)
            root.right = l
            root.left = None
        elif not root.left and root.right:
            r = self.flatten(root.right)
        return root
```