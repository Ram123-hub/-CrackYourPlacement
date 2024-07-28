class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    MOD = 10**9 + 7
    
    def multiplyTwoLists(self, l1: ListNode, l2: ListNode) -> int:
        # Helper function to convert linked list to integer
        def linked_list_to_int(node: ListNode) -> int:
            num = 0
            while node:
                num = num * 10 + node.val
                node = node.next
            return num
        
        # Convert both linked lists to integers
        num1 = linked_list_to_int(l1)
        num2 = linked_list_to_int(l2)
        
        # Multiply and take modulo
        result = (num1 * num2) % self.MOD
        
        return result

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Test the function
S = Solution()
l1 = create_linked_list([3, 2])  # Represents 32
l2 = create_linked_list([2])     # Represents 2
print(S.multiplyTwoLists(l1, l2))  # Output: 64

l1 = create_linked_list([1, 0, 0])  # Represents 100
l2 = create_linked_list([1, 0])    # Represents 10
print(S.multiplyTwoLists(l1, l2))  # Output: 1000
