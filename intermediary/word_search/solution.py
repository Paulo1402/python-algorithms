"""
Dado uma matriz 2D e uma palavra, identifique se esta determinada palavra está dentro da matriz.

A palavra pode ser construída a partir de letras que estão sequenciais em valores adjacentes, onde valores adjacentes são aqueles que estão horizontalmente ou verticalmente por perto.

LEMBRE-SE: a mesma letra não pode ser usada duas vezes para construir uma palavra.

Exemplo:

board = [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]

Dada a palavra = "ABCCED", retorne true.
Dada a palavra = "SEE", retorne true.
Dada a palavra = "ABCB", retorne false.
"""


class Solution:
    _board = None
    _board_x_size = -1
    _board_y_size = -1

    def solution(self, board, word):
        self.board = board

        self._board_x_size = len(self.board)
        self._board_y_size = len(self.board[0])

        for x in range(self._board_x_size):
            for y in range(self._board_y_size):
                if self.board[x][y] == word[0]:
                    move = (x, y)

                    if self._deep_first_search(move, [move], word, 0):
                        return True

        return False

    def _deep_first_search(
        self, current_move, visited_paths, expected_word, word_index
    ):
        if word_index + 1 >= len(expected_word):
            return True

        x, y = current_move
        possible_moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for move_x, move_y in possible_moves:
            if (
                move_x >= 0
                and move_x < self._board_x_size
                and move_y >= 0
                and move_y < self._board_y_size
            ):
                if self.board[move_x][move_y] == expected_word[word_index + 1]:
                    if (move_x, move_y) not in visited_paths:
                        next_move = (move_x, move_y)

                        if self._deep_first_search(
                            next_move,
                            visited_paths + [next_move],
                            expected_word,
                            word_index + 1,
                        ):
                            return True

        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
solution = Solution()

print(solution.solution(board, word="ABCCED"))
print(solution.solution(board, word="SEE"))
print(solution.solution(board, word="ABCB"))
