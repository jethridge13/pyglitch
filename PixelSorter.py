from PIL import Image

def pixelLine(img, x, y, direction, length, color):
	'''
	Generates a pixel sorted line starting at x and y
	and going for length in direction ('v' or 'h'
	for vertical or horizontal) of a single color
	img - the PIL Image object to edit
	x - the x coordinate to start drawing on
	y - the y coordinate to start drawing on
	direction - 'v' or 'h', draw vertical or horizontal
	length - number of pixels to draw for
	'''
	pixelMap = img.load()

	if direction == 'v':
		for i in range(y, y+length):
			pixelMap[x, i] = color
	elif direction == 'h':
		for i in range(x, x+length):
			pixelMap[i, y] = color

def pixelLineWithWidth(img, x, y, direction, length, color, width):
	'''
	Generates multiple pixel sorted lines starting at x and y
	and going for length in direction ('v' or 'h'
	for vertical or horizontal) of a single color
	img - the PIL Image object to edit
	x - the x coordinate to start drawing on
	y - the y coordinate to start drawing on
	direction - 'v' or 'h', draw vertical or horizontal
	length - number of pixels to draw for
	'''
	if direction == 'v':
		for i in range(x, x+width):
			pixelLine(img, i, y, direction, length, color)
	elif direction == 'h':
		for i in range(y, y+width):
			pixelLine(img, x, y, direction, length, color)
