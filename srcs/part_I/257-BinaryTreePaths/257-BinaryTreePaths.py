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
    def binaryTreePaths(self, root):
        if not root:
            return []
        return [str(root.val) + '->' + path
                for kid in (root.left, root.right) if kid
                for path in self.binaryTreePaths(self, kid)] or [str(root.val)]


    def binaryTreePaths1(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        treepaths = [str(root.val) + '->' + path for path in self.binaryTreePaths1(self, root.left)]
        print(treepaths)
        treepaths += [str(root.val) + '->' + path for path in self.binaryTreePaths1(self, root.right)]
        return treepaths

#       6
#    2      8
#   0 4    7 9

node1 = TreeNode(0, None, None)
node2 = TreeNode(4, None, None)
node3 = TreeNode(2, node1, node2)
node4 = TreeNode(7, None, None)
node5 = TreeNode(9, None, None)
node6 = TreeNode(8, node4, node5)
root = TreeNode(6, node3, node6)

# node1 = TreeNode(1, None, None)
# root = TreeNode(2, node1, None)

root.printTree()
print()
print(Solution.binaryTreePaths1(Solution, root))
# r == null: return res.append(path)
# [6]
# l [6, 2, 0]
# r
