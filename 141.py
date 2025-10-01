# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if not head:
            return None

        fast = slow = head

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
            
        return False





# Helper function to create a linked list with a cycle
def createLinkedList(values, pos):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    nodes = [head]
    
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        nodes.append(current)
    
    # Create cycle if pos is not -1
    if pos != -1:
        current.next = nodes[pos]
    
    return head

# Test Case 1
head1 = createLinkedList([3, 2, 0, -4], 1)
sol = Solution()
print(sol.hasCycle(head1))  # Expected output: True

# Test Case 2
head2 = createLinkedList([1, 2], 0)
print(sol.hasCycle(head2))  # Expected output: True

# Test Case 3
head3 = createLinkedList([1], -1)
print(sol.hasCycle(head3))  # Expected output: False