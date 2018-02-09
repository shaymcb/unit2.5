#Shaylee McBride
#8Feb2018
#house.py - makes a house

from ggame import *

gold = Color(0xF2DE5A, 1)
white = Color(0xFFFFFF, 1)
black = Color(0x000000, 1)

goldOutline = LineStyle(1,gold)
whiteOutline = LineStyle(1,white)
blackOutline = LineStyle(2,black)

bigRectangle = RectangleAsset(570,300,goldOutline,gold)
eraseBig = RectangleAsset(270,100,whiteOutline,white)
eraseLittle = RectangleAsset(30,20,whiteOutline,white)
door = EllipseAsset(150,200,whiteOutline,white)
text = TextAsset("My house is a castle",fill=black,style="bold italic 40pt Times")

Sprite(bigRectangle)
Sprite(eraseBig, (150,0))
Sprite(eraseLittle, (30,0))
Sprite(eraseLittle, (90,0))
Sprite(eraseLittle, (30,0))
Sprite(eraseLittle, (90,0))
Sprite(eraseLittle, (450,0))
Sprite(eraseLittle, (510,0))
Sprite(eraseLittle, (180,100))
Sprite(eraseLittle, (240,100))
Sprite(eraseLittle, (300,100))
Sprite(eraseLittle, (360,100))
Sprite(door, (570/2-150,200))
Sprite(text, (10,50))


App().run()