import random

def initialize_board():
    return [['?' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def place_bomb(board):
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    return row, col

def check_win(board):
    for row in board:
        if '?' in row:
            return False
    return True
def make_line():
    print("=================================================") 

def play_game():
    make_line()
    board = initialize_board()
    print_board(board)
    place_bomb(board)
    bomb_row, bomb_col = place_bomb(board)
    while True:
        make_line()
        row = int(input("\nEnter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if row == bomb_row and col == bomb_col:
          print("Yikes, you found a bomb. Game over!\n")
          make_line()
          board[row][col] = 'X'
          print_board(board)
          break
        else:
          print("Well, there's no bomb here. Congrats!.\n")
          make_line()
          board[row][col] = 'O'
          print_board(board)
          if check_win(board):
              print("Congratulations! You win the game!")
              break
  
play_game()
