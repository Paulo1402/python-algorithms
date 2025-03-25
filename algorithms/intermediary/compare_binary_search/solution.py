"""
Dadas duas árvores binárias, escreva uma função que indique se elas são iguais ou não.

As duas árvores binárias são consideradas as mesmas se elas forem estruturalmente identicas e os nós estiverem com o mesmo valor.

Exemplos:

Entrada:
      1          1
     / \        / \
    2   3      2   3
   [1,2,3],   [1,2,3]

Deverá retornar true pois as duas arvores são identicas.

Entrada:

      1          1
     / \        / \
    2   3      2   3
   / \
  4   5
 [1,2,4,5,3],  [1,2,3]

 Deverá retornar false pois as duas arvores são diferentes.
"""


# DFS
def solution_1(tree1, tree2):
    if tree1 is None or tree2 is None:
        if tree1 == tree2:
            return True

        return False

    if tree1.value == tree2.value:
        return solution_1(tree1.left, tree2.left) and solution_1(
            tree1.right, tree2.right
        )

    return False


# BFS
def solution_2(tree1, tree2):
    queue = [(tree1, tree2)]

    while queue:
        t1, t2 = queue.pop(0)

        if t1 is None or t2 is None:
            if t1 == t2:
                continue
            return False

        if t1.value != t2.value:
            return False

        queue.append((t1.left, t2.left))
        queue.append((t1.right, t2.right))

    return True
