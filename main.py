GAME_IS_RUNNING = True
PLAYER_MARK = "X"
TURN = 0

board_map = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

print(("~" * 10) + "Welcome to the game!" + ("~" * 10))


def print_board():
    # printing the game board
    print("---+---+---")
    for r in range(3):
        print(board_map[r][0], " |", board_map[r][1], "|", board_map[r][2])
        print("---+---+---")


def switch_player(current):
    # Switching user X <--> 0
    global PLAYER_MARK
    if current == "X":
        PLAYER_MARK = "0"
    else:
        PLAYER_MARK = "X"


def get_user_choice(value, player):
    # Getting the user input
    x = 0
    try:
        if value == "row":
            x = int(input(f"Player {player} please select the row --> UPPER = 0 MIDDLE = 1 BOTTOM = 2: "))

        elif value == "column":
            x = int(input(f"Player {player} please select the column --> LEFT = 0 MIDDLE = 1 RIGHT = 2: "))

        if 3 > x >= 0:
            return x
        else:
            print("Out of boundaries. Please select number from 0 to 2")
            get_user_choice(value, player)

    except ValueError:
        print("Please choose the number")
        get_user_choice(value, player)


def check_winning_combination(board):
    # Checking rows
    global TURN
    global GAME_IS_RUNNING
    TURN += 1
    if TURN == 9:
        print()
        print("No winner today. Game Over.")
        GAME_IS_RUNNING = False
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2] == "X":
            print("Congratulations! Player X won!")
            GAME_IS_RUNNING = False

        elif board[row][0] == board[row][1] == board[row][2] == "0":
            print("Congratulations! Player 0 won!")
            GAME_IS_RUNNING = False

    # Checking columns
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] == "X":
            print("Congratulations! Player X won!")
            GAME_IS_RUNNING = False
        elif board[0][col] == board[1][col] == board[2][col] == "0":
            print("Congratulations! Player 0 won!")
            GAME_IS_RUNNING = False

    # Checking diagonal
    if board[0][0] == board[1][1] == board[2][2] == "X":
        print("Congratulations! Player X won!")
        GAME_IS_RUNNING = False

    elif board[0][0] == board[1][1] == board[2][2] == "0":
        print("Congratulations! Player 0 won!")
        GAME_IS_RUNNING = False

    elif board[0][2] == board[1][1] == board[2][0] == "X":
        print("Congratulations! Player X won!")
        GAME_IS_RUNNING = False

    elif board[0][2] == board[1][1] == board[2][0] == "0":
        print("Congratulations! Player 0 won!")
        GAME_IS_RUNNING = False


print_board()

while GAME_IS_RUNNING:

    print(f"Player {PLAYER_MARK} turn:")
    print()
    row = get_user_choice("row", PLAYER_MARK)
    column = get_user_choice("column", PLAYER_MARK)
    if board_map[row][column] == ' ':
        board_map[row][column] = PLAYER_MARK
    else:
        print()
        print("This spot is already taken. Please select again: ")
        print()
        row = get_user_choice("row", PLAYER_MARK)
        column = get_user_choice("column", PLAYER_MARK)
    print_board()
    check_winning_combination(board_map)
    switch_player(PLAYER_MARK)


