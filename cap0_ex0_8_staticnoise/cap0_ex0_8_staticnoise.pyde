global mx, my
mx, my = 600, 400

def setup():
    size(mx, my)
    #background(150,30,100)
    
def draw():
    global mx, my
    loadPixels()
    test = 0.0
    xoff = 0.0
    for x in range(mx):
        yoff = 0.0
        for y in range(my):
            #n = random(255)
            i = (x + (y * width))
            n = map(noise(xoff,yoff,test), 0,1,0,255)
            gray = color(n, n, n)
            pixels[i] = gray
            yoff += 0.02
        #test += random(1)/500
        xoff += 0.02
    
            
    updatePixels()
    noLoop()

    


    
