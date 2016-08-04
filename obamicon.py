from PIL import Image

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

im = Image.open("me2.jpg")
data= im.getdata()
data_list = list(data)
new_image = Image.new(im.mode, im.size)

def colorize(image_data):
	new_pic = []
	for pixel in image_data:
		red1 = pixel[0]
		green = pixel[1]
		blue = pixel[2]
		total = red1 + green + blue
		if total < 182:
			new_pic.append(darkBlue)
		elif total < 364:
			new_pic.append(red)
		elif total < 546:
			new_pic.append(lightBlue)
		else:
			new_pic.append(yellow)
	return new_pic
	
colors = colorize(data_list)
new_image.putdata(colors)
new_image.show()
new_image.save("output3.jpg", "jpeg")
