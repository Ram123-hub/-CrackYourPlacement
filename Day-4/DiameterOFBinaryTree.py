# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 
# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100


from typing import Optional

class TreeNode:
    def __init__(self,val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node:Optional[TreeNode])->int:

            if not node:
                return 0
            
            left_depth = dfs(node.left)
            right_depth= dfs(node.right)

            self.diameter = max(self.diameter,left_depth+right_depth)

            return max(left_depth,right_depth)+1
        
        dfs(root)
        return self.diameter
    

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

# Build the tree structure
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

# Initialize Solution and compute the diameter
solution = Solution()
print(solution.diameterOfBinaryTree(node1)) 

node1 = TreeNode(1)
node2 = TreeNode(2)

node1.left = node2

solution = Solution()
print(solution.diameterOfBinaryTree(node1))  