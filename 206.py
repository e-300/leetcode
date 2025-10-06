# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        prev_node = None

        current_node = head

        while current_node:

            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node
    
    def recursiveList(self, head: ListNode) -> ListNode:


        # empty list
        if head is None:
            return None  
        
        # single node - BASE CASE!
        if head.next is None:
            return head  

        newhead = self.recursiveList(head.next)

        head.next.next = head

        head.next = None

        return newhead

        



        







        
            







    
        

# Helper function to create linked list from array
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to array
def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.recursiveList(head1)
    print(f"Test 1: {linked_list_to_array(result1)}")  # Expected: [5, 4, 3, 2, 1]
    
    # Test case 2
    head2 = create_linked_list([1, 2])
    result2 = solution.recursiveList(head2)
    print(f"Test 2: {linked_list_to_array(result2)}")  # Expected: [2, 1]
    
    # Test case 3
    head3 = create_linked_list([])
    result3 = solution.recursiveList(head3)
    print(f"Test 3: {linked_list_to_array(result3)}")  # Expected: []