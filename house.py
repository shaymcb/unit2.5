#Shaylee McBride
#8Feb2018
#house.py - makes a house

from ggame import *

gold = Color(0xF2DE5A, 1)
white = Color(0xFFFFFF, 1)

goldOutline = LineStyle(1,gold)
whiteOutline = LineStyle(1,white)

bigRectangle = RectangleAsset(600,300,goldOutline,gold)
eraseBig = RectangleAsset(300,100,whiteOutline,white)
eraseLittle = RectangleAsset(30,40,whiteOutline,white)

Sprite(bigRectangle)
Sprite(eraseBig, (150,0))
Sprite(eraseLittle, (30,0))
Sprite(eraseLittle, (90,0))


App().run()