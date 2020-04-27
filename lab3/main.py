from graphics import *
from graphicsCG import *
import math

def matMult(M, N):
	# # print(M)
	# # print(N)
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
	# # print(M)
	return M[0]

def copyMetrics(M):
	a=[]
	for i in range(len(M)):
		a.append([])
		for j in M[i]:
			a[i].append(j)
	return a


def choices():
	# print("select choice for transformation->")
	# print("1. Translation")
	# print("2. Scaling")
	# print("3. Rotation")
	# print("4. Quit")
	pass

if __name__=="__main__":	
	# print("enter xmin, ymin, xmax, ymax for window: ", end="")
	xmin , xmax , ymin , ymax = map(int, input().split())
	window = size(xmin , xmax , ymin , ymax)

	# print("enter xmin, ymin, xmax, ymax for viewPort: ", end="")
	xvmin , xvmax , yvmin , yvmax = map(int, input().split())
	viewPort = size(0 , xvmax - xvmin, 0 , yvmax - yvmin)

	win = GraphWin(' Line ' , xvmax - xvmin , yvmax - yvmin, autoflush = False)

	drawLine(win, 0 , window.ymax, 0, window.ymin, 'blue', window,viewPort )
	drawLine(win, window.xmin , 0 , window.xmax, 0, 'red', window,viewPort )

	# print("Enter number of edges of polygon: ", end="")
	n=int(input())
	# print("Enter vertices of the edges as (x, y) one by one")
	vertices=[]
	for i in range(n):
		vertices.append(list(map(int, input().split())))
	# print("Enter color of the Edges:- ", end="")
	color = input()
	drawPolygon(win, n, vertices, color, window, viewPort)
	choices()
	while(1):

		choice=int(input())

		if(choice==1): #translation
			# print("enter Tx: ", end="")
			Tx=float(input())
			# print("enter Ty: ", end="")
			Ty=float(input())
			k=copyMetrics(vertices)
			print(k)
			for i in k:
				i[0]+=Tx
				i[0]=math.ceil(i[0])
				i[1]+=Ty
				i[1]=math.ceil(i[1])
			print(k)
			print(vertices)
			drawPolygon(win, n, k, 'red', window, viewPort)

		elif(choice==2): #Scaling
			# print("enter Sx: ", end="")
			Sx=float(input())
			# print("enter Sy: ", end="")
			Sy=float(input())
			# print("Reference point for rotation (x, y): ", end=" ")
			x, y = map(int, input().split())
			k=copyMetrics(vertices)
			print(k)
			for i in k:
				i[0]-=x
				i[0]*=Sx
				i[0]+=x
				i[1]-=y
				i[1]*=Sy
				i[1]+=y
				i[0]=math.ceil(i[0])
				i[1]=math.ceil(i[1])
			print(k)
			print(vertices)
			drawPolygon(win, n, k, 'red', window, viewPort)

		elif(choice==3):
			# print("enter angle of rotation: ", end="")
			angle=float(input())
			# print("enter directon of rotation->")
			# print("1. Anti Clockwise")
			# print("2. Clockwise")
			k=int(input())
			if(k==2):
				angle=-angle
			array=[[math.cos(angle), math.sin(angle)], [-math.sin(angle), math.cos(angle)]]
			# print("Reference point for rotation (x, y): ", end=" ")
			x, y = map(int, input().split())
			k=copyMetrics(vertices)
			print(k)
			for i in k:
				l=[i[0]-x, i[1]-y]
				l = matMult([l], array)
				i[0]=x+l[0]
				i[1]=y+l[1]
				i[0]=math.ceil(i[0])
				i[1]=math.ceil(i[1])
			print(k)
			print(vertices)
			drawPolygon(win, n, k, 'red', window, viewPort)


		elif(choice==4):
			# print("enter shx: ", end="")
			shx=float(input())

			# print("enter shy: ", end="")
			shy=float(input())
			# print("Reference point for rotation (x, y): ", end=" ")
			x, y = map(int, input().split())




		elif(choice==4):
			break

		else:
			pass
			# print("please enter valid choice.")
		choices()



	# print("Click on window to exit")


	win.getMouse()
	win.close 