class ConsoleView:
    @staticmethod
    def show_menu(state):
        print("\n--- MENU ---")
        print("NEW <n> - Start a new game with board size n (5-25)")
        if state.game_in_progress:
            print("PUT <row> <col> - Make a move")
            print("PRINT - Print the current board")
            print("EXIT - Exit the program")
        else:
            print("EXIT - Exit the program")

    @staticmethod
    def get_user_input():
        return input("Enter command: ").strip()

    @staticmethod
    def show_message(message):
        print(message)
