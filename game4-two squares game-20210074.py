#Author: Omnya Ahmed Mohamed
# ID: 20210074
# Game 4 -A1- 2 squares game
# User inputs 2 numbers that form a rectangle

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']

def display_board():
    print("---------------------")
    print("|", board[0], "", "|", board[1], "", "|", board[2], "", "|", board[3], "", "|")
    print("---------------------")
    print("|", board[4], "", "|", board[5], "", "|", board[6], "", "|", board[7], "", "|")
    print("---------------------")
    print("|", board[8], "", "|", board[9], "|", board[10], "|", board[11], "|")
    print("---------------------")
    print("|", board[12], "|", board[13], "|", board[14], "|", board[15], "|")
    print("---------------------")

# Checking valid/ invalid inputs and replacing the 2 no's with "X"

def play_game():
    player = -1
    c = game_running()
    while c > 0:
        player = (player + 1) % 2
        print("******************")
        print("player {}'s turn".format(player + 1))
        display_board()
        action1 = input("Choose a cell from 1 to 16 to form a rectangle : ")
        action2 = input("Choose another cell from 1 to 16 to form a rectangle :")
        while not action1.isdigit() or not action2.isdigit() or int(action1) < 1 or int(action1) > 16 or int(action2) < 1 or int(action2) > 16:
            print("____Invalid Inputs____")
            action1 = input("Choose a cell from 1 to 16 to form a rectangle : ")
            action2 = input("Choose another cell from 1 to 16 to form a rectangle :")
        if action1 > action2:
            a1 = action1
            a2 = action2
            action1 = a2
            action2 = a1
        while board[int(action1) - 1] == "X" or board[int(action2) - 1] == "X":
            while int(action2) != int(action1) + 1 and int(action2) != int(action1) + 4:
                print("____Invalid Inputs____")
                action1 = input("Choose a cell from 1 to 16 to form a rectangle : ")
                action2 = input("Choose another cell from 1 to 16 to form a rectangle :")
        while (board[int(action1) - 1] == '4' and board[int(action2) - 1] == '5') or (board[int(action1) - 1] == '8' and board[int(action2) - 1] == '9') or (board[int(action1) - 1] == '12' and board[int(action2) - 1] == '13'):
            print("____Inputs don't form a rectangle____")
            action1 = input("Choose a cell from 1 to 16 to form a rectangle : ")
            action2 = input("Choose another cell from 1 to 16 to form a rectangle :")
        board[int(action1) - 1] = "X"
        board[int(action2) - 1] = "X"
        c = game_running()
    display_board()
    c = no_winners()
    if c == 16:
        print("__GAME DIE__NO WINNER__")
    else:
        print("Player {} won".format(player + 1))

# Game die condition , when all the squares are replaced with "X"

def no_winners():
    c = 0
    for i in range(16):
        if board[i] == "X":
            c = c + 1
    return c

# Checking if the game is still running

def game_running():
    c = 0
    for i in range(0, 15):
        if i == 3 or i == 7 or i == 11:
            if board[i] != "X" and board[i + 4] != "X":
                c += 1
        elif i == 12 or i == 13 or i == 14:
            if board[i] != "X" and board[i + 1] != "X":
                c += 1
        else:
            if (board[i] != "X" and board[i + 1] != "X") or (board[i] != "X" and board[i + 4] != "X"):
                c += 1
    return c

play_game()
