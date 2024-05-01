from day9_data_structures.tree.templatetree import BinaryTree


class Solution:
    def postorderTraversal(self, root: BinaryTree) -> list[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.data]

    def preorderTraversal(self, root: BinaryTree) -> list[int]:
        if not root:
            return []
        return [root.data] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def inorderTraversal(self, root: BinaryTree) -> list[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.data] + self.inorderTraversal(root.right)
