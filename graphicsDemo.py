#Shaylee McBride
#7Feb2018
#graphicsDemo.py - intro to ggame

from ggame import *

red = Color(0xFF0000, 1)
black = Color(0x000000, 1)

blackOutline = LineStyle(1,black) #first number is how many pixels wide

redRectangle = RectangleAsset(200,100,blackOutline,red) #width, height, outline, fill color

Sprite(redRecangle)
App().run()
