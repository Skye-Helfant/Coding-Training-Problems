# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        sol = ListNode()

        trail = sol
        curr = head
        while curr != None:
            values.append(curr.val)
            curr = curr.next
            trail.next = ListNode()
            trail = trail.next

        values.reverse()

        curr = sol.next
        index = 0
        while curr != None:
            curr.val = values[index]
            index += 1
            curr = curr.next 

        return sol.next
