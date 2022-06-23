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
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next