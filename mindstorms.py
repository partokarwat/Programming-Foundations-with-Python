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

def draw_two_triangles(some_turtle, edge_length):
    some_turtle.color("blue", "green")
    some_turtle.begin_fill()
    draw_triangle(some_turtle, edge_length)
    some_turtle.end_fill()
    some_turtle.color("blue", "white")
    some_turtle.forward(edge_length/2)
    some_turtle.left(60)
    some_turtle.begin_fill()
    draw_triangle(some_turtle, edge_length/2)
    some_turtle.end_fill()
    some_turtle.right(60)

def draw_small_triangles_part(some_turtle, edge_length):
    draw_two_triangles(some_turtle, edge_length) 
    draw_two_triangles(some_turtle, edge_length/2)
    some_turtle.backward(edge_length*3/4)
    draw_two_triangles(some_turtle, edge_length/2)
    some_turtle.backward(edge_length/4)
    some_turtle.left(60)
    some_turtle.forward(edge_length/2)
    some_turtle.right(60)
    draw_two_triangles(some_turtle, edge_length/2)    

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.fillcolor("green")
    brad.speed(10)

    draw_two_triangles(brad, 200)
    
    draw_small_triangles_part(brad, 100)

    brad.backward(25)
    brad.left(60)
    brad.backward(50)
    brad.right(60)
    brad.backward(100)
    draw_small_triangles_part(brad, 100)

    brad.backward(25)
    brad.left(60)
    brad.forward(50)
    brad.right(60)
    draw_small_triangles_part(brad, 100)

    brad.fillcolor("green")
    window.exitonclick()
    
    
draw_art()
