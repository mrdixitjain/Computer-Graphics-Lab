edgeTable={}
activeEdgeTuple=[]


def initEdgeTable():
	for i in range(yvmax-yvmin):
		edgeTable[i+yvmin]=[]

def removeEdgeByYmax(Tup, yy):
	i=0
	while(i<len(Tup)): 
		if (Tup[i][0] == yy): 
			print("Removed at "+str(yy))
			del Tup[i]
		else:
			i+=1


def storeEdgeInTuple(et, ymaxTS, xwithyminTS, minv):
	et.append([ymaxTS, xwithyminTS, minv])
	et.sort(reverse=true)

def storeEdgeInTable(x1, y1, x2, y2):
	m=0
	minv=0
	ymaxTS=0
	xwithyminTS=0
	scanline=0 #ts stands for to store 

	if (x2==x1):
		minv=0.000000
	else:
		m = ((float)(y2-y1))/((float)(x2-x1)) 
		
		# horizontal lines are not stored in edge table 
		if (y2==y1):
			return
			
			minv = (float)1.0/m
			printf("\nSlope string for %d %d & %d %d: %f",x1,y1,x2,y2,minv) 

			if (y1>y2): 
				scanline=y2 
				ymaxTS=y1 
				xwithyminTS=x2
			else:
				scanline=y1
				ymaxTS=y2
				xwithyminTS=x1
	# // the assignment part is done..now storage.. 
	storeEdgeInTuple(EdgeTable[scanline],ymaxTS,xwithyminTS,minv)


def scanLineFill():
	for i in range(yvmax-yvmin):
		for j in edgeTable[i]:
			storeEdgeInTuple(activeEdgeTuple, j[0], j[1], j[2])

		removeEdgeByYmax(activeEdgeTuple, i); 
		FillFlag = 0
		coordCount = 0
		x1 = 0
		x2 = 0
		ymax1 = 0
		ymax2 = 0
		while (j<len(ActiveEdgeTuple)):
			if (coordCount%2==0): 
				x1 = (int)(ActiveEdgeTuple.buckets[j].xofymin) 
				ymax1 = ActiveEdgeTuple.buckets[j].ymax 
				if (x1==x2): 

				# /* three cases can arrive- 
				# 	1. lines are towards top of the intersection 
				# 	2. lines are towards bottom 
				# 	3. one line is towards top and other is towards bottom 
				# */
					if (((x1==ymax1)&&(x2!=ymax2))||((x1!=ymax1)&&(x2==ymax2))):
						x2 = x1 
						ymax2 = ymax1 


					else:
						coordCount+=1 



				else:

					coordCount+=1 


			else:

				x2 = (int)ActiveEdgeTuple.buckets[j].xofymin 
				ymax2 = ActiveEdgeTuple.buckets[j].ymax 

				FillFlag = 0 

				// checking for intersection... 
				if (x1==x2) :

					# /*three cases can arive- 
					# 	1. lines are towards top of the intersection 
					# 	2. lines are towards bottom 
					# 	3. one line is towards top and other is towards bottom 
					# */
					if (((x1==ymax1)&&(x2!=ymax2))||((x1!=ymax1)&&(x2==ymax2))):					
						x1 = x2 
						ymax1 = ymax2 

					else:
						coordCount+=1 
						FillFlag = 1 


				else:
					coordCount+=1 
					FillFlag = 1 


