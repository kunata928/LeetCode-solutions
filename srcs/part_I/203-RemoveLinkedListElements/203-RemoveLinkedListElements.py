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
    def removeElements(self, head, val: int):
        curr, prev = head, None
        while curr:
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
            else:
                prev = curr
            curr = curr.next
        return head


count_elems = 10
prev_elem = ListNode(val=1)
for elem in range(count_elems):
    next_elem = ListNode(val=elem, next=prev_elem)
    prev_elem = next_elem

next_elem.printList()
print()
Solution.removeElements(Solution, next_elem, 1).printList()
