## 116. Populating Next Right Pointers in Each Node

### 信息卡片

- 时间：2021-04-03
- 题目链接：https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
- tag：`tree`  `DFS`

### 题目描述

```
Given a binary tree
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Constraints:
The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
```

### 代码

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        stack = [root]
        count1 = 1
        count2 = 0
        tmp = []
        while stack:
            curr = stack.pop(0)
            count1 = count1 - 1
            if curr.left:
                stack.append(curr.left)
                tmp.append(curr.left)
                count2 = count2 + 1
            if curr.right:
                stack.append(curr.right)
                tmp.append(curr.right)
                count2 = count2 + 1
            if count1 == 0:
                if count2 > 1:
                    for i in range(count2 -1):
                        tmp[i].next = tmp[i + 1]
                count1 = count2
                count2 = 0
                tmp = []
        return root
```