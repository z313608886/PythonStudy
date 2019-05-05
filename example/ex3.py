import turtle
import math
'''def polygon(t,d,n):
    for i in range(n):
        t.fd(d)
        t.lt(360/n)'''  #画多边形
def arc(t,d,n):
    for i in range(n):  #画弧
        t.fd(d)
        t.lt(360/100)

bob= turtle.Turtle()


r=100
d=2*math.pi*r/100
int(d)
angle=180
n=angle/360*100
n=round(n)
arc(bob,d,n)
turtle.mainloop()
