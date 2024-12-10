import random


class GameLogic:
    @staticmethod
    def is_valid_move(state, row, col):
        table = state.table
        return (
            table.is_valid_position(row, col)
            and table.get_sign(row, col) == Sign.EMPTY
        )

    @staticmethod
    def apply_move(state, row, col):
        state.table.set_sign(row, col, state.who_is_on_move)
        state.toggle_turn()


class MachinePlayer:
    @staticmethod
    def get_random_move(state):
        table = state.table
        empty_positions = [
            Position(row, col)
            for row in range(table.size)
            for col in range(table.size)
            if table.get_sign(row, col) == Sign.EMPTY
        ]
        return random.choice(empty_positions) if empty_positions else None


class Command:
    def execute(self, state):
        raise NotImplementedError


class NewGameCommand(Command):
    def __init__(self, size):
        self.size = size

    def execute(self, state):
        state.start_new_game(self.size)
        print(f"New game started with board size {self.size}")


class PrintCommand(Command):
    def execute(self, state):
        table = state.table
        if table is None:
            print("No board to display. Start a new game first.")
        else:
            for row in table.board:
                print(" ".join(sign.value for sign in row))
