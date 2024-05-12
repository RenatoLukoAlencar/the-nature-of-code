global max_x, max_y
max_x = 600
max_y = 300

def setup():
    size(max_x, max_y)
    background(0)
    
class Walker:
    def __init__(self, x, y, self_size):
        self.x = x
        self.y = y
        self.s = self_size
        self.colorRgb = [random(255), random(255) , random(255)]
            
    def walk(self):
        
        step = random(1)

        if self.x < 580:
            if step < 0.35:
                self.x += 1
            elif step < 0.60:
                self.y += 1
            elif step < 0.85:
                self.y -= 1
            else:
                self.x -= 1
        else:
            if step < 0.10:
                self.x += 1
            elif step < 0.45:
                self.y += 1
            elif step < 0.80:
                self.y -= 1
            else:
                self.x -= 1
        
        
global walkers

walkers = [Walker(int(random(max_x)/3), max_y/2, 1)]

def mouseClicked():
    walkers.append(Walker(mouseX, mouseY, 1))


def draw():
    for item in walkers:
        fill(item.colorRgb[0], item.colorRgb[1], item.colorRgb[2])
        stroke(item.colorRgb[0], item.colorRgb[1], item.colorRgb[2])
        circle(item.x, item.y, item.s)
        item.walk()
