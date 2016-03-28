"""Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

Tree
"""

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        tmp = root.left
        root.left = root.right
        root.right =tmp
        
        return root
# beats 9.8 % of python submissions


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return
        
        res = TreeNode(root.val)
        if root.right:
            res.left = self.invertTree(root.right)
        else:
            res.left = None
        if root.left:
            res.right = self.invertTree(root.left)
        else:
            res.right = None
        
        return res
# beats 35.07 % submissions