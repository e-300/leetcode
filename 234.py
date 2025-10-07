# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []


        while head != None:

            arr.append(head.val)

            head = head.next

        
        return arr == arr[::-1]










# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Test Case 1: Palindrome with even number of nodes
head1 = create_linked_list([1, 2, 2, 1])
solution = Solution()
print(f"Test 1: {solution.isPalindrome(head1)}")  # Expected: True

# Test Case 2: Palindrome with odd number of nodes
head2 = create_linked_list([1, 2, 3, 2, 1])
print(f"Test 2: {solution.isPalindrome(head2)}")  # Expected: True

# Test Case 3: Not a palindrome
head3 = create_linked_list([1, 2, 3, 4, 5])
print(f"Test 3: {solution.isPalindrome(head3)}")  # Expected: False