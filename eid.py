import turtle as t
import random as r
from typing import Text

def star():
    t.left(90)
    t.forward(99)
    t.pencolor('#d4ad4c')
    t.begin_fill()
    for i in range(5):
        t.color('#d4ad4c')
        t.forward(51)
        t.left(144)
    t.end_fill()

t.pen(pensize=5, pencolor='#d4ad4c')
t.bgcolor('#000000')
t.up()
t.goto(-50, 15)
t.down()
t.begin_fill()
t.color('#d4ad4c')
t.circle(120)
t.end_fill()

t.up()
t.goto(-20, 25)
t.down()
t.begin_fill()
t.color('#000000')
t.circle(120)
t.end_fill()

star()

# Eid Mubarak

for i in range(10):
    Text = 'Eid Mubarak'
    # text print in down side of the star
    t.up()
    t.goto(-100, -100)
    t.down()
    t.pencolor('#d4ad4c')
    t.write(Text, font=('Arial', 30, 'bold'))
    t.up()


t.done()


