from winSize import *
from graphics import *
from drawLine import *
from drawCircle import *
from drawEllipse import *
from drawPolygon import *
from windowToViewport import *
from fillColor import *


# print( " Enter window size im the following order (xmin , xmax , ymin , ymax) :-")
xmin , xmax , ymin , ymax = map(int, input().split())
window = size(xmin , xmax , ymin , ymax)

# print( " Enter viewport size in the following order (xmin , xmax , ymin , ymax) :-")
xvmin , xvmax , yvmin , yvmax = map(int, input().split())
viewPort = size(0 , xvmax - xvmin, 0 , yvmax - yvmin)

win = GraphWin(' Line ' , xvmax - xvmin , yvmax - yvmin)
colors=[['w']*(xmax-xmin)]*(ymax-ymin+1)
# print(colors[0])

drawLine(win, 0 , window.ymax, 0, window.ymin, 'blue', window,viewPort, colors )
drawLine(win, window.xmin , 0 , window.xmax, 0, 'red', window,viewPort, colors )

n=int(input())
# print("Enter vertices of the edges as (x, y) one by one")
vertices=[]
for i in range(n):
	vertices.append(list(map(int, input().split())))
color = input()

drawPolygon(win, n, vertices, color, window, viewPort, colors)
fillColor=input()
if(fillColor.lower()==color.lower()):
	print("sorry! same color as boundry color entered.")
	exit(0)
xv1,yv1 = windowToViewportPoint(500, 50, window,  viewPort)
fillColor4(win, xv1, yv1, fillColor, colors, window, viewPort, color)


print("Click on window to exit")


win.getMouse()
win.close 


