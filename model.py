from enum import Enum


class Sign(Enum):
    EMPTY = '.'
    X = 'X'
    O = 'O'


class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col


class Table:
    def __init__(self, size):
        self.size = size
        self.board = [[Sign.EMPTY for _ in range(size)] for _ in range(size)]

    def get_sign(self, row, col):
        return self.board[row][col]

    def set_sign(self, row, col, sign):
        self.board[row][col] = sign

    def is_valid_position(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size


class GameState:
    def __init__(self):
        self.table = None
        self.who_is_on_move = Sign.X
        self.game_in_progress = False

    def start_new_game(self, size):
        self.table = Table(size)
        self.game_in_progress = True
        self.who_is_on_move = Sign.X

    def toggle_turn(self):
        self.who_is_on_move = Sign.O if self.who_is_on_move == Sign.X else Sign.X

    def end_game(self):
        self.game_in_progress = False
