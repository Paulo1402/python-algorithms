def solution(tree1, tree2):
    if tree1 is None or tree2 is None:
        if tree1 == tree2:
            return True

        return False

    if tree1.value == tree2.value:
        return solution(tree1.left, tree2.left) and solution(tree1.right, tree2.right)

    return False
