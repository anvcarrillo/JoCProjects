# Turtle Party Project
# by Andrea Carrillo
# 10/16/2023

import turtle
turtle.color("red")

# Main functions
def back(dist):
  turtle.penup()
  turtle.backward(dist)
  turtle.pendown()
def move(dist):
  back(dist*(-1))  
def polygon(numSides, lenSide):
  if (numSides >= 3):
    for i in range(numSides):
      turtle.forward(lenSide)
      turtle.left(360/numSides)
  else:
    print("Polygons must have at least 3 sides") 

## Figure with certer-drawn incremental size polygons  
for i in range(3,10):
  polygon(i, 20)
  turtle.left(360/7)

## Circle with clean separated polygons  
for i in range(3,10):
  move(50)
  polygon(i, 100/i)
  back(50)
  turtle.left(360/7)
    
## Spiral
def spiral(l, a):
  for i in range(l, 2, -5):
    turtle.forward(i)
    turtle.right(a)
  
spiral(75,45)
move(20)
turtle.color("blue")
spiral(90,90)
