global arr
arr = []

def setup():
    size(500, 500)
    
    
    
value = 0

def draw():
    fill(0)
    stroke(0)
    
    if len(arr) == 3:
        for index, value in enumerate(arr):
            next = arr[0]
            
            if index != len(arr) - 1:
                next = arr[index + 1]
        
            line(value[0], value[1], next[0], next[1])



def mouseClicked():
    if len(arr) is not 3:
        arr.append([mouseX, mouseY])
        ellipse(mouseX, mouseY, 3,3) 
    
