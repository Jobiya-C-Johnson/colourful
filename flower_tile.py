# -*- coding: utf-8 -*-
"""
Created on Sat May 22 21:21:50 2021

@author: jobiya

"""

from turtle import *
color("yellow","")
circle(100)
color("green","")
left(90)
left(5)
while True:
    forward(200)
    right(170)
    if abs(pos()) < 1:
        break
color("violet","")
left(10)
while True:
    forward(200)
    right(150)
    if abs(pos()) < 1:
        break
color("pink","")
right(10)
while True:
    forward(200)
    right(165)
    if abs(pos()) < 1:
        break
color("orange","")
right(15)
while True:
    forward(200)
    right(200)
    if abs(pos()) < 1:
        break
done()


