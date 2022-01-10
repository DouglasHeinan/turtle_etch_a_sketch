from turtle import Turtle, Screen

THOMAS = Turtle()
SCREEN = Screen()


def main():
    SCREEN.listen()
    SCREEN.onkey(move, "w")
    SCREEN.onkey(left, "a")
    SCREEN.onkey(right, "d")
    SCREEN.onkey(back, "s")
    SCREEN.onkey(clear, "c")
    SCREEN.exitonclick()


def move():
    THOMAS.forward(5)


def left():
    THOMAS.left(5)


def right():
    THOMAS.right(5)


def back():
    THOMAS.backward(5)


def clear():
    SCREEN.reset()


if __name__ == "__main__":
    main()
