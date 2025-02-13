def solution(root, expected_sum):
    def dfs(node, current_path, current_sum, expected_sum, result):
        if not node:
            return

        current_sum += node.value
        node_without_leaf = node.left is None and node.right is None

        if node_without_leaf and current_sum == expected_sum:
            result += [current_path + [node.value]]
            return

        dfs(node.left, current_path + [node.value], current_sum, expected_sum, result)
        dfs(node.right, current_path + [node.value], current_sum, expected_sum, result)

    result = []

    if root:
        dfs(root, [], 0, expected_sum, result)

    return result
