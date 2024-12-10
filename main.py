from model import GameState, Sign
from services import NewGameCommand, PrintCommand, GameLogic, MachinePlayer
from view import ConsoleView


def main():
    state = GameState()
    view = ConsoleView()

    while True:
        view.show_menu(state)
        command_input = view.get_user_input()

        try:
            tokens = command_input.split()
            command = tokens[0].upper()

            if command == "NEW":
                size = int(tokens[1])
                if size < 5 or size > 25:
                    raise ValueError("Invalid board size. Must be between 5 and 25.")
                NewGameCommand(size).execute(state)

            elif command == "PRINT":
                PrintCommand().execute(state)

            elif command == "PUT":
                if not state.game_in_progress:
                    raise ValueError("No game in progress. Start a new game first.")
                row, col = map(int, tokens[1:3])
                if GameLogic.is_valid_move(state, row, col):
                    GameLogic.apply_move(state, row, col)
                    PrintCommand().execute(state)
                else:
                    print("Invalid move!")

            elif command == "EXIT":
                print("Exiting game. Goodbye!")
                break

            else:
                print("Unknown command!")

        except Exception as e:
            view.show_message(f"Error: {e}")


if __name__ == "__main__":
    main()
