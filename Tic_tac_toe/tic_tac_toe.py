import speech_recognition as sr

from collections import deque
from pprint import pprint

def get_name(): #speech recognition functionality
    pass
#TO DO PLS


def check_for_win():
    player_name, player_symbol = players[0].values()

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(SIZE)])
    second_diagonal_win = all([board[i][SIZE - i - 1] == player_symbol for i in range(SIZE)])
    row_win = any([all([el == player_symbol for el in row]) for row in board])
    col_win = any([all([board[row][col] == player_symbol for row in range(SIZE)]) for col in range(SIZE)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_board()
        print(f"!!!!!{player_name} has won!!!!!")

        raise SystemExit


def place_symbol(row, col):
    board[row][col] = players[0]["symbol"]

    check_for_win()
    print_board()

    if turns == SIZE * SIZE:
        print("Draw!")
        raise SystemExit

    players.rotate()


def choose_position():
    global turns

    while True:
        try:
            position = int(input(f"{players[0]['name']}, please choose a free position 1-{SIZE * SIZE}"))
            row, col = (position - 1) // SIZE, (position - 1) % SIZE
        except ValueError:
            print_select_valid_position()
            continue

        if 1 <= position <= SIZE * SIZE and board[row][col] not in ["X", "O"]:
            turns += 1

            place_symbol(row, col)
        else:
            print_select_valid_position()


def print_select_valid_position():
    print(f"{players[0]['name']}, Please select a valid position!!!")


def print_board():
    [print(f"| {' | '.join(row)} |") for row in board]


def print_game_state(begin=False):
    if begin:
        print("This is the numeration of the board")
        print_board()

        # for row in range(SIZE):
        #     for col in range(SIZE):
        #         board[row][col] = " "
    else:
        print_board()


def start():
    player_one_name = input("Player 1 enter your name")
    player_two_name = input("Player 2 enter your name")

    while True:
        player_one_symbol = input(f"{player_one_name} would you like to play with X or O?").upper()
        if player_one_symbol not in ["X", "O"]:
            print(f"{player_one_name} please select a valid option")
        else:
            break

    player_two_symbol = "O" if player_one_symbol == "X" else "X"
    players.append({"name": player_one_name, "symbol": player_one_symbol})
    players.append({"name": player_two_name, "symbol": player_two_symbol})

    print_game_state(begin=True)
    choose_position()


SIZE = 3
turns = 0

board = [[str(r+c) for c in range(SIZE)] for r in range(1, SIZE * SIZE + 1, SIZE)]
players = deque()

start()