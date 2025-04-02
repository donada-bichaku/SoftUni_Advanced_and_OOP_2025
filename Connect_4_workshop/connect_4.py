class FullColError(Exception):
    pass


class InvalidColumn(Exception):
    pass


ROWS = 6
COLS = 7
MAX_CONNECTION = 4

DIRECTION_MAPPER = {
    "left": (0, -1),
    "up": (-1 ,0),
    "main_diagonal": (-1, -1),
    "secondary_diagonal": (-1, 1),
}

def travel_direction(coordinates, current_row, current_col, element, board):
    count = 0
    for i in range(1, MAX_CONNECTION):
        row_direction, col_direction = coordinates
        next_el_row_index = current_row + row_direction * i
        next_el_col_index = current_col + col_direction * i
        try:
            if board[next_el_row_index][next_el_col_index] == element:
                count += 1
            else:
                return count
        except IndexError:
            return count
    return count


def travel_opposite_direction(coords, curr_row_index, curr_col_index, searched_element, board):
    count = 0
    for i in range(1, MAX_CONNECTION):
        row_direction, col_direction = coords
        next_el_row_index = curr_row_index - row_direction * i
        next_el_col_index = curr_col_index - col_direction * i
        try:
            if board[next_el_row_index][next_el_col_index] == searched_element:
                count += 1
            else:
                return count
        except IndexError:
            return count
    return count


def is_winner(curr_row_index, curr_col_index, board):
    for direction, coords in DIRECTION_MAPPER.items():
        searched_element = board[curr_row_index][curr_col_index]
        travel_direction_count = travel_direction(coords, curr_row_index, curr_col_index, searched_element, board)
        travel_opposite_direction_count = travel_opposite_direction(coords, curr_row_index, curr_col_index, searched_element, board)

        if travel_direction_count + travel_opposite_direction_count + 1 >= MAX_CONNECTION:
            return True
    else:
        return False


def validate_column_choice(col):
    if 1 <= col <= COLS:
        return True
    else:
        raise InvalidColumn


def print_board(board):
    for row in board:
        print(row)


def get_first_available_row(col_index, board):
    for row_index in range(ROWS-1, -1, -1):
        if board[row_index][col_index] == 0:
            return row_index
    else:
        raise FullColError("This column is already full, choose another column!!!")


def board_is_full(turns):
    return turns > ROWS*COLS



board = [[0 for col in range(COLS)] for row in range(ROWS)]
turns = 1

while True:
    player = 2 if turns % 2 == 0 else 1

    try:
        column = input(f"Player {player} please choose a column: ")
        column_index = int(column) - 1
        validate_column_choice(int(column))
        row = get_first_available_row(column_index, board)
        board[row][column_index] = player
        if is_winner(row, column_index, board):
            print(f"WINNER is {player}")
            break
    except FullColError as ex:
        print(str(ex))
        continue
    except InvalidColumn:
        print(f"This column is invalid, please select between 1-{COLS}")
        continue
    except ValueError:
        print(f"Invalid input, please select between 1-{COLS}")
        continue


    print_board(board)

    turns += 1
    if board_is_full(turns):
        print("Board is full. No winners this game")
        exit(0)

print_board(board)

