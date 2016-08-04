# Create a circle class
# create attributes for your circle -  radius, and pi
	#(think of which atrribute changes depending on circle)
  
# create a method to find the circumference of the circle
		#(circumference = 2 * pi * radius)
    # since we need the value of circumference return the circumference    
    	#(eg. return circumference)
      
# create a method to find the area of the circle
	#(area = pi * radius ** 2)
  # since we need the value of area return the area
  	
  
  
#create a new circle called big_circle with a radius of 10
#print the circumferene of big_circle
#print the area of big_circle


class circle(object):

	pi = 3.14

	def __init__(self, radius):
		self.radius = radius
	
	def circumference(self):
		circumference = 2 * self.pi * self.radius
		return circumference
	
	def area(self):
		area = self.pi * self.radius ** 2
		return area
 
circle1 = circle(5)
print(circle1.circumference())
print(circle1.area())
  