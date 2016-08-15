import turtle

def draw_square(some_turtle):
    for i in range (0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle, edge_length):
    some_turtle.begin_fill()
    for i in range (0,3):
        some_turtle.forward(edge_length)
        some_turtle.left(120)
    some_turtle.end_fill()

def draw_diamond(some_turtle):
    some_turtle.left(45)
    some_turtle.forward(100)
    some_turtle.right(45)
    some_turtle.forward(100)
    some_turtle.right(135)
    some_turtle.forward(100)
    some_turtle.right(45)
    some_turtle.forward(100) 

def draw_small_triangles(some_turtle):
    draw_triangle(some_turtle, 50)
    some_turtle.right(60)
    some_turtle.forward(25)
    some_turtle.left(60)
    draw_triangle(some_turtle, 25)
    some_turtle.forward(25)
    some_turtle.left(60)
    some_turtle.forward(25)
    some_turtle.left(60)
    some_turtle.forward(25)
    some_turtle.right(120)
    draw_triangle(some_turtle, 25)
    some_turtle.left(120)
    some_turtle.forward(25)
    some_turtle.left(60)
    some_turtle.forward(50)
    some_turtle.left(120)
    some_turtle.forward(25)
    some_turtle.left(60)
    draw_triangle(some_turtle, 25)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.fillcolor("green")
    brad.speed(5)

    brad.begin_fill()
    draw_triangle(brad, 200)
    brad.end_fill()

    brad.color("blue", "white")
    brad.forward(100)
    brad.left(60)
    draw_triangle(brad, 100)
    brad.forward(100)
    brad.left(120)
    brad.forward(50)
    brad.right(120)
    draw_small_triangles(brad)

    brad.left(120)
    brad.forward(25)
    brad.left(60)
    brad.forward(100)
    brad.left(120)
    brad.forward(50)
    brad.left(60)
    draw_small_triangles(brad)

    brad.right(60)
    brad.forward(125)
    brad.left(60)
    draw_small_triangles(brad)

    brad.right(60)
    brad.forward(25)    

    brad.fillcolor("green")
    window.exitonclick()
    
    
draw_art()
