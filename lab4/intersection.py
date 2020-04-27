''' intersection of a line x-x1/a1 = y-y1/b1 = z-z1/c1 with plane a2x+b2y+c2z+d = 0 =>
		x=x1-a1(a2x1+b2y1+c2z1+d)/(a1a2+b1b2+c1c2)
		y=y1-b1(a2x1+b2y1+c2z1+d)/(a1a2+b1b2+c1c2)
		z=z1-c1(a2x1+b2y1+c2z1+d)/(a1a2+b1b2+c1c2)
'''

def intersection(line, plane):
	# print(plane.a, plane.b, plane.c, plane.d)
	# print(line.a, line.b, line.c, line.x1, line.y1, line.z1)
	if((line.a*plane.a+line.b*plane.b+line.c*plane.c)==0):
		print("given line is parallel to given plane.")
		return
	# print(plane.a*line.x1+plane.b*line.y1+plane.c+line.z1+plane.d)
	# print(line.a*plane.a+line.b*plane.b+line.c*plane.c)
	# print(line.a)
	# print(line.x1)
	# print(line.b)
	# print(line.y1)
	# print(line.c)
	# print(line.z1)
	x = line.x1-line.a*(plane.a*line.x1+plane.b*line.y1+plane.c*line.z1+plane.d)/(line.a*plane.a+line.b*plane.b+line.c*plane.c)
	y = line.y1-line.b*(plane.a*line.x1+plane.b*line.y1+plane.c*line.z1+plane.d)/(line.a*plane.a+line.b*plane.b+line.c*plane.c)
	z = line.z1-line.c*(plane.a*line.x1+plane.b*line.y1+plane.c*line.z1+plane.d)/(line.a*plane.a+line.b*plane.b+line.c*plane.c)
	# print(x, y, z)
	return [x, y, z]
