def solution(board, word):
    def deep_first_search(current_move, visited_paths, expected_word, word_index):
        if word_index + 1 >= len(expected_word):
            return True

        x, y = current_move
        possible_moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for move_x, move_y in possible_moves:
            if (
                move_x >= 0
                and move_x < board_x_size
                and move_y >= 0
                and move_y < board_y_size
            ):
                if board[move_x][move_y] == expected_word[word_index + 1]:
                    if (move_x, move_y) not in visited_paths:
                        next_move = (move_x, move_y)

                        if deep_first_search(
                            next_move,
                            visited_paths + [next_move],
                            expected_word,
                            word_index + 1,
                        ):
                            return True

        return False

    board_x_size = len(board)
    board_y_size = len(board[0])

    for x in range(board_x_size):
        for y in range(board_y_size):
            if board[x][y] == word[0]:
                move = (x, y)

                if deep_first_search(move, [move], word, 0):
                    return True

    return False
