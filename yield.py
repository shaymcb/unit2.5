#Shaylee McBride
#9Feb2018
#yield.py - displays yield sign

from ggame import *
from math import sqrt

white = Color(0xFFFFFF,1)
red = Color(0xFF0000,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)
noOutline = LineStyle(0,black)

redTriangle = PolygonAsset([(0,0),(400,0),(200,200*sqrt(3))],noOutline,red)
whiteTriangle1 = PolygonAsset([(0,20),(20,0),(400,0),(420,20),(210+10*sqrt(2),200*sqrt(3)+10),(210-10*sqrt(2),200*sqrt(3)+10)],blackOutline,white)
whiteTriangle2 = PolygonAsset([(0,0),(200,0),(100,100*sqrt(3))],noOutline,white)
text = TextAsset('YIELD',fill=red,style='bold 35pt Arial')

Sprite(whiteTriangle1)
Sprite(redTriangle,(10,10))
Sprite(whiteTriangle2,(110,2/3*100))
Sprite(text,(140, 2/3*100+10))
App().run()
