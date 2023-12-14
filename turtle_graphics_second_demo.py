import turtle as t
import random

# Please comment and uncomment the blocks to run the turtle graphics properly. Please check the recorded sessions on Youtube

tim = t.Turtle()
t.colormode(255)
t.bgcolor("black")
tim.speed("fastest")

########### Random Walk ###########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(300):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
    
########### Function To Get the RGB colors ###########
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
    

########### Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()