import random
import os

over = False
move_xy = ""
last = ""
rematch = True
scores = {"x": 0, "o": 0, "draw": 0}
move = random.choice(["X","O"])
end = ["END", "CLOSE", "QUIT", "EXIT"]
vektors = []
mode = 0

#function for printing out the zone
def print_zone(zone, scores):
    os.system("cls")
    print(f"\n|---------|\n|Scores:  |\n|X: {scores['x']}     |\n|O: {scores['o']}     |\n|Draw: {scores['draw']}  |\n|---------|\n|---------|")
    print("|1 2 3 /  |")
    for n in range(3):
        for n2 in range(3):
            print(f"|{zone[n][n2]}", end="")
        print(f"| {n+1} |\n|---------|")
    print("")

#choosing a mode
def choose_mode(mode, end):
    while mode not in ["1", "2", "3"]:
        os.system("cls")
        print("Choose between option '1', '2', or '3'")
        mode = input("Which mode would you like to play?\n 1. 2 player mode\n 2. Player against an easy bot\n 3. Player against an expert bot\n ")
        if mode.upper() in end:
            quit()
    return mode        

#scanning surroundings
def scanning(vektors):
    vektors.clear()
    for v in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        vektor_y = v[0]
        vektor_x = v[1]
        try:
            if zone[x+vektor_x][y+vektor_y] == move and 3 <= (x + vektor_x) >= 0 and 3 <= (y + vektor_y) >= 0:
                vektors.append([vektor_x, vektor_y])
        except:
            pass

#checking for win condition
def winning(vektors, over):

    for v in vektors:
        try:
            if zone[x + (2 * v[0])][y + (2 * v[1])] == move: 
                over = True
                print_zone(zone, scores)
                print(f"{move} won the round.")
        except:
            pass
        try:
            if zone[x - v[0]][y - v[1]] == move:
                over = True
                print_zone(zone, scores)
                print(f"{move} won the round.")
        except:
            pass
    return over
    
#scores
def scoring():
    if over and draw != 0:
        if move == "X":
            scores["x"] += 1
        else:
            scores["o"] += 1

#draw
def draw(over):
    if not over:
        draw = 9
        for n in range(3):
            for n2 in range(3):
                if zone[n][n2] != " ":
                    draw -= 1
        if draw == 0:
            over = True
            scores["draw"] += 1
            print_zone(zone, scores)
            print("The round is draw.")
    return over

mode = choose_mode(mode, end)

#2player
if mode == '1':
    while rematch == True:
        rematch = False
        zone = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ]
        x = 0
        y = 0

        #1 round
        while over != True:
            last = move
            print_zone(zone, scores)

            #placing the move
            choosing = True
            while choosing:
                valid_move = False
                while not valid_move:
                    move_xy = input(f"Where do you want to place '{move}' : ")  #getting a move
                    if move_xy.upper() in end:                                  #quitting if wanted
                        exit()
                    elif len(move_xy) == 2 and move_xy[0] in ["1","2","3"] and move_xy[1] in ["1","2","3"]:
                        valid_move = True
                    else:                                                       #invalid move
                        print_zone(zone, scores)
                        print("Invalid syntax. Correct form for placing your move is 'xy'\nx being the row, y being the column")
                    try:                                                        
                        move_xy = int(move_xy)                                  #checking valid move
                    except:
                        print_zone(zone, scores)
                        print("Invalid syntax. Correct form for placing your move is 'xy'\nx being the row, y being the column")
                x = int(str(move_xy)[0])-1                         #placing the move into the zone if the choosen cell is available
                y = int(str(move_xy)[1])-1
                if zone[x][y] == " ":                              #finalizing move
                    zone[x][y] = move
                    choosing = False
                else:                                              #cell not available
                    print_zone(zone, scores)
                    print("That cell is already occupied, please choose again")   
                    valid_move = False

            scanning(vektors)
            over = winning(vektors, over)
            over = draw(over)
            scoring()

            #next move
            if last == "X":
                move = "O"
            else:
                move = "X"

        #starting next round
        while not rematch:
            answer = input("Do you want to play another round?\n   yes -> Y\n   no -> N\n")
            if answer.upper() == "Y":
                rematch = True
                over = False
            elif answer.upper() == "N" or answer.upper() in end:
                exit()

#vs easy bot
elif mode == "2":
    print("easy bot coming soon")

#vs expert bot
elif mode == "3":
    print("expert bot coming soon")
