global max_x, max_y, lines, board, turn, winner, rgb
max_x, max_y = 600,600
lines = [[200,0,200, 600], [400, 0, 400, 600], [0, 200, 600, 200], [0,400, 600, 400]] 
board = [["", "", ""],["", "", ""],["","", ""]]
turn = "O"
winner = False
rgb = [124, 255, 0]

def drawIcon(x, y, icon):
    global rgb
    if icon == "O":
        fill(rgb[0],rgb[1],0)
        circle(x, y, 150)
    else:        
        line(x-80, y-80, x+80, y+80)
        line(x+80, y-80, x-80, y+80)
    
def mousePressed():
    global turn, board, rgb
    yIndex = 2 if mouseY >= 400 else 1 if mouseY > 200 and mouseY <400 else 0
    xIndex = 2 if mouseX >= 400 else 1 if mouseX > 200 and mouseX <400 else 0        
        
    if board[yIndex][xIndex] == "":       
        board[yIndex][xIndex] = turn
        checkWinners()
        turn = "X" if turn == "O" else "O"
    
def placeIcons():
    global board, turn 
    
    for yindex, row in enumerate(board):
        for xindex, col in enumerate(row):
            if col != "":                
                drawIcon((200*(xindex+1))-100, (200*(yindex+1))-100, col)

def checkWinners():
    global board, turn, winner, rgb
    winner = checkRows(board, turn) or checkCols(board, turn) or checkDiagonals(board, turn)
    rgb = [255,124,0] if winner else rgb
    
def checkRows(board, turn):
    for row in board:
        if row[0] == row[1] == row[2] == turn:
            return True
            
def checkCols(board, turn):
    for number in range(0,3):
        if board[0][number] == board[1][number] == board[2][number] == turn:
            return  True
            
def checkDiagonals(b, turn):
    return b[0][0] == b[1][1] == b[2][2] == turn or b[0][2] == b[1][1] == b[2][0] == turn
 
def setup():
    size(max_x, max_y)
        
def draw():   
    background(rgb[0], rgb[1], rgb[2])
    strokeWeight(10)
    placeIcons()    
    for seg in lines:
        line(seg[0], seg[1], seg[2], seg[3])

    if winner:
        noLoop()
    
        

        
        
        
    
