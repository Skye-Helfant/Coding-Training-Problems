# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base Cases
        if not list1 and not list2:
            return None
        
        if not list1 and list2:
            return list2

        if list1 and not list2:
            return list1

        p1, p2 = list1, list2
        dummy = ListNode()  # Dummy node to start the merged list
        current = dummy

        while p1 and p2:
            if p1.val <= p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next

        # Connect the remaining nodes
        current.next = p1 if p1 else p2

        return dummy.next  # Return the merged list starting from the next node of the dummy

            