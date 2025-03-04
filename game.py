class Square():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.side_right = ""
        self.side_left = ""
        self.side_top = ""
        self.side_bottom = ""
    
SIZE = 4
PLAYBOARD = []

def init_playboard():
    global PLAYBOARD
    for y in range(SIZE):
        line = []
        for x in range(SIZE):
            line.append(Square(x,y))
        PLAYBOARD.append(line)

def show(PLAYBOARD):
    for line in PLAYBOARD:
        sentence = ""
        for square in line:
            if square.side_top:
                sentence += "+ - "
            else:
                sentence += "+   "
        print(f"{sentence}+")
        sentence=""
        for square in line:
            if square.side_left:
                sentence += "|   "
            else:
                sentence += "    "
        if line[-1].side_right:
            sentence += "|"
        print(sentence)
    for square in PLAYBOARD[-1]:
        sentence = ""
        for square in line:
            if square.side_bottom:
                sentence += "+ - "
            else:
                sentence += "+   "
    print(f"{sentence}+")

init_playboard()

def play(player,x,y,side):
    global PLAYBOARD
    if side == "R":
        try:
            PLAYBOARD[y][x].side_right = player
            PLAYBOARD[y][x+1].side_left = player
        except:
            pass
    elif side == "L":
        try:
            PLAYBOARD[y][x].side_left = player
            PLAYBOARD[y][x-1].side_right = player
        except:
            pass
    elif side == "T":
        try:
            PLAYBOARD[y][x].side_top = player
            PLAYBOARD[y-1][x].side_bottom = player
        except:
            pass
    else:
        try:
            PLAYBOARD[y][x].side_bottom = player
            PLAYBOARD[y+1][x].side_top = player
        except:
            pass
    
    show(PLAYBOARD)

play("A",0,0,"T")