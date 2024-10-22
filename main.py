# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
tcolor = "red"
tsize = 4
tshape = "square"
#-----initialize turtle-----
t = trtl.Turtle()
t.shape(tshape)
t.shapesize(tsize)
t.fillcolor("red")

#-----game functions--------
def spot_clicked(x, y):
    print("you clicked it!")

def change_position():
    
   

#-----events----------------
wn = trtl.Screen()
t.onclick(spot_clicked)
wn.mainloop()

