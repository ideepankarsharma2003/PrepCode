import turtle as t
import math as m
t.speed(0)
t.bgcolor('black')
t.left(90)
t.forward(60)
t.right(90)
for i in range(409):
    t.pencolor('cyan')
    t.fd(i)
    t.rt(68)
    t.fd(i)
    t.rt(78)
    t.bk(i)
    t.rt(79)
    t.fd(i)
    t.lt(155)
    t.rt(90)
t.done()
