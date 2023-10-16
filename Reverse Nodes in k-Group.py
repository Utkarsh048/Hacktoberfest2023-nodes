# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverseLinkedList(head, k):
            prev = None
            current = head
            while k > 0:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                k -= 1
            return prev
        
        def countNodes(head):
            count = 0
            current = head
            while current:
                count += 1
                current = current.next
            return count
        
        count = countNodes(head)
        if count < k:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        while count >= k:
            group_head = prev_group_tail.next
            group_tail = group_head
            for _ in range(k - 1):
                group_tail = group_tail.next
            
            next_group_head = group_tail.next
            group_tail.next = None
            
            prev_group_tail.next = reverseLinkedList(group_head, k)
            group_head.next = next_group_head
            
            prev_group_tail = group_head
            count -= k
        
        return dummy.next
