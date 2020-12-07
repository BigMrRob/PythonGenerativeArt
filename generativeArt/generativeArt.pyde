#Global Variables
x = 300
y = 300
angle = 0.0
endPoint = 20

def setup():
    size(900, 900)
    this.surface.setLocation(987, 70)
    
def draw():
    start_animation()
        
#This starts an animation using an animation method known as generative art.
def start_animation():
    global angle
    global x
    global y
    global endPoint
    background(0)
    
    #This takes care of the rotation of our values
    translate(width/2, height/2)
    #We use radians in combination with our angle to get a smooth experience
    rotate(radians(angle / 3))
    #Our range is set to 360 for full rotation
    for i in range(1, 360, 10):
        #Reset the origin
        pushMatrix()
        rotate(radians(i));
        stroke(255)
        strokeWeight(3)
        line(x * sin(radians(angle)), 0, x, y);
        noStroke()
        fill(255)
        ellipse(x*sin(radians(angle)), 0, endPoint / 2, endPoint / 2);
        stroke(255)
        noFill()
        ellipse(0, y, endPoint, endPoint)
        popMatrix()
    angle = angle + 1
    
