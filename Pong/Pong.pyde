#global variables
rad = 30
rectSize = 200
xSpeed = 4.8
ySpeed = 4.2
x = 600
y = 350
opponentY = 350
opponentSpeed = 7
playerScore = 0
opponentScore = 0
reset = False

def setup():
    size(1200, 700)
    noCursor()
    
def draw():
    global rad, rectSize, xSpeed, ySpeed, x, y, opponentY, opponentSpeed, playerScore, opponentScore, reset
    
    background(0)
    
    #background details
    stroke(0,255,0)
    strokeWeight(7)
    fill(0)
    ellipse(600,350,150,150)
    line(600,0,600,700)
    
    #ball
    fill(255)
    noStroke()
    ellipseMode(RADIUS)
    ellipse(x, y, rad, rad)
    x += xSpeed
    y += ySpeed
    
    #player moves with mouse Y axis
    rect(width-35, mouseY-rectSize/2, 25, rectSize)
    
    rect(10, opponentY-rectSize/2, 25, rectSize)
    opponentY += opponentSpeed
    #opponent movement
    if(opponentY >= 600):
        opponentSpeed *= -1
    if(opponentY <= 100):
        opponentSpeed *= -1
    
    #bounce off of player and opponent paddle
    if(x > width-50 and x < width-20 and y > mouseY-rectSize/2 and y < mouseY+rectSize/2):
        xSpeed *= -1
    if(x < 55  and x > 5 and y > opponentY-rectSize/2 and y < opponentY+rectSize/2):
        xSpeed *= -1
    #bounce off of walls
    if(y > height - rad or y < rad):
        ySpeed *= -1
        
    textSize(42)
    text(playerScore, 1050, 75)
    text(opponentScore, 125, 75)
    
    #opponent scores
    if(x > 1215):
        x = 600
        y = 350
        opponentScore += 1
    #player scores
    if(x < -15):
        x = 600
        y = 350
        playerScore += 1
        
    
    textSize(80)
    if (opponentScore == 3):
        x = 600
        y = 350
        fill(255, 0, 0)
        text("You Lose!", 400, 350)
        textSize(30)
        text("(Press any key to Play Again)", 380, 425)
        
    if (playerScore == 3):
        x = 600
        y = 350
        fill("#D8F029")
        textSize(80)
        text("You Win!", 400, 350)
        textSize(30)
        text("(Press any key to Play Again)", 380, 425)
        
    #resets game
    if reset:
        playerScore = 0
        opponentScore = 0
        reset = False
        
def keyPressed():
    global reset
    reset = not reset
    
    
    
    
