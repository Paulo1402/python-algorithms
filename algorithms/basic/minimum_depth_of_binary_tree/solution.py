# BFS
def solution(root):
    if root:
        queue = [(root, 1)]

        while queue:
            node, level = queue.pop(0)

            if node.left is None and node.right is None:
                return level

            level += 1

            if node.left:
                queue.append((node.left, level))

            if node.right:
                queue.append((node.right, level))

    return 0
