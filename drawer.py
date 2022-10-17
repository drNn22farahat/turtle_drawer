import random
import turtle as t
colors = ['red','cyan','pink','yellow','green','orange','indigo','violet','white','brown','beige','grey']
t.speed(50)
t.bgcolor('black')
length=4
angle=50
size=10
for i in range(length):
    color=random.choice(colors)
    t.pencolor(color)
    t.fillcolor(color)
    t.right(90)   
    t.forward(120)
   
    t.left(100)
    t.forward(100)
    t.left(100)
    t.forward(100)
    t.begin_fill()
t.exitonclick() 
