"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        
        return self.helper(root,result)
    
    def helper(self,node,result):
        if not node:
            return result
        self.helper(node.left,result)
        result.append(node.val)
        self.helper(node.right,result)
        return result

# submission better than 36% 

# iterative
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        queue = []
        current = root
        flag = 0
        
        while not flag:
            if current:
                queue.append(current)
                current = current.left
            else:
                if len(queue)>0:
                    current = queue.pop()
                    result.append(current.val)
                    current = current.right
                else:
                    flag = 1
            
            
            
        return result    