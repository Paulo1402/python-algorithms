# O(n)
def solution(tree):
    def invert_tree(tree):
        if tree.left is None and tree.right is None:
            return tree

        tree.left, tree.right = tree.right, tree.left

        if tree.left:
            tree.left = invert_tree(tree.left)

        if tree.right:
            tree.right = invert_tree(tree.right)

        return tree

    inverted_tree = invert_tree(tree)
    return inverted_tree
