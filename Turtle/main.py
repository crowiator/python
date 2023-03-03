#Turtle graphics
from turtle import Screen, Turtle
import random
import turtle

#Zmena barevneho modu
turtle.colormode(255)
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(20)

#stvorec
# for move in range(1,5):
#     tommy.forward(60)
#     tommy.left(90)
#     tommy.dot()

#ciarkovana ciara
# for x in range(1,6):
#     tommy.pendown()
#     tommy.forward(10)
#     tommy.penup()
#     tommy.forward(10)
# colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue"]
# size =60
# tommy.pensize(3)
# for tvar in range(3,9):
#     position = random.randint(0, (len(colors)-1))
#     color = colors[position]
#     tommy.pencolor(color)
#     print(tvar)
#     uhol = 360 // tvar
#     print(uhol)
#     for strana in range(0,tvar):
#         tommy.forward(size)
#         tommy.right(uhol)
#     #size+=10   

#RANDOM WALK

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     #tupple
#     random_color = (r,g,b)
#     return random_color
# # colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue"]
# rotation = [0,90,180,270]
# speed = 1

# for number in range(200):
#     #nahodny vyber farby
#     color= random_color()
#     tommy.pencolor(color)

#     #hrube ciary
#     if number <=10:
#         tommy.pensize(number)
#     #pohyb a nahodne otocenie
#     tommy.forward(40)
#     tommy.right(random.choice(rotation))
    
#     #zvysujeme rychlost
#     tommy.speed(speed)
#     speed +=2



#spriograf


# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     #tupple
#     color = (r,g,b)
#     return color
# def spirograph(gap):
#     for x in range(int(360/ gap)):
#         tommy.pencolor(random_color())
#         tommy.circle(80)
#         tommy.right(gap)

# spirograph(2)

my_screen = Screen()
my_screen.bgcolor("grey")
my_screen.exitonclick()