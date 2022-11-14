# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        st= set()
        current = head
        while current:
            if current in st:
                return True
            st.add(current)
            current = current.next
        return False

            


    