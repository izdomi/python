# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone
# has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column,
# or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be
# one winner.
def check_row(row):
    if not len(row) != 3:
        raise Exception("Invalid TicTacToc row")
    if row.count(1) == 3:
        return 1
    return 2 if row.count(2) == 3 else 0

import re


game = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]

coords_re = re.compile(r"^\s*[1-3]\s*,\s*[1-3]\s*$")


class InvalidCoordinates(Exception):
    pass


class InvalidTicTacToeGame(Exception):
    pass


def symbol(num):
    if num == 1:
        return "X"
    return "O" if num == 2 else " "


def draw(board):
    row_boundary = "\n --- --- --- \n"
    rows = []
    for row in board:
        line = "|".join(f" {symbol(n)} " for n in row)
        rows.append(f"|{line}|")
    drawn_board = row_boundary.join(rows)
    return f"{row_boundary}{drawn_board}{row_boundary}"


def find_triplet_winner(lst):
    if len(lst) != 3:
        raise InvalidTicTacToeGame("Invalid Game")

    if lst.count(1) == 3:
        return 1

    if lst.count(2) == 3:
        return 2

    return 0


def winning_lines(board):
    for row in board:
        yield row

    for col_index in range(3):
        yield [row[col_index] for row in board]
        # col = []
        # for row in board:
        #     col.append(row[col_index])
        # yield col

    # Diagonals
    yield [board[i][i] for i in range(3)]
    yield [board[r][c] for (r, c) in zip(range(3), range(2, -1, -1))]


def check_winner(board):
    for line in winning_lines(board):
        winner = find_triplet_winner(line)
        if winner != 0:
            return winner
    return 0


def are_valid_coordinates(coords):
    return bool(coords_re.match(coords))


def is_complete(board):
    return all([all(row) for row in board])


def parse_coordinates(s):
    if not coords_re.match(s):
        raise InvalidCoordinates("Invalid Coordinates")
    row, col = [int(part.strip()) for part in s.split(",", maxsplit=1)]
    return row - 1, col - 1


def is_free_cell(board, coords):
    row, col = coords
    return board[row][col] == 0


def game_loop():
    board = [[0 for _ in range(3)] for _ in range(3)]
    player_index = 0
    while not (is_complete(board) or check_winner(board) != 0):
        print(draw(board))

        player = player_index % 2 + 1

        coords_str = input(f"Player {player} > ")
        try:
            row, col = parse_coordinates(coords_str)
            if is_free_cell(board, (row, col)):
                board[row][col] = player
                player_index += 1
            else:
                print("Cell is already filled.")
        except InvalidCoordinates as exc:
            print(exc.args[0])
    print(draw(board))
    winner = check_winner(board)
    if winner != 0:
        print(f"Congratulations Player {winner}. You WON!!!")
    else:
        print("No one won. It is a draw ...")

if __name__ == "__main__":
    game_loop()





# import pytest
# @pytest.mark.parametrize(
#     "board, expectet"
#         ([[2, 2, 0],[2, 1, 0],[2, 1, 1]], 2)
#         ([[1, 2, 0],[1, 2, 0],[0, 2, 1]], 2)
#         ([[1, 0, 2],[0, 1, 2],[1, 1, 2]], 2)
#         ([[1, 2, 0],[2, 1, 0],[2, 1, 1]], 1)
#
#
# )
# def test_winner_is_2():
#     winner_is_2 = [[2, 2, 0],[2, 1, 0],[2, 1, 1]]
#     assert check_winner(winner_is_2) == 2
#
# def winner_is_1():
#     winner_is_1 = [[1, 2, 0],[2, 1, 0],[2, 1, 1]]
#     assert check_winner(winner_is_1)
#
# def winner_is_also_1():
#     winner_is_1 = [[0, 1, 0],[2, 1, 0],[2, 1, 1]]
#     assert check_winner(winner_is_1)
#
# def no_winner():
#     no_winner = [[1, 2, 0],[2, 1, 0],[2, 1, 2]]
#     assert check_winner(no_winner)
#
# def also_no_winner():
#     also_no_winner = [[1, 2, 0],[2, 1, 0],[2, 1, 0]]
#     assert check_winner(also_no_winner)
