def setup():
    global screen, lat, longt
    screen = 500
    lat = 1000
    longt = 1000
 
    global count
    count = [0,0, 0]
    
    global marathon
    marathon = []
    size(1000, 1000)
    background(0)


class Walker:
    def __init__(self, pos_x, pos_y, r, g, b):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel = 1
        self.age = 0
        self.cor_r = r
        self.cor_g = g
        self.cor_b = b
        self.sizeBall = 10
        self.id = str(pos_x) + str(pos_y) + str(random(1000)) + str(len(marathon))

        
    def show(self): 
        fill(self.cor_r/2, self.cor_g/2, self.cor_b/2, 120)
        stroke(self.cor_r, self.cor_g, self.cor_b, 120)
        ellipse(self.pos_x, self.pos_y, self.sizeBall, self.sizeBall)
    
    def randomMove(self):
        rnd_x = int(random(-2, 2))
        rnd_y = int(random(-2, 2))
        
        while rnd_x == 0:
           rnd_x = int(random(-2, 2))
        
        while rnd_y == 0:
           rnd_y = int(random(-2, 2))
           
    
        if self.defeatEnemy(rnd_x, rnd_y):
            self.sizeBall += 1
 
    
        if 0 < self.pos_x + (rnd_x * self.vel)< 1000:
            self.pos_x += rnd_x * self.vel
        
        if 0 < self.pos_y + (rnd_y * self.vel) <1000:
            self.pos_y += rnd_y * self.vel
        
        self.age += 1
        
    def defeatEnemy(self, newX, newY):
        futureX = self.pos_x + newX
        futureY = self.pos_y + newY
        res = False
        for index, item in enumerate(marathon):
            if self.id != item.id and self.sizeBall >= item.sizeBall:
                if self.findHip(item.pos_x, item.pos_y) <= self.sizeBall/1.8:
                    #print("kill 1 of {}".format(len(marathon)))
                    self.sizeBall += item.sizeBall
                    marathon.pop(index)
                    res = True
                            
        return res
    
    def findHip(self, item_x, item_y):
        catetos = [abs(self.pos_x - item_x), abs(self.pos_y - item_y)]
        catSomados =int(catetos[0]**2 + catetos[1]**2)
        return sqrt(catSomados)
          
        
    def check_age(self):
        if self.age % 100000 == 0:
            #x, y, r, g, b = self.pos_x, self.pos_y,self.r, self.g, self.b
            #marathon.append(Walker(x, y, r, g, b))
            self.age = 0
            self.sizeBall *= 2
            
    def where_am_i(self):
        print("x: {}\ny: {}".format(self.pos_x, self.pos_y))


def draw():
    background(255)
    if mousePressed:
        r, g, b = int(random(255)), int(random(255)), int(random(255))
        marathon.append(Walker(mouseX, mouseY, r, g, b))
    
    for item in marathon:
        item.show()
        item.randomMove()
        #item.check_age()
        #print("current number of walker: {}".format(len(marathon)))
