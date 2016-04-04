"""Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        
        queue = []
        result = []
        queue.append(root)
        while queue:
            size = len(queue)
            for _ in xrange(size):
                node = queue.pop(0)
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        result.sort()
        if k>len(result):
            return null
        return result[k-1]

 # worst performance because of sort. Beats 3.2% of submissions

# slightly better. Beats 9.6% submissions
 class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        queue = []
        queue.append(root)
        result = []
        while queue:
            node = queue.pop()
            result.append(node.val)
            
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        
        result.sort()
        if k>len(result):
            return None
        return result[k-1]

 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        queue = []
        node = root
        while queue or node:
            if node:
                queue.append(node)
                node = node.left
            else:
                node = queue.pop()
                if k>1:
                    k-=1
                else:
                    return node.val
                node = node.right
                
# beats 85.68% submissions

