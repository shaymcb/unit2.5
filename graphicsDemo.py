#Shaylee McBride
#7Feb2018
#graphicsDemo.py - intro to ggame

from ggame import *

red = Color(0xFF0000, 1) #hex code, opacity
green = Color(0x00FF00, 1)
blue = Color(0x0000FF, 1)
black = Color(0x000000, 1)

blackOutline = LineStyle(1,black) #first number is how many pixels wide

redRectangle = RectangleAsset(200,100,blackOutline,red) #width, height, outline, fill color
blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, fill

Sprite(redRectangle)
Sprite(blueCircle)
App().run()
