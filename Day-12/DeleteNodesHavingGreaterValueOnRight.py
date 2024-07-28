# Delete nodes having greater value on right
# Difficulty: EasyAccuracy: 35.51%Submissions: 139K+Points: 2
# Given a singly linked list, remove all the nodes in the list which have any node on their right whose value is greater. (Not just immediate Right , but entire List on the Right)

# Example 1:

# Input:
# LinkedList = 12->15->10->11->5->6->2->3
# Output: 15 11 6 3
# Explanation: Since, 12, 10, 5 and 2 are
# the elements which have greater elements
# on the following nodes. So, after deleting
# them, the linked list would like be 15,
# 11, 6, 3.
# Example 2:

# Input:
# LinkedList = 10->20->30->40->50->60
# Output: 60
# Explanation: All the nodes except the last
# node has a greater value node on its right,
# so all the nodes except the last node must
# be removed.
# Your Task:
# The task is to complete the function compute() which should modify the list as required and return the head of the modified linked list. 
# The printing is done by the driver code,

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 ≤ size of linked list ≤ 105
# 1 ≤ element of linked list ≤ 105

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def compute(self, head: Node) -> Node:
        # Helper function to reverse the linked list
        def reverse_list(head: Node) -> Node:
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        # Reverse the list
        head = reverse_list(head)
        
        # Traverse the reversed list and remove nodes with smaller value than max so far
        max_value = float('-inf')
        dummy = Node()
        dummy.next = head
        current = dummy
        
        while current and current.next:
            if current.next.data >= max_value:
                max_value = current.next.data
                current = current.next
            else:
                current.next = current.next.next
        
        # Reverse the list again to restore original order
        head = reverse_list(dummy.next)
        
        return head

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = Node()
    current = dummy
    for val in values:
        current.next = Node(data=val)
        current = current.next
    return dummy.next

# Helper function to print the linked list
def print_linked_list(head: Node):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()

# Example usage
if __name__ == "__main__":
    S = Solution()
    
    
    head = create_linked_list([12, 15, 10, 11, 5, 6, 2, 3])
    
    
    new_head = S.compute(head)
    
    
    print_linked_list(new_head) 
