import os


board = [["3", " ", "4", " "], 
    [" ", "1", " ", "2"],
    [" ", "4", " ", "3"],
    ["2", " ", "1", " "]]
over = False

def print_board(zone,):
    os.system("cls")
    print(f"\n|-------------|\n|   Sudoku    |\n|-------------|")
    print("|A B C D //   |\n|-------------|")
    for n in range(4):
        for n2 in range(4):
            print(f"|{zone[n][n2]}", end="")
        print(f" || {n+1} |\n|-------------|")
    print("")

def x_correction(x):
    if x.upper() == "A":
        x = 0
    elif x.upper() == "B":
        x = 1
    elif x.upper() == "C":
        x = 2
    elif x.upper() == "D":
        x = 3
    return x


while not over:
    print_board(board)
    validmove = False
    while not validmove:
        move = input("Milyen számot tennél és hova? (szám, oszlop, sor)")
        move = move.strip().split()
        move_number = int(move[0])
        x = move[1]
        y = int(move[2])-1
        x = x_correction(x)

        if board[y][x] == " ":
            board[y][x] = move_number
            validmove = True
        else:
            change = input("Ezen a helyen már van egy szám, szeretnéd lecserélni?")