# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return

        carry = 0
        dummy = ListNode()  # Create a dummy node
        current = dummy  # Use a current pointer to iterate and build the new linked list

        while l1 or l2 or carry != 0: # Keep running while either list contains elements or if carrying a value
            digit = carry
           
            if l1:
                digit += l1.val
                l1 = l1.next
            if l2:
                digit += l2.val
                l2 = l2.next
      
            carry = digit // 10  # Calculate the carry for the next iteration
            digit %= 10  # Calculate the current digit value

            current.next = ListNode(digit)  # Create a new node with the current digit
            current = current.next  # Move the current pointer to the next node

        return dummy.next

        