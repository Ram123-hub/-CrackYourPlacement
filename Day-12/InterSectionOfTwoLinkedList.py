class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: Node, headB: Node) -> Node:
        if not headA or not headB:
            return None
        
        # Initialize two pointers
        ptrA, ptrB = headA, headB
        
        # Traverse both lists
        while ptrA != ptrB:
            # Move to next node or switch to other list
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA
        
        # Either both are None (no intersection) or both point to the intersection node
        return ptrA

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = Node()
    current = dummy
    for val in values:
        current.next = Node(data=val)
        current = current.next
    return dummy.next

# Helper function to find the intersection node given two lists
def find_intersection(headA: Node, headB: Node, skipA: int, skipB: int) -> Node:
    # Advance headA by skipA
    for _ in range(skipA):
        headA = headA.next
    
    # Advance headB by skipB
    for _ in range(skipB):
        headB = headB.next
    
    # Return the intersection node
    return Solution().getIntersectionNode(headA, headB)

# Example usage
if __name__ == "__main__":
    # Creating intersection node
    intersect_node = create_linked_list([8, 4, 5])

    # Creating list A
    listA = create_linked_list([4, 1])
    listA_end = listA
    while listA_end.next:
        listA_end = listA_end.next
    listA_end.next = intersect_node  # Adding intersection

    # Creating list B
    listB = create_linked_list([5, 6, 1])
    listB_end = listB
    while listB_end.next:
        listB_end = listB_end.next
    listB_end.next = intersect_node  # Adding intersection

    # Finding intersection
    intersection = find_intersection(listA, listB, 2, 3)
    print(intersection.data if intersection else "No intersection")  # Output: 8
