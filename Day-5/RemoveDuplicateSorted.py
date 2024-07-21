# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

def deleteDuplicates(head:ListNode)->ListNode:
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

def create_linked_list(vals):
    if not vals:
        return None
    
    head =ListNode(vals[0])
    current = head
    for val in vals[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    vals = []
    current = head
    while current:
        vals.append(current.val)
        current = current.next
    print(vals)


# Test case 1
head = create_linked_list([1, 1, 2])
head = deleteDuplicates(head)
print_linked_list(head) 

# Test case 2
head = create_linked_list([1, 1, 2, 3, 3])
head = deleteDuplicates(head)
print_linked_list(head)  



        