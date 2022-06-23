# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
        if not self:
            return None
        print(self.val)
        TreeNode.printTree(self.left)
        TreeNode.printTree(self.right)


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        if root:
            if max(q.val, p.val) < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            elif min(q.val, p.val) > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return root


# node1 = TreeNode(0, None, None)
# node2 = TreeNode(4, None, None)
# node3 = TreeNode(2, node1, node2)
# node4 = TreeNode(7, None, None)
# node5 = TreeNode(9, None, None)
# node6 = TreeNode(8, node4, node5)
# root = TreeNode(6, node3, node6)

node1 = TreeNode(1, None, None)
root = TreeNode(2, node1, None)

root.printTree()
print()
print(Solution.lowestCommonAncestor(Solution, root, root, node1).val)

#       6
#    2      8
#   0 4    7 9