from winSize import *
from graphics import *
from drawLine import *
from drawCircle import *
from drawEllipse import *
from drawPolygon import *
from windowToViewport import *
from fillColor import *


# print( " Enter window size im the following order (xmin , xmax , ymin , ymax) :-")
xmin , xmax , ymin , ymax = 0, 1000, 0, 900
window = size(xmin , xmax , ymin , ymax)

# print( " Enter viewport size in the following order (xmin , xmax , ymin , ymax) :-")
xvmin , xvmax , yvmin , yvmax = 0, 800, 0, 700
viewPort = size(0 , xvmax - xvmin, 0 , yvmax - yvmin)

win = GraphWin(' Line ' , xvmax - xvmin , yvmax - yvmin)
colors=[]
for i in range(xvmax-xvmin+10):
	colors.append([])
	for j in range(yvmax-yvmin+10):
		colors[i].append('w')
# print(colors[0])

drawLine(win, 0 , window.ymax, 0, window.ymin, 'blue', window,viewPort, colors )
drawLine(win, window.xmin , 0 , window.xmax, 0, 'red', window,viewPort, colors )
# print(colors)
# for i in colors:
# 	for j in i:
# 		if j=='b':
# 			print('yeah')
n=4
# print("Enter vertices of the edges as (x, y) one by one")
vertices=[[0, 0], [0, 200], [200, 200], [200, 0]]
# for i in range(n):
# 	vertices.append(list(map(int, input().split())))
color = 'black'

drawPolygon(win, n, vertices, color, window, viewPort, colors)
fillColor='yellow'
if(fillColor.lower()==color.lower()):
	print("sorry! same color as boundry color entered.")
	exit(0)
xv1,yv1 = windowToViewportPoint(100, 100, window,  viewPort)
fillColor4(win, xv1, yv1, fillColor, colors, window, viewPort, color)


print("Click on window to exit")


win.getMouse()
win.close 


