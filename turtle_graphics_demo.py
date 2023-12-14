import turtle as t
import random

# Please comment and uncomment the blocks to run the turtle graphics properly. Please check the recorded sessions on Youtube
#t.delay(100)  
timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.backward(200)
timmy_the_turtle.right(90)
timmy_the_turtle.left(180)
timmy_the_turtle.setheading(0)

####### Draw a Square ############
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
    
########### Draw a Dashed Line ########
tim = t.Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    

########### Draw circle ########
radius of circle
r = 50
tim.circle(r) 

#radius of smallet circle
r1=10
# number of circles 
n = 10
  
# loop for printing tangent circles 
for i in range(1, n + 1, 1): 
    t.circle(r1 * i) 
    
########### Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)
    
screen = t.Screen()
screen.exitonclick()