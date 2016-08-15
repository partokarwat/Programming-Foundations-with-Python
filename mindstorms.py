import turtle

def draw_square(some_turtle):
    for i in range (0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle, edge_length):
    for i in range (0,3):
        some_turtle.forward(edge_length)
        some_turtle.left(120)

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

    brad.left(90)
    brad.forward(200)
    brad.backward(100)
    brad.right(45)
    brad.forward(150)
    brad.backward(150)
    brad.right(80)
    brad.forward(150)
    brad.backward(150)
    brad.right(55)
    brad.forward(100)
    brad.left(90)
    brad.penup()
    brad.forward(150)
    brad.pendown()
    brad.left(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(100)
    brad.back(100)
    brad.right(90)
    brad.forward(200)
    brad.left(90)
    brad.forward(100)

 
    window.exitonclick()
    
    
draw_art()
