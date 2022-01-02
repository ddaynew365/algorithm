# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_head = list()
        while head.next:
            list_head.append(head.val)
            head = head.next
        list_head.append(head.val)

        for front, back in zip(list_head, list_head[::-1]):
            if front != back:
                return False
        return True