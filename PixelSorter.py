from PIL import Image

# TODO For anything that takes direction, if it is not h or v, raise exception
# TODO Add assertions

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
	color - the RGB tuple that dictates the color

	Modifies the provided img, does not return a value
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
	color - the RGB tuple that dictates the color
	width - the width of the pixel line to draw

	Modifies the provided img, does not return a value
	'''
	if direction == 'v':
		for i in range(x, x+width):
			pixelLine(img, i, y, direction, length, color)
	elif direction == 'h':
		for i in range(y, y+width):
			pixelLine(img, x, y, direction, length, color)

def pixelLineWithGradient(img, x, y, direction, length, startingColor, endingColor):
	'''
	Generates a pixel line that follows a gradient starting
	at startingColor and ends at endingColor.
	img - the PIL Image object to edit
	x - the x coordinate to start drawing on
	y - the y coordinate to start drawing on
	direction - 'v' or 'h', draw vertical or horizontal
	length - number of pixels to draw for. If length 1, returns ending color
	startingColor - the color to start at the gradient
	endingColor - the color to end at the gradient

	Modifies the provided img, does not return a value
	'''
	assert type(length) == int
	
	if length == 1:
		pixelLine(img, x, y, direction, length, endingColor)
		return

	for i in range(length):
		val = i / length
		color = _getGradientColor(startingColor, endingColor, val)
		if direction == 'v':
			pixelLine(img, x, y+i, direction, 1, color)
		elif direction == 'h':
			pixelLine(img, x+i, y, direction, 1, color)

def _getGradientColor(start, end, val):
	'''
	Generates a gradient color between the two based on
	float value val.
	start - the beginning color tuple
	end - the ending color tuple
	val - the float val calculate the gradient with

	Returns a new color tuple
	'''
	color = [0, 0, 0]
	for i in range(len(color)):
		color[i] = int(start[i] + val * (end[i] - start[i]))
	return tuple(color)
