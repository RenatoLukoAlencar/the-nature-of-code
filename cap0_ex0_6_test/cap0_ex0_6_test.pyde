global max_x, max_y, dots
max_x = 750
max_y = 300


class Dot:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

dots = [Dot(max_x, max_y/2, [0, 255,0])]

def setup():
    size(max_x, max_y)
    background(0)
    
global t
t = 0

def draw():
    global t
    background(0)
    stroke(255,255,255,30)
    strokeWeight(1)
    space = 4
    
    
    
    for i in range(max_x/ 5):
        line(max_x/50 * i * space, 0, max_x/50*i * space, max_y )
        
    for i in range(max_y/5):
        line(0, max_y/50 * i * space*2, max_x, max_y/50*i * space * 2)
    
    

    for index, item in enumerate(dots):
        if index != len(dots)-1 and index >= 2:
            nexty = item.y        
            
            stroke(item.c[0], item.c[1], item.c[2],255)
            circle(item.x, item.y, 10)
            item.x -=1
            #line(dots[index-1].x, dots[index-1].y, item.x, nexty)
    
        item.x -= 1
    
    if len(dots) > max_x:
        dots.pop(0)   
    
    n = noise(t)
    newY = map(n, 0, 1, 0, max_y)
    c = [0,0,0]
    
    c[1] = 255 if newY < dots[-1].y else 0
    c[0] = 255 if newY > dots[-1].y else 0

    dots.append(Dot(max_x, newY, c))

    t += 0.01
        
    
 
    
    
