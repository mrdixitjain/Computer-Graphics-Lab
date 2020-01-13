from graphics import *

win = GraphWin("line", 1860, 1024)


def f(x, y):
	return dy*x-dx*y+dx*y1-dy*x1

def positiveSlopeLine(x1, y1, x2, y2, d):
	print('in positiveSlopeLine')
	print(dx, dy)
	x=x1
	y=y1
	while(x<=x2):
		pt=Point(x+930, 512-y)
		pt.draw(win)
		if(f(x+1, y+1/2)<0):
			x=x+1
			d+=dy
		else:
			d+=dy-dx
			x+=1
			y+=1

def negativeSlopeLine(x1, y1, x2, y2, d):
	x=x1
	y=y1
	while(x<=x2):
		pt=Point(x+930, 512-y)
		pt.draw(win)
		if(f(x+1, y-1/2)<0):
			x=x+1
			y=y-1
			d+=dy+dx
		else:
			d+=dy
			x+=1

def infiniteSlopeLine(x1, y1, x2, y2):
	x=x1
	y=y1
	if(y2<y1):
		x1, x2=x2, x1
		y1, y2=y2, y1
	while(y<=y2):
		pt=Point(x+930, 512-y)
		pt.draw(win)
		y+=1


infiniteSlopeLine(0, -930, 0, 930)

x=-930
y=0
while(x<=930):
	pt=Point(x+930, 512-y)
	pt.draw(win)
	x+=1

x1=int(input())
y1=int(input())
x2= int(input())
y2=int(input())#"enter y2: ""enter x2: ""enter y1: ""enter x1: "
if(x1>x2):
	x1, x2=x2, x1
	y1, y2=y2, y1
dx=x2-x1
dy=y2-y1
slope=0
d=2*dy-dx
if(dx!=0):
	slope=dy/dx
else:
	infiniteSlopeLine(x1, y1, x2, y2)
if(slope>=0):
	positiveSlopeLine(x1, y1, x2, y2, d)
else:
	negativeSlopeLine(x1, y1, x2, y2, d)



win.getMouse()
win.close()