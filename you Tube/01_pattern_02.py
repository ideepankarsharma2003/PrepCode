import turtle as t
import math as m
t.speed(0)
t.bgcolor('black')
t.left(90)
t.forward(60)
t.right(90)
for i in range(300):
    t.pencolor('cyan')
    if(i>50 and i<100):
        t.pencolor('yellow')
    if(i>100 and i<150):
        t.pencolor('orange')
    if(i>150 and i<200):
        t.pencolor('magenta')
    if(i>200 and i<500):
        t.pencolor('green')

    t.fd(i)
    t.rt(68)
    t.fd(i)
    t.rt(78)
    t.bk(i)
    t.rt(79)
    t.fd(i)
    t.lt(43)
    t.rt(90)
t.done()
