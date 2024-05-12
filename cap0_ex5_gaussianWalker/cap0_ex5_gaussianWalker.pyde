global max_x, max_y
max_x = 1000
max_y = 1000

def setup():
    size(max_x, max_y)
    background(255)
    
class GaussianWalker:
    def __init__(self, x, y, sizeWalker):
        self.x = x
        self.y = y
        self.s = sizeWalker
        self.p_x = x
        self.p_y = y
        self.rgb = [int(random(255)),int(random(255)),int(random(255))]
        
    def walk(self):
        self.p_x = self.x
        self.p_y = self.y
        newX = self.x + int(randomGaussian() * self.s)
        newY = self.y + int(randomGaussian() * self.s)
        self.x = newX if newX > 0 and newX < max_x else self.x
        self.y = newY if newY > 0 and newY < max_y else self.y   
        
        for index, value in enumerate(self.rgb):
            self.rgb[index] += randomGaussian() * 3
            
        

global walkers
walkers = [GaussianWalker(max_x/2, max_y/2, 5)]


def draw():
    for walker in walkers:
        fill(walker.rgb[0],walker.rgb[1], walker.rgb[2] )
        stroke(walker.rgb[0],walker.rgb[1], walker.rgb[2] )
        strokeWeight(2)
        line(walker.x, walker.y, walker.p_x, walker.p_y)
        walker.walk()
        
def mouseClicked():
    global walkers
    walkers.append(GaussianWalker(mouseX, mouseY, 5))
        
    
