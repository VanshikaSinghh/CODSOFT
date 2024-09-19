# Tic-Tac-Toe game
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
    
    def print_board(self):
        print("\n")
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")
        print("\n")
    
    def is_winner(self, player):
        win_conditions = [
            [0, 1, 2],  # Top row
            [3, 4, 5],  # Middle row
            [6, 7, 8],  # Bottom row
            [0, 3, 6],  # Left column
            [1, 4, 7],  # Middle column
            [2, 5, 8],  # Right column
            [0, 4, 8],  # Diagonal 1st
            [2, 4, 6]   # Diagonal 2nd
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] == player:
                return True
        return False
    
    def is_full(self):
        # now check if the board iss full
        return ' ' not in self.board
    
    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.is_winner(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                return True
            elif self.is_full():
                # If the board is full and the winner isnt declared, displays error
                self.print_board()
                raise Exception("Nobody wins! Game is a draw.")
            # Switching the player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("This position is already taken. Try another.")
        return False
    
    def start_game(self):
        # Main loop of the game
        print("Welcome to the game of Tic-Tac-Toe!")
        while True:
            self.print_board()
            try:
                move = int(input(f"Player {self.current_player}, enter your move now (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Invalid move! Please enter a number between 1 and 9.")
                    continue
                if self.make_move(move):
                    break
            except ValueError:
                print("Please enter a valid number.")
            except Exception as e:
                print(e)
                break

# Run the game
game = TicTacToe()
game.start_game()