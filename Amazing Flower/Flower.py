#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:42:32 2024

@author: risaluthor
"""

from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0
for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)    

 # ht(): Hide the turtle after drawing a circle
 # pu(): Move Pen to the next position
 # setpos(0, 0): Move to the center before drawing the next set of circles
 # pd(): Pen down to start next drawing                            