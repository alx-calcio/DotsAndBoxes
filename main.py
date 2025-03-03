class Square():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.side_right = ""
        self.side_left = ""
        self.side_top = ""
        self.side_bottom = ""
    
size = 10
playboard = []

def init_playboard():
    global playboard
    for y in range(size):
        line = []
        for x in range(size):
            line.append(Square(x,y))
        playboard.append(line)

def show(playboard):
    for line in playboard:
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
    for square in playboard[-1]:
        sentence = ""
        for square in line:
            if square.side_bottom:
                sentence += "+ - "
            else:
                sentence += "+   "
    print(f"{sentence}+")

init_playboard()

def play(player):
    global playboard
    x, y = map(lambda x: int(x), input().split())
    side = input("R, L, T, B")
    if side == "R":
        try:
            playboard[y][x].side_right = player
            playboard[y][x+1].side_left = player
        except:
            pass
    elif side == "L":
        try:
            playboard[y][x].side_left = player
            playboard[y][x-1].side_right = player
        except:
            pass
    elif side == "T":
        try:
            playboard[y][x].side_top = player
            playboard[y-1][x].side_bottom = player
        except:
            pass
    else:
        try:
            playboard[y][x].side_bottom = player
            playboard[y+1][x].side_top = player
        except:
            pass
    
    show(playboard)