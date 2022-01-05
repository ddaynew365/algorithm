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
    
# 런너 기법
# 연결리스트를 순회할 때, 2개의 포인터를 동시에 사용하는 기법
# 한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용하게 사용할 수 있다.