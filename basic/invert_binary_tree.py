"""
Neste desafio você deverá construir uma função que recebe uma árvore binária e inverta seus itens filhos, ou seja, o nó filho da direita do item atual deve ser invertido com o nó filho da esquerda.

Os nós podem ter valores ou até mesmo serem nulos (indicando que não possuem filhos).

Exemplo:

Sua função receberá uma árvore binária da seguinte forma:

..........1 ......../...
.......2.....3 ....../....../.
....4...5.6..7 ..../.\
..8...9

E deverá retornar a árvore binária da seguinte forma:
..........1 ......../...
.......3.....2 ....../....../.
....5...4.7..6 ..../.\
..9...8
"""

from __future__ import annotations

from dataclasses import dataclass  # noqa: E402
from pprint import pprint


@dataclass
class BinaryTree:
    value: int
    left: BinaryTree | None = None
    right: BinaryTree | None = None


# Fail
def solution(tree: BinaryTree):
    def extract_binary_tree_values(
        tree: BinaryTree, tree_side: str = None, values: dict = None
    ):
        if not values:
            values = {"left": [], "right": []}

        if tree_side == "left":
            values["left"].append(tree.value)
        elif tree_side == "right":
            values["right"].append(tree.value)

        if tree.left:
            values = extract_binary_tree_values(tree.left, "left", values)

        if tree.right:
            values = extract_binary_tree_values(tree.right, "right", values)

        return values

    def invert_tree(tree: BinaryTree, values: dict, tree_side: str = None):
        value = None

        if tree_side == "left":
            value = values["right"].pop(0)
        elif tree_side == "right":
            value = values["left"].pop(0)

        if value:
            tree.value = value

        if tree.left:
            tree.left = invert_tree(tree.left, values, "left")

        if tree.right:
            tree.right = invert_tree(tree.right, values, "right")

        return tree

    values = extract_binary_tree_values(tree)
    pprint(tree)
    print(values)
    # values_reversed = {
    #     "left": list(reversed(values["left"])),
    #     "right": list(reversed(values["right"])),
    # }
    inverted_tree = invert_tree(tree, values)

    return inverted_tree


# O(n)
def solution(tree: BinaryTree):
    def invert_tree(tree: BinaryTree):
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


pprint(
    solution(
        BinaryTree(
            value=1,
            left=BinaryTree(
                value=2, left=BinaryTree(value=7), right=BinaryTree(value=6)
            ),
            right=BinaryTree(
                value=3, left=BinaryTree(value=5), right=BinaryTree(value=4)
            ),
        )
    )
)

"""
BinaryTree(value=1,
           left=BinaryTree(value=2,
                           left=BinaryTree(value=7, left=None, right=None),
                           right=BinaryTree(value=6, left=None, right=None)),
           right=BinaryTree(value=3,
                            left=BinaryTree(value=5, left=None, right=None),
                            right=BinaryTree(value=4, left=None, right=None)))
"""
