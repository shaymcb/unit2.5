#Shaylee McBride
#9Feb2018
#name.py - input name & fav color, get cool screen

from ggame import *

name = input("What is your name? ")
color = input("What is your favorite color's hex code (no 0x)? ")

fillColor = Color('0x'+color,1)

outline = LineStyle(0,fillColor)

rectangle = RectangleAsset(1080,580,outline,fillColor)
text = TextAsset(name,fill=Color(0x000000,1),style="bold 50pt Courier")

Sprite(rectangle)
Sprite(text,(350,250))
App().run()
