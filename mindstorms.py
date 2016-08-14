import turtle

def draw_square(some_turtle):
    for j in range (0,4):
        some_turtle.forward(100)
        some_turtle.right(90)



def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("yellow")
    brad.speed(10)

    for i in range (0,36):
        draw_square(brad)
        brad.left(10)
    window.exitonclick()
    
    
draw_art()
