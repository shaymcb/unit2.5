#Shaylee McBride
#9Feb2018
#germany.py - displays german flag

from ggame import *

black = Color(0x000000,1)
red = Color(0xFF0000,1)
yellow = Color(0xFFFF00,1)

outline = LineStyle(0,black)

blackStripe = RectangleAsset(500,100,outline,black)
redStripe = RectangleAsset(500,100,outline,red)
yellowStripe = RectangleAsset(500,100,outline,yellow)
text = TextAsset("WILLKOMMEN IN DEUTSCHLAND",fill=black,style="bold 50pt Times",align='center')

Sprite(blackStripe)
Sprite(redStripe,(0,100))
Sprite(yellowStripe,(0,200))
Sprite(text,(0,300))
App().run()
