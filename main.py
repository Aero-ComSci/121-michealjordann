# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
tcolor = "red"
tsize = 4
tshape = "square"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False


#-----initialize turtle-----
t = trtl.Turtle()
t.shape(tshape)
t.shapesize(tsize)
t.fillcolor("red")
scwriter = trtl.Turtle()
counter =  trtl.Turtle()
counter.speed(0)
scwriter.speed(0)
t.speed(0)
#-----game functions--------
def spot_clicked(x, y):
    t.stamp()
    color = ["red","blue", "green", "orange", "purple","brown","yellow"]
    shape = ["turtle","classic","triangle","square"]
    t.color(rand.choice(color))
    t.shape(rand.choice(shape))
    change_position()
    counterpos()
   


def change_position():
    
    xnew = rand.randint(-360,260)
    ynew = rand.randint(-360,260)
    t.penup()
    t.goto(xnew,ynew)
    update_score()
    

def update_score():
    global score
    score += 1
    scwriter.penup()
    scwriter.goto(0,295)
    scwriter.clear()
    scwriter.write("Score:", font=font_setup)
    scwriter.goto(80,295)
    scwriter.write(score, font=font_setup)

def counterpos():
   t.penup()
   counter.goto(-300,295)
   

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    if timer_up == False:
       update_score()
       change_position()
    else:
       t.hideturtle()
       scwriter.hideturtle()
       counter.hideturtle()
        
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
    
 
   

#-----events----------------
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
t.onclick(spot_clicked)
wn.mainloop()

