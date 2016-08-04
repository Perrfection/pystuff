import random
list5 = ['Birds chirping at noon', 'Forever after', 'Trees walking in light', 'Grass is always green', 'overwhelming love', 'Life in a nut shell', 'Walking past the moon', 'golden rays of sun']
list7 = ['Beyond the horizon lies', 'Will I ever have that thing?', 'Winter wanders wishfully', 'Glittering grasshoppers sprint', 'Life is totally awesome']
list5_length = len(list5)
list7_length = len(list7)
for x in range(4):
	random_index1 = random.randint(0, list5_length-1)
	random_index2 = random.randint(0, list7_length-1)
	random_index3 = random.randint(0, list5_length-1)
	print(list5[random_index1])
	print(list7[random_index2])
	print(list5[random_index3])
	print("\n")