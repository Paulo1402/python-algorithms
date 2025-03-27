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


from algorithms.utils import BinaryTree

result = solution(
    BinaryTree(
        value=1,
        left=BinaryTree(
            value=2,
            left=BinaryTree(value=4),
            right=BinaryTree(value=5),
        ),
        right=BinaryTree(
            value=3,
            left=BinaryTree(value=6),
        ),
    )
)

print(result)
