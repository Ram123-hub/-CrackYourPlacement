class TreeNode:
    def __init__(self, val = 0 , left = None ,right = None):
        self.val = val
        self.left =left
        self.right = right
    

def merge_trees(root1, root2):
    if not root1 and not root2:
        return None
    if not root1:
        return root2
    if not root2:
        return root1
    
    merged = TreeNode(root1.val + root2.val)
    merged.left = merge_trees(root1.left , root2.left)
    merged.right = merge_trees(root1.right, root2.right)

    return merged

from collections import deque
def print_trees(root):
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

merged_root = merge_trees(root1, root2)
print(print_trees(merged_root))  

root3 = TreeNode(1)
root4 = TreeNode(1)
root4.left = TreeNode(2)

merged_root2 = merge_trees(root3, root4)
print(print_trees(merged_root2)) 

