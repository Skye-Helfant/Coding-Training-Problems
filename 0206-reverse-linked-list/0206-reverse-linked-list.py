# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity O(n), Memory Complexity O(n)
        prev, current = None, head

        while current:
            # stores current.next in temporary variable
            nxt = current.next
            current.next = prev # set next to reversed values 
            prev = current # sets previous to reversed list up to the current iteration
            current = nxt # sets current back to original linked list for the next loop
        return prev
