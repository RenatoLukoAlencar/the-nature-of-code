global max_x, max_y,angle
max_x = 600
max_y = 600
angle=0
def setup():
    size(max_x, max_y)
    background(255,0,0)
    
    
class Quad:
    def __init__(self, x, y, s, angle, speed):
        self.pos_x = x
        self.pos_y = y
        self.s = s
        self.angle = 0
        self.speed = speed
        

global quads
quads = []
for i in range(30):
    t = 20
    quads.insert(0,Quad(0 -(t*i/2), 0 - (t*i/2), t*i, i, 15 - i))
    
def draw():
    global max_x, max_y,angle
    background(255,0,0)
    
    fill(255,0,0)
    translate(max_x/2, max_y/2)
    strokeWeight(5)
    
 
    for quad in quads:
        rotate(radians(quad.angle))
        square(quad.pos_x, quad.pos_y, quad.s )
        quad.angle += 0.05
        
