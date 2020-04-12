from graphics import *

class size:
	def __init__(self,xmin ,xmax,ymin,ymax):
		self.xmin = xmin
		self.xmax = xmax
		self.ymin = ymin
		self.ymax = ymax

def windowToViewportPoint(x_w, y_w,window,viewPort):
	dx = (viewPort.xmax - viewPort.xmin )/(window.xmax - window.xmin)
	dy = (viewPort.ymax - viewPort.ymin )/(window.ymax - window.ymin)
	
	x_v = (x_w-window.xmin)*dx + viewPort.xmin
	
	y_v =  ( viewPort.ymax - (y_w - window.ymin )*dy )
	
	return (int(x_v),int(y_v))

def windowToViewportRadius(radius,window,viewPort):

	dx = (viewPort.xmax - viewPort.xmin )/(window.xmax - window.xmin)
	dy = (viewPort.ymax - viewPort.ymin )/(window.ymax - window.ymin)
	
	if( (viewPort.xmax - viewPort.xmin) < (viewPort.ymax - viewPort.ymin)):
		return int(radius * dx)
	else:
		return int(radius * dy)



def windowToViewportEllipse(rx,ry,window,viewPort):

	dx = (viewPort.xmax - viewPort.xmin )/(window.xmax - window.xmin)
	dy = (viewPort.ymax - viewPort.ymin )/(window.ymax - window.ymin)
	
	rx = dx * rx
	ry = dy * ry
	return (int(rx), int(ry))

def drawLineF(win,x1,y1,x2,y2,color):
	dx = x2 - x1
	dy = y2 - y1

	dx1 = abs(dx)
	dy1 = abs(dy)
	
	px = 2 * dy1 - dx1
	py = 2 * dx1 - dy1

	if (dy1 <= dx1) :
		if (dx >= 0):
			x = x1
			y = y1
			xe =x2
		else:
			x = x2
			y = y2
			xe =x1
		

		while(x<xe):
			win.plotPixel(x,y,color)
			x = x + 1
			if(px < 0):
				px = px + 2 * dy1
			else:
				if ((dx < 0 and dy < 0) or (dx > 0 and dy >0)):
					y = y+1
				else:
					y = y - 1
				px = px + 2 * (dy1 - dx1)
			
	else:
		if ( dy >= 0):
			x = x1
			y = y1
			ye = y2
		else:
			x = x2
			y = y2
			ye = y1
		

		while(y < ye):
			win.plotPixel(x,y,color)
			y = y + 1

			if (py <= 0):
				py = py + 2 * dx1
			else:
				if ((dx < 0 and dy < 0) or (dx > 0 and dy >0)):
					x = x + 1
				else:
					x = x - 1

				py = py + 2 * (dx1 - dy1)

def drawLine(win, xw1, yw1, xw2 , yw2, color):

	# xv1,yv1 = windowToViewportPoint(xw1 , yw1, window,  viewPort)
	# xv2,yv2 = windowToViewportPoint(xw2 , yw2, window,  viewPort)
	# print(xw1, yw1, xw2, yw2)
	xv1, yv1, xv2, yv2 = 900+xw1, 500-yw1, 900+xw2 , 500-yw2
	drawLineF(win, xv1, yv1, xv2, yv2, color)


def drawCircleF(win, xc, yc, rc, color):

	x = 0
	y = rc

	d = 5/4 - rc

	while(x<=y):
		win.plotPixel(xc + x,yc + y,color)
		win.plotPixel(xc + x,yc - y,color)
		win.plotPixel(xc - x,yc + y,color)
		win.plotPixel(xc - x,yc - y,color)

		win.plotPixel(xc + y,yc + x,color)
		win.plotPixel(xc + y,yc - x,color)
		win.plotPixel(xc - y,yc + x,color)
		win.plotPixel(xc - y,yc - x,color)
		x = x + 1
		if(d<0):
			d = d + 2 * x +3
		else:
			d = d + 2 * (x-y) +5
			y = y-1

def drawCircle(win, xw, yw, rw, color, window, viewPort):
	xv,yv = windowToViewportPoint(xw,yw,window,viewPort)
	rv = windowToViewportRadius(rw,window,viewPort)
	drawCircleF(win , xv, yv, rv, color)

def drawEllipseF(win,a,b,xc,yc,color):
	x = 0
	y = b

	d1 = (b * b) - (a * a * b) + (0.25 * a * a)
	dx = 2 * b * b * x
	dy = 2 * a * a * y

	while(dx < dy):
		win.plotPixel(xc + x,yc + y,color)
		win.plotPixel(xc + x,yc - y,color)
		win.plotPixel(xc - x,yc + y,color)
		win.plotPixel(xc - x,yc - y,color)
		
		x = x + 1
		dx = dx + (2 * b * b)

		if(d1 < 0):
			d1 = d1 + dx +(b * b)
		else:
			y = y - 1 
			dy = dy - (2 * a * a)
			d1 = d1 + dx - dy + (b * b)
	d2 = ((b * b) * ((x + 0.5) * (x + 0.5))) + ((a * a) * ((y - 1) * (y - 1))) - (a * a * b * b)

	while(y >= 0):
		win.plotPixel(xc + x,yc + y,color)
		win.plotPixel(xc + x,yc - y,color)
		win.plotPixel(xc - x,yc + y,color)
		win.plotPixel(xc - x,yc - y,color)
		y = y -1
		dy = dy - (2 * a * a)

		if(d2 > 0):
			d2 = d2 + (a * a) - dy
		else:
			x = x + 1 
			dx = dx + (2 * b * b)
			d2 = d2 + dx - dy + (a * a)

def drawEllipse(win , a , b, xw, yw, color, window, viewPort):
	xv, yv = windowToViewportPoint(xw, yw, window, viewPort)
	av, bv = windowToViewportEllipse(a, b, window, viewPort)
	drawEllipseF(win, av, bv, xv, yv, color)

def drawPolygon(win, n, vertices, window, viewPort):
	for i in range(n-1):
		xw1=vertices[i][0]
		yw1=vertices[i][1]
		xw2=vertices[i+1][0]
		yw2=vertices[i+1][1]
		drawLine(win , xw1, yw1, xw2 , yw2, "black", window, viewPort)
	xw1=vertices[n-1][0]
	yw1=vertices[n-1][1]
	xw2=vertices[0][0]
	yw2=vertices[0][1]
	drawLine(win , xw1, yw1, xw2, yw2, "black", window, viewPort)

	# scanFill(win, window, viewPort, vertices, color)