#libs
import math 
import turtle


def xt(t):
    return 17 * math.sin(t) ** 3

def yt(t):
    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * \
        math.cos(3 * t) - math.cos(4 * t)

t = turtle.Turtle()
t.speed(15500)
turtle.Screen().title('Heart - by Shanazar ❤')
turtle.colormode(255)
turtle.Screen().bgcolor('black')
#Drawing
for i in range(550):
    t.goto((xt(i) * 20, yt(i) * 20))
    t.pencolor((255 - i) % 255, i % 255, (255 + i) // 2 % 255)
    t.goto(0, 0)

#loop
if __name__=='__main__':
    t.hideturtle()
    turtle.update()
    turtle.mainloop() 