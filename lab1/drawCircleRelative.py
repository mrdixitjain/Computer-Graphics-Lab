from graphics import *

win = GraphWin("line", 1860, 1024)


def f(x, y):
	return (x-x1)*(x-x1)+(y-y1)*(y-y1)-r*r

def infiniteSlopeLine(x1, y1, x2, y2):
	x=x1
	y=y1
	if(y2<y1):
		x1, x2=x2, x1
		y1, y2=y2, y1
	while(y<=y2):
		win.plotPixel(x+930, 512-y, 'orange')
		y+=1

def drawCircle(x1, y1, r):
	xp, yp= 0, r
	while(xp<=yp):
		win.plotPixel(xp+930+x1, 512-yp+y1, 'black')
		win.plotPixel(yp+930+x1, 512-xp+y1, 'black')
		
		win.plotPixel(xp+930+x1, 512-(-yp)+y1, 'black')
		win.plotPixel(yp+930+x1, 512-(-xp)+y1, 'black')
		
		win.plotPixel(-xp+930+x1, 512-yp+y1, 'black')
		win.plotPixel(-yp+930+x1, 512-xp+y1, 'black')

		win.plotPixel(-xp+930+x1, 512-(-yp)+y1, 'black')
		win.plotPixel(-yp+930+x1, 512-(-xp)+y1, 'black')

		if(f(xp+1+x1, yp-1/2+y1)<0):
			xp+=1
		else:
			xp+=1
			yp-=1

r=50
infiniteSlopeLine(0, -930, 0, 930)

x=-930
y=0
while(x<=930):
	win.plotPixel(x+930, 512-y, 'orange')
	x+=1
x1=10
y1=10
drawCircle(50, 50, 100)
win.getMouse()
win.close()
		
