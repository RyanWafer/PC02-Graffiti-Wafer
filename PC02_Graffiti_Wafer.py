#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 13:57:43 2020

@author: ryanwafer
"""

#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Ryan Wafer
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos6.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)


#=======Add your code here======

# create Turtle
Turtle()
up()
goto(-18,114)

# left green eye
down()
dot(8,"green")
up()

# move
goto(42,120)

# right green eye
down()
dot(8,"green")
up()

# move
goto(250,-100)

# red shape
down()
color("red")
begin_fill()
forward(50)
right(50)
forward(60)
right(60)
forward(80)
right(100)
forward(80)
right(50)
forward(30)
end_fill()
up()

# move
goto(230,-120)
right(100)

# line
down()
color("orange")
pensize(10)
forward(120)

done()










