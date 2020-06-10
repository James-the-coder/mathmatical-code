import turtle

def tree(branchLen,t):
    if branchLen > 0.0005:
        t.forward(branchLen)
        t.right(30)
        tree(branchLen-5,t)
        t.left(60)
        tree(branchLen-5,t)
        t.right(30)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("black")
    tree(50,t)
    screen.exitonclick()

main()



    

