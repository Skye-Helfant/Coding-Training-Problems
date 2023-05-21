# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # get index of element to remove
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        remove_index = length - n

        # remove element
        prev, current = None, head
        index = 0
        while current:
            # if element is the last element of the list
            if index == remove_index and current.next == None:
                if prev != None:
                    prev.next = None
                if index == 0:
                    return None
                return head
            # if element is not the last element of the list
            elif index == remove_index and current.next != None:
                if remove_index == 0:
                    current = head
                    return head.next
                if prev != None:
                    prev.next = current.next
                return head

            prev = current
            current = current.next
            index += 1