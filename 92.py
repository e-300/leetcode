# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        l = left-1
        r = right-1

        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l +=1
            r -=1
        
        
        head = ListNode(arr[0])
        curr = head

        for index, val in enumerate(arr):

            curr.next = ListNode(val)
            curr = curr.next

        return head.next 
    

    def reverseBtw(self, head: ListNode, left: int, right: int) -> ListNode:

        dummy_head = ListNode(-1)

        dummy_head = head

        while head:
            print(head.val)

            head = head.next
            
    




        


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
    left1, right1 = 2, 4
    result1 = solution.reverseBtw(head1, left1, right1)
    print(f"Test 1: {linked_list_to_array(result1)}")  # Expected: [1, 4, 3, 2, 5]
    
    # Test case 2
    head2 = create_linked_list([5])
    left2, right2 = 1, 1
    result2 = solution.reverseBtw(head2, left2, right2)
    print(f"Test 2: {linked_list_to_array(result2)}")  # Expected: [5]
    
    # Test case 3
    head3 = create_linked_list([3, 5, 7, 9, 11])
    left3, right3 = 1, 5
    result3 = solution.reverseBtw(head3, left3, right3)
    print(f"Test 3: {linked_list_to_array(result3)}")  # Expected: [3, 9, 7, 5, 11]