# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

# Example 1:


# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
# Example 2:


# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 2 * 104].
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# All Node.val are unique


class TreeNode:
    def __init__(self, val = 0 , left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def range_sum_bst(root, low , high):
    def dfs(node):
        if not node:
            return 0 
        
        if node.val <low:
            return dfs(node.right)
        elif node.val > high:
            return dfs(node.left)
        else:
            return node.val + dfs(node.left) + dfs(node.right)
    return dfs(root)

root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(15)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(7)
root1.right.right = TreeNode(18)

low1, high1 = 7, 15
print(range_sum_bst(root1, low1, high1))  
root2 = TreeNode(10)
root2.left = TreeNode(5)
root2.right = TreeNode(15)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(13)
root2.right.right = TreeNode(18)
root2.left.left.left = TreeNode(1)
root2.left.right.left = TreeNode(6)

low2, high2 = 6, 10
print(range_sum_bst(root2, low2, high2))  
