global max_x, max_y, qtdBars, lenBar
max_x = 840
max_y = 300
qtdBars = 20
lenBar = (max_x / qtdBars)

def setup():
    size(max_x, max_y)
    background(255)

class Bar:
    def __init__(self, x, y, altura, rand):
        self.x = x
        self.y = y
        self.altura = altura
        self.rand = rand
    
    def grow(self):
         if self.rand-4 > qtdBars + int(randomGaussian()* qtdBars/2):
            self.altura += 1
            
global bars
bars = [Bar((lenBar*i), max_y, 10, i) for i in range(qtdBars)]

def draw():
    fill(100)
    stroke(0)
    strokeWeight(3)
    for bar in bars:
        if max_y > bar.altura:
            rect(bar.x, max_y - bar.altura, lenBar, bar.altura)
            bar.grow()
