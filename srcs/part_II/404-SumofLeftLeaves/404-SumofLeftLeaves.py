class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
        print(self.val)
        if not all((self.left, self.right)):
            return None
        TreeNode.printTree(self.left)
        TreeNode.printTree(self.right)


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        pass


node1 = TreeNode(1, None, None)
node2 = TreeNode(2, None, None)
node3 = TreeNode(3, node1, node2)
node4 = TreeNode(4, None, None)
node5 = TreeNode(5, None, None)
node6 = TreeNode(6, node4, node5)
root = TreeNode(7, node3, node6)

root.printTree()
print()
head = Solution.invertTree1(Solution, root)
head.printTree()

#       7
#    3      6
#   1 2    4 5


