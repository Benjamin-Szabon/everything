import random

over = False
move_xy = 0
move = ""
last = ""
zone = [[{"null": True, "xy": 11, "cell": " "}, {"null": True, "xy": 12, "cell": " "}, {"null": True, "xy": 31, "cell": " "},], 
        [{"null": True, "xy": 21, "cell": " "}, {"null": True, "xy": 22, "cell": " "}, {"null": True, "xy": 32, "cell": " "},], 
        [{"null": True, "xy": 31, "cell": " "}, {"null": True, "xy": 13, "cell": " "}, {"null": True, "xy": 33, "cell": " "},] ]
x = 0
y = 0
draw = 9
vektor_x = 0
vektor_y = 0
vektor_wx = 0
vektor_wy = 0

#1 round
move = random.choice(["X","O"])
while over != True:
    last = move

    #print out the zone
    print("-1-2-3-")
    for n in range(3):
        for n2 in range(3):
            print(f"|{zone[n][n2]['cell']}", end="")
        print(f"| {n+1}\n---------")

    #placing the move
    choosing = True
    while choosing == True:
        move_xy = int(input(f"Where do you want to place '{move}' :"))
        x = int(str(move_xy)[0])-1
        y = int(str(move_xy)[1])-1
        if zone[x][y]["null"] == True:
            zone[x][y]["cell"] = move
            zone[x][y]["null"] = False
            choosing = False
        else:
            print("That cell is already occupied")

    #winning
    for v in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        vektor_x = v[0]
        vektor_y = v[1]
        try:
            if zone[x+vektor_x][y+vektor_y]["cell"] == move:
                vektor_wx = vektor_x
                vektor_wy = vektor_y
                try:
                    if zone[x-vektor_wx-vektor_wx][y-vektor_wy-vektor_wy]["cell"] == move:
                        print(f"{move} won the round")
                        break
                except:
                    try:
                        if zone[x+vektor_wx+vektor_wx][y+vektor_wy+vektor_wy]["cell"] == move:
                            print(f"{move} won the round")
                            break
                    except:
                        pass
        except:
            pass


    #draw
    for n in range(3):
        for n2 in range(3):
            if zone[n][n2]['null'] == False:
                draw -= 1
            if zone[n][n2]['null'] == True:
                draw += 1
    if draw == 0:
        over = True
        print("-1-2-3-")
        for n in range(3):
            for n2 in range(3):
                print(f"|{zone[n][n2]['cell']}", end="")
            print(f"| {n+1}\n---------")
        print("The round is draw")

    #next move
    if last == "X":
        move = "O"
    else:
        move = "X"
