import turtle

def draw_square(some_turtle):
    
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)
    

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    brad = turtle.Turtle()
    count = 0
    brad.shape("turtle")
    brad.speed(10)
    for i in range(1,36):
        
        draw_square(brad)
        brad.right(10)
    
    window.exitonclick()

draw_art()
    
    
