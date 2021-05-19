import turtle

t = turtle.Pen()
t.speed('fastest')

def square():
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)

def tifufu(x,y):

    t.pensize()
    t.pencolor("red")

    t.up()
    t.goto(x,y)
    t.down()
    # T
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.right(90)
    t.forward(100)

    # I

    t.pencolor("orange")
    radius = 15

    t.up()
    t.forward(25)
    t.down()
    t.right(90)
    t.forward(100)
    t.left(180)
    t.forward(100)
    t.up()
    t.forward(50)
    t.right(90)
    t.forward(radius)
    t.right(-90)
    t.down()
    t.circle(radius,360)
    t.up()

    t.left(180)
    t.forward(150)

    t.down()


    # F

    t.pencolor("yellow")

    t.up()
    t.left(90)
    t.forward(25)
    t.down()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.left(180)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    # U

    t.pencolor("green")

    t.up()
    t.forward(25)
    t.down()
    t.left(90)
    t.forward(50)
    t.left(180)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    # F

    t.pencolor("blue")

    t.up()
    t.right(90)
    t.forward(25)
    t.down()
    t.forward(50)
    t.left(180)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(180)
    t.forward(50)
    t.left(90)
    t.forward(50)
    # U

    t.pencolor("purple")

    t.up()
    t.left(90)
    t.forward(75)
    t.down()
    t.left(90)
    t.forward(100)
    t.left(180)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    # FRAME

    t.pencolor("black")

    t.up()
    t.forward(25)
    t.down()
    t.left(90)
    t.forward(450)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(500)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(50)
    t.setheading(0)


tifufu(-50,-50)
#tifufu(-200,-200)



while 1:
    pass