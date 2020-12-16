# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def display_board(board):
    print(board[7]+"  |  "+board[8]+"  |   "+board[9])
    print("-------------------")
    print(board[4]+"  |  "+board[5]+"  |   "+board[6])
    print("-------------------")
    print(board[1]+"  |  "+board[2]+"  |   "+board[3])


def check_board(board):
    if board[1] == board[2] == board[3] != "#" :
        return True
    elif board[4] == board[5] == board[6] != "#" :
        return True
    elif board[7] == board[8] == board[9] != "#" :
        return True
    elif board[1] == board[4] == board[7] != "#" :
        return True
    elif board[2] == board[5] == board[8] != "#" :
        return True
    elif board[3] == board[6] == board[9] != "#" :
        return True
    elif board[3] == board[5] == board[7] != "#" :
        return True
    elif board[1] == board[5] == board[9] != "#" :
        return True
    return False

def check_cell(board,index):
    index = int(index)
    return board[index] == "#"

def check_choice(board,choice):
    while not choice.isdigit():
        choice = input("Invalid input.\nenter your choice 1-9:")

    empty = check_cell(board, choice)
    while not empty:
        choice = input("Cell is already in use,try other number.\nenter your choice 1-9:")
    return int(choice)

def play(board,counter,players):
    if counter % 2 != 0:
        print("player1 turn.")
        choice = check_choice(board,input("enter your choice 1-9:"))
        board[choice] = players["player1"]
    else:
        print("player2 turn.")
        choice = check_choice(board,input("enter your choice 1-9:"))
        board[choice] = players["player2"]
    return board

def start():
    print("Welcome to Tic Tac Toe!")
    choice = ""
    while choice != 'X' and choice != 'O':
        choice = input("enter your choice X or O \n").upper()

    players = {}
    player1 = choice
    if player1 == 'X':
        players = {"player1": 'X', "player2": 'O'}
    else:
        players = {"player1": 'O', "player2": 'X'}

    print("player1 plays with "+players["player1"])
    print("player2 plays with "+players["player2"])

    board = ["#","#","#","#","#","#","#","#","#","#"]
    counter = 1
    while counter < 10 :  #there are 9 rounds for the game
        play(board, counter, players)
        display_board(board)
        counter += 1

        if counter >= 6 and check_board(board)==True:
            if counter%2!=0:
                print("player1 WIN!")
                break
            elif counter%2==0:
                print("player2 WIN!")
                break
        elif counter == 9:
            print("ITS A TIE!")


start()