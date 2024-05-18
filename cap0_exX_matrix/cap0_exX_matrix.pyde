global mx, my, char_size, cols, chance, maxColumn, count, rowControl
mx, my = 500, 500
colunas = 30
chance = 0.90
char_size = my /colunas
maxColumn = 10
rows = []
count = 0
rowControl = []

for i in range(0,mx / char_size):
    rowControl.append(0)

def setup():
    size(mx, my)
    background(0)

def getRandomChar():
    global chance
    chars = "abcdefghijklmnopqrstuvwyxz0123456789#!#$%^&*()_+=,./:;'[]\\"
    letter = chars[(int(random(0, len(chars))))]
    
    return letter.upper() if random(1) >= chance else letter
    
def randomArr(leng):
    global chance, rowControl, maxColumn
    newArr = []
    
    for i in range(0, leng):
        if random(1) > chance and rowControl[i] < maxColumn :
            rowControl[i] += 1
            newArr.append(getRandomChar())   
        else:
            newArr.append(" ")

    return newArr
               
def draw():
    global test, mx, my, rows, count, char_size

    fill(0,0,0, 20)
    rect(0, 0, mx,my)
    textSize(char_size)
    fill(255,255,255)

    if count == 0:
        rows.insert(0, randomArr(int(mx/char_size)))
        count = 3
        
        for index, value in enumerate(rows):
            for i, v in enumerate(value):
                text(v, i * char_size, index * char_size)
                if v != " ":
                    rows[index][i] = getRandomChar()
                
        if len(rows)> int(my /char_size):
            for index, item in enumerate(rows.pop(len(rows) - 1)):
                if item != " ":
                    rowControl[index] -= 1            
    else:
        count -= 1
