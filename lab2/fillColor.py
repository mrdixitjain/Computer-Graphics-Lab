def fillColor4(win, x, y, fillColor, colors, window, viewPort, boundaryColor):
	if(x<len(colors) and y<len(colors[0]) and x>=0 and y>=0):
		print(x, y)
		print(colors[x][y], boundaryColor[0], fillColor[0])
		if(colors[x][y] != boundaryColor[0] and colors[x][y] != fillColor[0]):
			win.plotPixel(x, y, fillColor)
			colors[x][y]=fillColor[0]
			fillColor4(win, x + 1, y, fillColor, colors, window, viewPort, boundaryColor) 
			fillColor4(win, x, y + 1, fillColor, colors, window, viewPort, boundaryColor) 
			fillColor4(win, x - 1, y, fillColor, colors, window, viewPort, boundaryColor) 
			fillColor4(win, x, y - 1, fillColor, colors, window, viewPort, boundaryColor)
		else:
			return
	else:
		return
