#Free_Palestine
#developed By @Kaylid
from turtle import *

#تقدر تغير السرعة بس انا ما افضلها 
speed(0)
setup(800,400)
penup()
goto(-400,200)
pendown()

#recangle 1
 
color("black")
begin_fill()
forward(800)
right(90)
forward(133)
right(90)
forward(800)
right(180)
end_fill()

#recangle 2

color("white")
begin_fill()
forward(800)
right(90)
forward(133)
right(90)
forward(800)
right(180)
end_fill()

#recangle3
 
color("green")
begin_fill()
forward(800)
right(90)
forward(133)
right(90)
forward(800)
right(180)
end_fill()

#triangle
 
color("red")
begin_fill()
goto(-200,20)
left(320)
forward(-400)
end_fill()

mainloop()