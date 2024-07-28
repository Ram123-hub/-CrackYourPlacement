class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def removeElements(self, head: Node, val: int) -> Node:
        # Create a dummy node that points to the head of the list
        dummy = Node(next=head)
        current = dummy
        
        # Traverse the list
        while current.next:
            if current.next.data == val:
                # Remove the node by skipping it
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        # Return the new head of the list
        return dummy.next

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
    
    
    head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
    

    new_head = S.removeElements(head, 6)
    
    print_linked_list(new_head)  
