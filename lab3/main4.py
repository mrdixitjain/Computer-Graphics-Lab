from graphics import *
from graphicsCG import *
import math

def matMult(M, N):
	# print(M)
	# print(N)
	R=[]
	for i in range(len(M)):
		R.append([])
		for j in range(len(N[0])):
			R[i].append(0)
	for i in range(len(M)):
		for j in range(len(N[0])):
			for k in range(len(N)):
				R[i][j] += M[i][k] * N[k][j]
	for i in range(len(M)):
		for j in range(len(N)):
			M[i][j]=R[i][j]
	# print(M)
	return M[0]

def copyMetrics(M):
	a=[]
	for i in range(len(M)):
		a.append([])
		for j in M[i]:
			a[i].append(j)
		a[i].append(1)
	return a

def getKey():
	l=""
	key=win.getKey()
	while(key!='slash'):
		if(key=='period'):
			key='.'
		if(key=='minus'):
			key='-'
		l+=key
		print(l[-1], end="")
		key=win.getKey()
	print()
	return l


def choices():
	print("\nenter choice on window(enter '/' at the end).")
	print("select choice for transformation->")
	print("1. Translation")
	print("2. Scaling")
	print("3. Rotation")
	print("4. Shearing")
	print("5. Reflection")
	print("6. Quit")
	pass

if __name__=="__main__":	
	#print("enter xmin, ymin, xmax, ymax for window: ", end="")
	xmin , xmax , ymin , ymax = 0, 1000, 0, 900 #map(int, input().split())
	window = size(xmin , xmax , ymin , ymax)

	#print("enter xmin, ymin, xmax, ymax for viewPort: ", end="")
	xvmin , xvmax , yvmin , yvmax = 0, 800, 0, 700 #map(int, input().split())
	viewPort = size(0 , xvmax - xvmin, 0 , yvmax - yvmin)

	win = GraphWin(' Line ' , xvmax - xvmin , yvmax - yvmin, autoflush = False)

	drawLine(win, 0 , window.ymax, 0, window.ymin, 'blue', window,viewPort )
	drawLine(win, window.xmin , 0 , window.xmax, 0, 'red', window,viewPort )

	#print("Enter number of edges of polygon: ", end="")
	n=5#int(input())
	#print("Enter vertices of the edges as (x, y) one by one")
	vertices=[[200, 200], [500, 300], [700, 600], [400, 300], [200, 500]]#[]
	# for i in range(n):
		# vertices.append(list(map(int, input().split())))
	# print("Enter color of the Edges:- ", end="")
	color = 'black'#input()
	drawPolygon(win, n, vertices, color, window, viewPort)
	choices()
	while(1):

		choice=int(getKey())
		print(choice)

		if(choice==1): #translation

			print("enter Tx through window(enter '/' at the end)")
			Tx=float(getKey())
			print("enter Ty through window(enter '/' at the end)")
			Ty=float(getKey())

			T=[[1, 0, 0], [0, 1, 0], [Tx, Ty, 1]]
			k=copyMetrics(vertices)
			print(k)
			for i in k:
				i=matMult([i], T)[:2]
				i[0]=math.ceil(i[0])
				i[1]=math.ceil(i[1])
			print(k)
			print(vertices)
			drawPolygon(win, n, k, 'red', window, viewPort)

		elif(choice==2): #Scaling
			print("enter Sx through window(enter '/' at the end)")
			Sx=float(getKey())
			print("enter Sy through window(enter '/' at the end)")
			Sy=float(getKey())

			S=[[Sx, 0, 0], [0, Sy, 0], [0, 0, 1]]
			print("enter Reference point for rotation (x, y)")
			print("enter x through window(enter '/' at the end)")
			x=float(getKey())
			print("enter y through window(enter '/' at the end)")
			y=float(getKey())
			k=copyMetrics(vertices)
			print(k)
			for i in k:
				l=[i[0]-x, i[1]-y, i[2]]
				l=matMult([l], S)[:2]
				print(l)
				i[0]=x+l[0]
				i[1]=y+l[1]
				i=i[:2]
				i[0]=math.ceil(i[0])
				i[1]=math.ceil(i[1])
			print(k)
			print(vertices)
			drawPolygon(win, n, k, 'red', window, viewPort)

		elif(choice==3):
			print("enter t such that angle of rotation is pi/t: ")
			print("enter t through window(enter '/' at the end)")
			angle=math.pi/float(getKey())
			print("enter directon of rotation through window->")
			print("1. Anti Clockwise")
			print("2. Clockwise")
			k=int(win.getKey())
			if(k==2):
				angle=-angle
			R=[[math.cos(angle), math.sin(angle), 0], [-math.sin(angle), math.cos(angle), 0], [0, 0, 1]]
			print(R)
			print("Reference point for rotation (x, y): ", end=" ")
			x = float(getKey())
			y = float(getKey())
			k=copyMetrics(vertices)
			print(k)
			for i in k:
				l=[i[0]-x, i[1]-y, 1]
				l = matMult([l], R)
				print(l)
				i[0]=x+l[0]
				i[1]=y+l[1]
				i=i[:2]
				i[0]=math.ceil(i[0])
				i[1]=math.ceil(i[1])
			print(k)
			print(vertices)
			drawPolygon(win, n, k, 'red', window, viewPort)


		elif(choice==4):
			print("enter shx through window(enter '/' at the end)")
			shx = float(getKey())
			print("enter shy through window(enter '/' at the end)")
			shy = float(getKey())
			Sh = [[1, shy, 0], [shx, 1, 0], [0, 0, 1]]
			print("Reference point for rotation (x, y): ", end=" ")
			x = float(getKey())
			y = float(getKey())
			k=copyMetrics(vertices)
			print(k)
			for i in k:
				l=[i[0]-x, i[1]-y, i[2]]
				l=matMult([l], Sh)[:2]
				print(l)
				i[0]=x+l[0]
				i[1]=y+l[1]
				i=i[:2]
				i[0]=math.ceil(i[0])
				i[1]=math.ceil(i[1])
			print(k)
			print(vertices)
			drawPolygon(win, n, k, 'red', window, viewPort)

		elif(choice==5):
			print("enter a, b, c where ax+by+c=0 is reference line: ", end="")
			print("enter a through window(enter '/' at the end)")
			a = float(getKey())
			print("enter b through window(enter '/' at the end)")
			b = float(getKey())
			print("enter c through window(enter '/' at the end)")
			c = float(getKey())

			k=copyMetrics(vertices)

			Ref = [[(b*b-a*a)/(a*a+b*b), -2*a*b/(a*a+b*b), 0],
				 [-2*a*b/(a*a+b*b), (a*a-b*b)/(a*a+b*b), 0],
				 [-2*a*c/(a*a+b*b), -2*b*c, 1]]

			for i in k:
				x=i[0]
				y=i[1]
				l=[x, y, 1]
				# i[0]=((b*b-a*a)*x-2*a*b*y-2*a*c)/(a*a+b*b)
				# i[1]=((a*a-b*b)*y-2*a*b*x-2*b*c)/(a*a+b*b)
				l=matMult([l], Ref)[:2]
				print(l)
				i[0]=math.ceil(l[0])
				i[1]=math.ceil(l[1])
				i=i[:2]
			print(k)
			print(vertices)
			drawPolygon(win, n, k, 'red', window, viewPort)


		elif(choice==6):
			break

		else:
			pass
			print("please enter valid choice.")
		choices()



	print("Click on window to exit")

	win.getMouse()
	win.close 