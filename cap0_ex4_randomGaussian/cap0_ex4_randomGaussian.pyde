global max_x, max_y
max_x = 1000
max_y = 500

def setup():
    background(255)
    size(max_x, max_y)
    
    
def draw():
    global max_x
    global max_y
    stroke(0)
    
    line(max_x/2, 0, max_x/2, max_y)
    line(0, max_y/2, max_x, max_y/2)
    
    stroke(int(random(1)*255),int(random(1)*255),int(random(1)*255),50)
    fill(int(random(1)*255),int(random(1)*255),int(random(1)*255),10)
    circle(max_x/2 + (randomGaussian() * max_x/10), max_y/2 + (randomGaussian()* max_y/10), 25)
        
