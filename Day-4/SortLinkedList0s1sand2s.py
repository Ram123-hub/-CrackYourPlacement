
# Sort a linked list of 0s, 1s and 2s
# Last Updated : 20 Mar, 2023
# Given a linked list of 0s, 1s and 2s, The task is to sort and print it.

# Examples: 

# Input: 1 -> 1 -> 2 -> 0 -> 2 -> 0 -> 1 -> NULL 
# Output: 0 -> 0 -> 1 -> 1 -> 1 -> 2 -> 2 -> NULL

# Input: 1 -> 1 -> 2 -> 1 -> 0 -> NULL 
# Output: 0 -> 1 -> 1 -> 1 -> 2 -> NULL 

class ListNode:
    def __init__(self, value=0,next=None):
        self.value = value
        self.next = next
    
def print_list(head):
    while head:
        print(head.value, end="->")
        head = head.next
    print("Null")
    
def sort_linked_list(head):
    if not head:
        return None
    
    low, mid, high = ListNode(0), ListNode(0), ListNode(0)
    low_curr, mid_curr, high_curr = low, mid, high
    
 
    curr = head
    while curr:
        if curr.value == 0:
            low_curr.next = curr
            low_curr = low_curr.next
        elif curr.value == 1:
            mid_curr.next = curr
            mid_curr = mid_curr.next
        else:
            high_curr.next = curr
            high_curr = high_curr.next
        curr = curr.next
    
    
    low_curr.next = None
    mid_curr.next = None
    high_curr.next = None
    
   
    if mid.next:
        low_curr.next = mid.next
        mid_curr.next = high.next
    else:
        low_curr.next = high.next

 
    return low.next


head = ListNode(1, ListNode(1, ListNode(2, ListNode(0, ListNode(2, ListNode(0, ListNode(1)))))))
print("Original list:")
print_list(head)

sorted_head = sort_linked_list(head)
print("Sorted list:")
print_list(sorted_head)