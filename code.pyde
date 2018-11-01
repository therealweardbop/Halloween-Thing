import random
class candy(object):  # Class definition
  def __init__(self, xloc):  # Object constructor
    self.xloc = xloc
    self.yloc = 0

  def display(self):  # Display method
    ellipse(self.xloc, self.yloc, 20, 20)
    triangle(self.xloc, self.yloc, self.xloc+20, self.yloc-10, self.xloc+20, self.yloc+10)
    triangle(self.xloc, self.yloc, self.xloc-20, self.yloc-10, self.xloc-20, self.yloc+10)
def setup():
    size(800,600)
    
xpos = 0
candies = []
counter = 0
score = 0
increments = 1
prev = 400
gameover = False
strikes = 0
maxc = 40

def draw():
    x = 0
    global gameover
    global maxc
    global score
    global xpos
    global candies
    global counter
    global increments
    global prev
    global strikes
    background(0,40,80)
    noStroke()
    fill(0,150,0)
    rect(0,550,800,50)
    fill(255,255,200)
    ellipse(100,100,50,50)
    fill(0,40,80)
    ellipse(110,100,50,50)
    if strikes >= 4:
        gameover = True
    if gameover == True:
        textSize(32)
        fill(250, 250, 250)
        text("Final Score: "+ str(score), 265, 300)
    else:
        for i in range(strikes):
            stroke(250, 0, 0)
            strokeWeight(10)
            line(40,300 +i*50-10, 60,300+i*50+10)
            line(40,300 +i*50+10, 60,300+i*50-10)
            noStroke()
        if keyPressed == True:
            if key == 'd':
                x = 8
            if key == 'a':
                x = -8
        xpos += x
        fill(250,100,0)
        rect(xpos,450,50,50)
        ellipse(xpos + 25,500,50,75)
        fill(255,150,0)
        counter += 1
        
        if counter >= maxc:
            counter = 0
            #if increments > 6:
            #    increments += random.random()*8-5
            #else:
            #    increments += random.random()*3-1
            increments += 0.5
            if maxc > 10:
                maxc-=0.5
        if counter == 1:
            a = 1
            for i in range(a):
                candies.append(candy(prev))
                while True:
                    a = floor(random.random()*(maxc*4))-maxc*2
                    if not(prev + a < 100 or prev + a > 700):
                        break
                prev += a
        for i in candies:
            i.yloc +=increments
            i.display()
            if i.yloc >=440 and i.yloc <= 550 and i.xloc+20 > xpos and i.xloc-20 < xpos + 50:
                candies.remove(i)
                score += 1
            if i.yloc >=610:
                strikes += 1
                candies.remove(i)
        textSize(32)
        fill(250, 250, 250)
        text("Missed\nCandies", 10, 220)
        text("Candies Collected: "+ str(score), 430, 50)
        
