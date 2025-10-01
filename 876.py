# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head

        while fast and fast.next:

            slow = slow.next 
            fast = fast.next.next
        
        return slow 










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

# Helper function to convert linked list to array for easy comparison
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
    
    # Test case 1: [1,2,3,4,5] -> expected middle starting from 3
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.middleNode(head1)
    print(f"Test case 1: {linked_list_to_array(result1)}")
    # Expected output: [3, 4, 5]
    
    # Test case 2: [1,2,3,4,5,6] -> expected middle starting from 4  
    head2 = create_linked_list([1, 2, 3, 4, 5, 6])
    result2 = solution.middleNode(head2)
    print(f"Test case 2: {linked_list_to_array(result2)}")
    # Expected output: [4, 5, 6]
    
    # Test case 3: [1] -> expected middle starting from 1
    head3 = create_linked_list([1])
    result3 = solution.middleNode(head3)
    print(f"Test case 3: {linked_list_to_array(result3)}")
    # Expected output: [1]