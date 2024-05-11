global w, h, y_line, qtdBars, arr_bars
w = 500
h = 500
y_line = h
qtdBars = 20
widthBars = w/qtdBars

class Bar:
    def __init__(self, self_w, self_h, self_color):
        self.w = self_w
        self.h = self_h + 10
        self.bcolor = self_color
        
    def grow(self):
        if int(random(5)) == 1:
            self.h += 1
            
        if self.h > y_line:
            self.bcolor = 240        

arr_bars = [Bar(widthBars, 1, 50) for i in range(0, qtdBars)]

def setup():
    size(w, h)

def draw():
    line(0, h - y_line, w, h - y_line)
    stroke(200, 0, 0)
    
    for index, bar in enumerate(arr_bars):
        bar.grow()
        fill(bar.bcolor)
        rect(0 + (index * bar.w), h - bar.h, bar.w, bar.h )
        if bar.h > y_line:
            noLoop()
            
def mouseClicked():
    global y_line
    y_line = h - mouseY
