from math import *
from graphics import *
from graphicsCG import *


def choices():
    print("Enter your choice")
    print("1. Cabinet projection")
    print("2. Cavilier projection")
    print("3. Perspective Projection")
    print("4. Orthogonal Projection")
    print("5. Oblique Projection")
    print("6. Parallel Projection")
    print("7. Quit")

def multiply(matrix1, matrix2):
    rmatrix = [[0,  0,  0,  0],  [0,  0,  0,  0],  [0,  0,  0,  0],  [0,  0,  0,  0],  [0,  0,  0,  0],  [0,  0,  0,  0],  [0,  0,  0,  0],  [0,  0,  0,  0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                rmatrix[i][j] += matrix1[i][k] * matrix2[k][j]
    # print(matrix1)
    # print(matrix2)
    # print(rmatrix)
    for i in range(8):
        for j in range(4):
            rmatrix[i][j]=int(rmatrix[i][j]/rmatrix[i][3])
    return rmatrix

def printCube(win, ans):

    # drawing
    for i in range(4):
        drawLine(win, ans[i][0], ans[i][1], ans[(i+1)%4][0], ans[(i+1)%4][1], "red")
    for i in range(4):
        drawLine(win, ans[i+4][0], ans[i+4][1], ans[(i+1)%4+4][0], ans[(i+1)%4+4][1], "red")
    for i in range(4):
        drawLine(win, ans[i][0], ans[i][1], ans[(i)%4+4][0], ans[(i)%4+4][1], "red")

    time.sleep(6)

    # removing
    for i in range(4):
        drawLine(win, ans[i][0], ans[i][1], ans[(i+1)%4][0], ans[(i+1)%4][1], "white")
    for i in range(4):
        drawLine(win, ans[i+4][0], ans[i+4][1], ans[(i+1)%4+4][0], ans[(i+1)%4+4][1], "white")
    for i in range(4):
        drawLine(win, ans[i][0], ans[i][1], ans[(i)%4+4][0], ans[(i)%4+4][1], "white")   


def draw(win):
    cube=[]

    print("Enter the cube cordinates")
    for i in range(8):
        tlis=list(map(int, input().split()))
        tlis.append(1)
        cube.append(tlis)
    printCube(win, cube)

    while(True):
        choices()
        ans=[]
        choice=int(input())
        if choice==1:
            alpha=64
            print("Enter angle phi")
            phi=int(input())
            lone=float(1)/float(tan(radians(alpha)))
            promatrix=[[1, 0, 0, 0], [0, 1, 0, 0], [lone*(cos(radians(phi))), lone*(sin(radians(phi))), 0, 0], [0, 0, 0, 1]]
            # print(promatrix)
            ans=multiply(cube, promatrix)
        elif choice==2:
            alpha=45
            print("Enter angle phi")
            phi=int(input())
            lone=float(1)/float(tan(radians(alpha)))
            promatrix=[[1, 0, 0, 0], [0, 1, 0, 0], [lone*(cos(radians(phi))), lone*(sin(radians(phi))), 0, 0], [0, 0, 0, 1]]
            # print(promatrix)
            ans=multiply(cube, promatrix)
        elif choice==3:
            print("Enter COP")
            a, b, c = map(int, input().split())

            print("Enter the normal to plane")
            n1, n2, n3 = map(int, input().split())

            print("Enter the reference point to plane")
            x0, y0, z0 = map(int, input().split())

            d0=x0*n1+y0*n2+z0*n3
            d1=a*n1+b*n2+c*n3
            d=d0-d1

            promatrix=[[a*n1+d, b*n1, c*n1, n1], [a*n2, b*n2+d, c*n2, n2], [a*n3, b*n3, c*n3+d, n3], [-1*a*d0, -1*b*d0, -1*c*d0, -1*d1]]
            ans=multiply(cube, promatrix)
        elif choice==4:
            promatrix=[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
            ans=multiply(cube, promatrix)
        elif choice==5:
            print("Enter angle alpha")
            alpha=int(input())
            print("Enter angle phi")
            phi=int(input())
            lone=float(1)/float(tan(radians(alpha)))
            promatrix=[[1, 0, 0, 0], [0, 1, 0, 0], [lone*(cos(radians(phi))), lone*(sin(radians(phi))), 0, 0], [0, 0, 0, 1]]
            # print(promatrix)
            ans=multiply(cube, promatrix)
        elif choice==6:
            print("Enter line of projection a, b, c")
            a, b, c = map(int, input().split())

            print("Enter the normal to plane")
            n1, n2, n3 = map(int, input().split())

            print("Enter the reference point to plane")
            x0, y0, z0 = map(int, input().split())

            d0=x0*n1+y0*n2+z0*n3
            d1=a*n1+b*n2+c*n3
            d=d0-d1

            promatrix=[[-1*a*n1+d1, -1*b*n1, -1*c*n1, 0], [-1*a*n2, -1*b*n2+d1, -1*c*n2, 0], [-1*a*n3, -1*b*n3, -1*c*n3+d1, 0], [a*d0, b*d0, c*d0, d1]]
            ans=multiply(cube, promatrix)

        elif(choice==7):
            break  

        # print(ans)
        printCube(win, ans)

if __name__=="__main__":
    win=GraphWin("3D Transform", 1800, 1000)
    win.setCoords(-500, -500, 500, 500)
    win.setBackground("white")
    drawLine(win, -900, 0, 900, 0, "black")
    drawLine(win, 0, -500, 0, 500, "black")
    draw(win)
    win.getMouse()
    win.close()
