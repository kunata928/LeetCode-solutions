# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        head = self
        while head:
            print(head.val, end="->")
            head = head.next


class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


count_elems = 10
prev_elem = ListNode(val=1)
for elem in range(count_elems):
    next_elem = ListNode(val=elem, next=prev_elem)
    prev_elem = next_elem

next_elem.printList()
print()
Solution.reverseList(Solution, next_elem).printList()

