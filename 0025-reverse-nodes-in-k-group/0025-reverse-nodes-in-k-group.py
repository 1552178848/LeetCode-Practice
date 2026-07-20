# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            prev = group_next
            cur = group_prev.next

            while cur != group_next:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
            
            new_group_prev = group_prev.next
            group_prev.next = kth
            group_prev = new_group_prev
        
        return dummy.next