import random
import turtle

bg_color = "black"
wn = turtle.Screen()
wn.bgcolor(bg_color)
draw_colors = ["red"]
t_amount = 5
ts = {}
starting_loc_offset = 0
inc_loc_offset = 1
alt_pos = 1
offset_adjust = 20

for i in range(t_amount):
    ts.update({i: turtle.Turtle()})

for v in ts:
    ts[v].hideturtle()
    ts[v].speed(0)
    ts[v].penup()
    if alt_pos:
        ts[v].goto(starting_loc_offset, 0)
        alt_pos = 0
    else:
        ts[v].goto(starting_loc_offset * -1, 0)
        alt_pos = 1
        inc_loc_offset = 0
    if inc_loc_offset:
        starting_loc_offset += t_amount * offset_adjust
    inc_loc_offset = 1
    ts[v].pendown()

rose = 0
petal_size = 52
while rose < 2:
    for steps in range(petal_size):
        for t in range(len(ts)):
            for c in draw_colors:
                ts[t].color(c)
                ts[t].forward(steps)
                if steps % 2 == 0:
                    ts[t].right(90)
                else:
                    ts[t].right(45)

    rose += 1
    petal_size -= 14

for t in range(len(ts)):
    ts[t].color("green")
    ts[t].penup()
    ts[t].right(45)
    ts[t].forward(63)
    ts[t].right(90)
    ts[t].forward(42)
    ts[t].pendown()
    ts[t].width(3)
    ts[t].forward(15)
    for i in range(random.randrange(20, 25)):
        ts[t].right(random.randrange(10))
        ts[t].forward(i)
        ts[t].left(random.randrange(10))

wn.exitonclick()
