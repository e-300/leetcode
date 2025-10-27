# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        dummmy_head = ListNode(-1)

        dummmy_head.next = head

        current = dummmy_head


        while current.next != None:

            #if the next nodes val is the val we are looking for 
            if current.next.val == val:
                current.next = current.next.next

            else:
                current = current.next

        return dummmy_head.next
    

    
    def removeElementsArr(self, head: ListNode, val: int) -> ListNode:
        arr = []

        while head:

            if head.val != val:
                arr.append(head.val)
        
            head = head.next

        head = ListNode(0)
        current = head

        for val in arr[0:]:

            current.next = ListNode(val)
            current = current.next
            
        return head.next

            

            




        

        


        





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
    head1 = create_linked_list([1, 2, 6, 3, 4, 5, 6])
    val1 = 6
    result1 = solution.removeElements(head1, val1)
    print(f"Test 1: {linked_list_to_array(result1)}")  # Expected: [1, 2, 3, 4, 5]
    
    # Test case 2
    head2 = create_linked_list([])
    val2 = 1
    result2 = solution.removeElements(head2, val2)
    print(f"Test 2: {linked_list_to_array(result2)}")  # Expected: []
    
    # Test case 3
    head3 = create_linked_list([7, 7, 7, 7])
    val3 = 7
    result3 = solution.removeElements(head3, val3)
    print(f"Test 3: {linked_list_to_array(result3)}")  # Expected: []