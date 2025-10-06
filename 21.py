# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        tmplist = dummylist = ListNode(0)

    
        while (list1 and list2) != None:

            if list1.val > list2.val: 

                tmplist.next = list2
                list2 = list2.next

            else:
                tmplist.next = list1
                list1 = list1.next
            
            tmplist = tmplist.next
            
        tmplist.next = list1 or list2
        
        return dummylist.next

                
                

    def mergeTwoListsRecursive(self, list1: ListNode, list2: ListNode) -> ListNode:

        #BASE CASE THAT HANDLES THREE POSSIBILITIES 
        #IF L1 EMPTY OR L2 EMPTY OR BOTH EMPTY
        if not list1 or not list2:

            if list1:
                return list1
            else:
                return list2
            
        
        if list1.val > list2.val:
            list1, list2 = list2, list1


        list1.next = self.mergeTwoListsRecursive(list1.next, list2)

        return list1
            


    



# Helper function to create linked list from array
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
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


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoListsRecursive(list1, list2)
    print(f"Test 1: {linked_list_to_array(result)}")
    # Expected: [1, 1, 2, 3, 4, 4]
    
    # Test Case 2
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoListsRecursive(list1, list2)
    print(f"Test 2: {linked_list_to_array(result)}")
    # Expected: []
    
    # Test Case 3
    list1 = create_linked_list([5])
    list2 = create_linked_list([1, 2, 4])
    result = solution.mergeTwoListsRecursive(list1, list2)
    print(f"Test 3: {linked_list_to_array(result)}")
    # Expected: [1, 2, 4, 5]
