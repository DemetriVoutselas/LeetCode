 class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        if not head: return False
        while (fast.next) and (fast.next.next):
            fast = fast.next.next
            if slow == fast:
                return True
            else: slow = slow.next
        return False
