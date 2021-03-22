import random
starting_board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j == 2:
                print(board[i][j])
            else:
                print(board[i][j], end=" | ")
        if i == 0 or i == 1:
            print("---------")


def enter_moves():
    coordinate_i = int(input("Enter i coordinate: "))
    coordinate_j = int(input("Enter j coordinate: "))
    starting_board[coordinate_i][coordinate_j] = "X"
    return coordinate_i, coordinate_j


def logic():
    computer_moves = [(0, 0), (0, 2), (2, 0), (2, 2), (0, 1), (1, 0), (1, 2), (2, 1), (1, 1)]
    player_win = False
    computer_win = False
    while True:
        x, y = enter_moves()
        if not (len(computer_moves) == 0):
            computer_moves.remove((x, y))
            computer_move = random.choice(computer_moves)
            starting_board[computer_move[0]][computer_move[1]] = "O"
            computer_moves.remove(computer_move)
        print_board(starting_board)
        if starting_board[0][0] == starting_board[0][1] == starting_board[0][2] == "X":
            player_win = True
            break
        elif starting_board[1][0] == starting_board[1][1] == starting_board[1][2] == "X":
            player_win = True
            break
        elif starting_board[2][0] == starting_board[2][1] == starting_board[2][2] == "X":
            player_win = True
            break
        elif starting_board[0][0] == starting_board[1][0] == starting_board[2][0] == "X":
            player_win = True
            break
        elif starting_board[0][1] == starting_board[1][1] == starting_board[2][1] == "X":
            player_win = True
            break
        elif starting_board[0][2] == starting_board[1][2] == starting_board[2][2] == "X":
            player_win = True
            break
        elif starting_board[0][0] == starting_board[1][1] == starting_board[2][2] == "X":
            player_win = True
            break
        elif starting_board[2][0] == starting_board[1][1] == starting_board[0][2] == "X":
            player_win = True
            break
        if starting_board[0][0] == starting_board[0][1] == starting_board[0][2] == "O":
            computer_win = True
            break
        elif starting_board[1][0] == starting_board[1][1] == starting_board[1][2] == "O":
            computer_win = True
            break
        elif starting_board[2][0] == starting_board[2][1] == starting_board[2][2] == "O":
            computer_win = True
            break
        elif starting_board[0][0] == starting_board[1][0] == starting_board[2][0] == "O":
            computer_win = True
            break
        elif starting_board[0][1] == starting_board[1][1] == starting_board[2][1] == "O":
            computer_win = True
            break
        elif starting_board[0][2] == starting_board[1][2] == starting_board[2][2] == "O":
            computer_win = True
            break
        elif starting_board[0][0] == starting_board[1][1] == starting_board[2][2] == "O":
            computer_win = True
            break
        elif starting_board[2][0] == starting_board[1][1] == starting_board[0][2] == "O":
            computer_win = True
            break
        if len(computer_moves) == 0:
            break
    if player_win:
        return "P"
    elif player_win == computer_win:
        return "D"
    else:
        return "C"


def score():
    print_board(starting_board)
    win_point = logic()
    if win_point == "P":
        print("Player Won")
    elif win_point == "D":
        print("Nobody Won")
    else:
        print("Computer Won")


if __name__ == '__main__':
    score()
