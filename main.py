from PIL import Image
import PixelSorter

def image1():
	import random
	img = Image.new('RGBA', (250, 250), 'black')
	height = 50
	startColor = (128, 9, 9)
	endColor = (253, 207, 88)
	for i in range(250):
		randomFloat = random.random()
		randomInt = random.randint(0, 250 - height)
		height = 75 + int(randomFloat * randomInt)
		if height > 250:
			height = 250
		PixelSorter.pixelLineWithGradient(img, i, 250 - height, 'v', height, startColor, endColor)
	img.show()

if __name__ == '__main__':
	image1()
