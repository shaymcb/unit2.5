#Shaylee McBride
#7Feb2018
#graphicsDemo.py - intro to ggame

from ggame import *

red = Color(0xFF0000, 1) #hex code, opacity
green = Color(0x00FF00, 1)
blue = Color(0x0000FF, 1)
black = Color(0x000000, 1)

blackOutline = LineStyle(2,black) #first number is how many pixels wide

redRectangle = RectangleAsset(200,100,blackOutline,red) #width, height, outline, fill color
blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, fill
greenEllipse = EllipseAsset(50,100,blackOutline,green) #width, height, outline, fill
blackLine = LineAsset(50,160,blackOutline) #x_endpoint,y_endpoint,linestyle (starts from origin)
redTriangle = PolygonAsset([(0,0),(120,180),(60,300)],blackOutline,red) #endpoints, outline, fill
text = TextAsset('whaddup',fill=green,style='bold 40pt Times') #can do whatever, just say what it is

Sprite(redRectangle)
Sprite(greenEllipse,(0,100))
Sprite(blackLine,(120,120))
Sprite(blueCircle,(50,50)) #how many over, how many down
Sprite(text,(300,200))
Sprite(redTriangle,(200,0))

App().run()
