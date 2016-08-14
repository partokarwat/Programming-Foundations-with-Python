import turtle

def draw_square(some_turtle):
    for i in range (0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range (0,3):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_diamond(some_turtle):
    some_turtle.left(45)
    some_turtle.forward(100)
    some_turtle.right(45)
    some_turtle.forward(100)
    some_turtle.right(135)
    some_turtle.forward(100)
    some_turtle.right(45)
    some_turtle.forward(100) 

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(10)

    for i in range (0,36):
        draw_diamond(brad)
        brad.right(10)

    brad.right(90)
    brad.forward(300)
    
    window.exitonclick()
    
    
draw_art()
