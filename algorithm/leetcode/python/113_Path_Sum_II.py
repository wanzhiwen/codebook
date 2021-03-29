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