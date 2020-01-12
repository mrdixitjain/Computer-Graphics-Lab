from graphics import *

win = GraphWin("line", 2000, 1000)



x1=int(input())
y1=int(input())
x2= int(input())
y2=int(input())#"enter y2: ""enter x2: ""enter y1: ""enter x1: "
dx=x2-x1
dy=y2-y1
x=x1
y=y1
def f(x, y):
	return dy*x-dx*y+dx*y1-dy*x1
while(x<=x2):
	pt=Point(x, 999-y)
	pt.draw(win)
	if(f(x+1, y+1/2)<0):
		x=x+1
		d=dy
	else:
		d=dy-dx
		x+=1
		y+=1

win.getMouse()
win.close()


