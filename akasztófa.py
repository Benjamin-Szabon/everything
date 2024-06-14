import os
import random


def print_board(board):
    os.system("cls")
    for n in range(7):
        for n2 in range(5):
            print(board[n][n2], end="")
        print("")
    for n in range(len(rejtett)):
        print(rejtett[n], "", end="")
    print(f"\nRossz tippek: {rossz} ")
def loose(points, board):
    if points == 1:
        board[6][0] = "_"
        board[6][1] = "|"
        board[6][2] = "_"
        board[6][3] = "_"
        board[6][4] = "_"
        
    elif points == 2:
        board[1][1] = "|"
        board[2][1] = "|"
        board[3][1] = "|"
        board[4][1] = "|"
        board[5][1] = "|"
    elif points == 3:
        board[0][1] = "_"
        board[0][2] = "_"
        board[0][3] = "_"
    elif points == 4:
        board[1][4] = "|"
    elif points == 5:
        board[2][4] = "O"
    elif points == 6:
        board[3][3] = "/|\\"
    elif points == 7:
        board[4][3] = "/ \\"
again = True

while again == True:
    szo = random.choice(["alma", "kutya", "templom", "kerék", "parkoló"])
    over = False
    rossz = []
    board = [[" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "]]
    points = 0
    rejtett = "_ " * len(szo)
    rejtett = rejtett.strip().split()
    again = False

    while not over:
        print_board(board)
        tipp = input("Tippelj egy betűt / a szót: ").lower()

        if tipp not in szo and tipp not in rossz:
            rossz.append(tipp)
            points += 1
        else:
            for n in range(len(szo)):
                if tipp == szo[n]:
                    rejtett[n] = tipp
        loose(points,board)

        if tipp == szo or "_" not in rejtett:
            for n in range(len(szo)):
                if tipp == szo[n]:
                    rejtett[n] = tipp
            print_board(board)
            print("Kitaláltad a szót")
            over = True

        if points >= 7:
            print_board(board)
            print("Felakasztottak :(")
            over = True
    again = input("Folyatod ->y vagy kilépsz ->n ? ")
    if again.lower() == "y":
        again = True
        over = False
