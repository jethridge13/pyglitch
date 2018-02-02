from PIL import Image
import PixelSorter


def test1():
	img = Image.new('RGBA', (250, 250), 'black')
	PixelSorter.pixelLine(img, 10, 10, 'v', 100, (255, 255, 255))
	PixelSorter.pixelLine(img, 11, 11, 'v', 100, (255, 255, 255))
	PixelSorter.pixelLine(img, 12, 12, 'v', 100, (255, 255, 255))
	PixelSorter.pixelLine(img, 13, 13, 'v', 100, (255, 255, 255))
	PixelSorter.pixelLine(img, 14, 14, 'v', 100, (255, 255, 255))
	PixelSorter.pixelLine(img, 15, 15, 'v', 100, (255, 255, 255))
	img.show()

def test2():
	img = Image.new('RGBA', (250, 250), 'black')
	PixelSorter.pixelLineWithWidth(img, 10, 10, 'v', 100, (255, 255, 255), 30)
	img.show()

if __name__ == '__main__':
	test2()
