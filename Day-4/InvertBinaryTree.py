# 226. Invert Binary Tree
# Easy
# Topics
# Companies
# Given the root of a binary tree, invert the tree, and return its root.

 

# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100



from typing import Optional

class TreeNode:
    def __init__(self, val = 0 , left = None , right= None):
        self.val = val
        self.left = left
        self.right= right



class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        # Swap the left and right subtrees
        root.left, root.right = root.right, root.left
        
        # Recursively invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root  
      
from collections import deque

def print_tree(root: TreeNode) -> None:
    if not root:
        print("[]")
        return
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    print(result)

# Example 1
# Create the binary tree: [4,2,7,1,3,6,9]
node1 = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(6)
node4 = TreeNode(9)
node5 = TreeNode(2)
node6 = TreeNode(7)
root1 = TreeNode(4, left=node5, right=node6)
node5.left = node1
node5.right = node2
node6.left = node3
node6.right = node4

solution = Solution()
inverted_root1 = solution.invertTree(root1)
print("Inverted Tree 1:", end=" ")
print_tree(inverted_root1)  # Expected Output: [4, 7, 2, 9, 6, 3, 1]

# Example 2
# Create the binary tree: [2,1,3]
node1 = TreeNode(1)
node2 = TreeNode(3)
root2 = TreeNode(2, left=node1, right=node2)

solution = Solution()
inverted_root2 = solution.invertTree(root2)
print("Inverted Tree 2:", end=" ")
print_tree(inverted_root2)  # Expected Output: [2, 3, 1]

# Example 3
# Create an empty binary tree
root3 = None

solution = Solution()
inverted_root3 = solution.invertTree(root3)
print("Inverted Tree 3:", end=" ")
print_tree(inverted_root3)  # Expected Output: []
