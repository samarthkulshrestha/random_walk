import turtle
import random
from operator import add

def random_walk_two_d_draw(iters):
    wn = turtle.Screen()
    wn.bgcolor("#141414")
    wn.title("Random Walk")

    turtle.hideturtle()
    turtle.pencolor("#ffffff")
    turtle.width(1.5)

    o = [0, 0]

    # while True:               # infinite loop
    for i in range(iters):
        u = [random.choice([-10, 10]), random.choice([-10, 10])]
        k = list(map(add, o, u))
        x, y = k
        turtle.goto(x, y)
        o = k

def random_walk_one_d(iters):
    c = 0
    for j in range(iters):
        p = random.choice([-1, 0, 1])
        # print(f"{c}\t+-\t{p}")
        c += p
    return c

if __name__ == '__main__':
    # random_walk_two_d_draw(100)
    print(random_walk_one_d(100))
