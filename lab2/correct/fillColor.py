
from windowToViewport import *
def fillColor4(win, x, y, fillColor, colors, window, viewPort, boundaryColor):
	#tempx1, tempy1 = windowToViewportPoint(tempx , tempy, window,  viewPort)
	stack=[[x, y]]
	while(len(stack)>0):
		tempx, tempy=stack[-1][0], stack[-1][1]
		stack.pop()
		if(colors[tempx][tempy] != boundaryColor[0] and colors[tempx][tempy] != fillColor[0]):
			win.plotPixel(tempx, tempy, fillColor)
			colors[tempx][tempy]=fillColor[0]
			if(colors[tempx+1][tempy] != boundaryColor[0] and colors[tempx+1][tempy] != fillColor[0]):# and [tempx+1, tempy] not in stack):
				stack.append([tempx+1, tempy])
			if(colors[tempx][tempy+1] != boundaryColor[0] and colors[tempx][tempy+1] != fillColor[0]):# and [tempx, tempy+1] not in stack):
				stack.append([tempx, tempy+1])
			if(colors[tempx-1][tempy] != boundaryColor[0] and colors[tempx-1][tempy] != fillColor[0]):# and [tempx-1, tempy] not in stack):
				stack.append([tempx-1, tempy])
			if(colors[tempx][tempy-1] != boundaryColor[0] and colors[tempx][tempy-1] != fillColor[0]):# and [tempx, tempy-1] not in stack):
				stack.append([tempx, tempy-1])
			# if(colors[tempx+1][tempy+1] != boundaryColor[0] and colors[tempx+1][tempy+1] != fillColor[0]):# and [tempx+1, tempy] not in stack):
			# 	stack.append([tempx+1, tempy+1])
			# if(colors[tempx-1][tempy+1] != boundaryColor[0] and colors[tempx-1][tempy+1] != fillColor[0]):# and [tempx, tempy+1] not in stack):
			# 	stack.append([tempx-1, tempy+1])
			# if(colors[tempx-1][tempy-1] != boundaryColor[0] and colors[tempx-1][tempy-1] != fillColor[0]):# and [tempx-1, tempy] not in stack):
			# 	stack.append([tempx-1, tempy-1])
			# if(colors[tempx+1][tempy-1] != boundaryColor[0] and colors[tempx+1][tempy-1] != fillColor[0]):# and [tempx, tempy-1] not in stack):
			# 	stack.append([tempx+1, tempy-1])
