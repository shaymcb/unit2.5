#Shaylee McBride
#7Mar2018
#graphAPoint.py - version 2 because who knows where the first one went

from ggame import *

print('Input function')
function = input('y=')

x = -10
scale = 10

black = Color(0x000000,1)
white = Color(0xFFFFFF,1)
blackLine = LineStyle(2,black)

square = RectangleAsset(540,540,blackLine,white)
xAxis = LineAsset(540,0,blackLine)
yAxis = LineAsset(0,540,blackLine)
yTick = LineAsset(30,0,blackLine)
xTick = LineAsset(0,30,blackLine)
point = CircleAsset(3,blackLine,black)

Sprite(square)
Sprite(xAxis,(0,540/2))
Sprite(yAxis,(540/2,0))
for i in range(13):
    Sprite(yTick,(540/2-15,i*45))
    Sprite(xTick,(i*45,540/2-15))

while x<= 10:
    y = eval(function)
    print('('+str(x)+','+str(y)+')')
    Sprite(point,((270+(x*45),270-(y*45))))
    x = x + 0.5

App().run()
