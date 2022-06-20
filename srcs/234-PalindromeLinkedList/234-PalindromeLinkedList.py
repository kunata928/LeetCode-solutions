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
    def isPalindrome(self, head):
        arr_list = list()
        while head:
            arr_list.append(head.val)
            head = head.next
        return arr_list == arr_list[::-1]

    def isPalindrome01(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            rev.printList()
            print()
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev

count_elems = 11
node00 = ListNode(val=1)
node01 = ListNode(val=2, next=node00)
node02 = ListNode(val=2, next=node01)
node03 = ListNode(val=1, next=node02)


node03.printList()
print()
print(Solution.isPalindrome01(Solution, node03))