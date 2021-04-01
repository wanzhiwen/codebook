## 116. Populating Next Right Pointers in Each Node

### 信息卡片

- 时间：2021-04-01
- 题目链接：https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
- tag：`tree` `recursion` `BFS` `DFS`

### 题目描述

```
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL

Follow up:
	You may only use constant extra space.
	Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
	
Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Constraints:
The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
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
        if not root or not root.left:
            return root
        l = self.connect(root.left)
        r = self.connect(root.right)
        while l:
            l.next = r
            l = l.right
            r = r.left
        return root
```

### 优质代码

####代码1
```python
# recursion
# by https://leetcode.com/OldCodingFarmer/ 
class Solution(object):
    def connect(self, root):
        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root
```

####代码2

```python
#BFS
# by https://leetcode.com/OldCodingFarmer/
class Solution(object):    
    def connect(self, root):
        if not root:
            return 
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                queue.append(curr.left)
                queue.append(curr.right)
        return root
```

####代码3

```python
# DFS
# by https://leetcode.com/OldCodingFarmer/
class Solution(object):    
    def connect(self, root):
        if not root:
            return 
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                stack.append(curr.right)
                stack.append(curr.left)
        return root
```