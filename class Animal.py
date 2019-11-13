class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
				self.sound =  sound
				self.name = name
				self.age = age
				self.favorite_color = favorite_color
	def eat(self):
			print( self.name + " Is eating pizza")
	def description(self):
			print(self.name + "is " + str(self.age) + " years old and loves the color "+self.favorite_color)
	def make_sound(self):
			print(self.sound + " Bark" + " Bark")
	        		


Dog1 = Animal("Bark","Sunny",16,"Yellow")
Dog1.eat()
Dog1.description()
Dog1.make_sound()

class Person(object):
 	"""docstring for person"""
 	def __init__(self,name,age,city,gender):
 		self.name = name
 		self.age = age 
 		self.city = city
 		self.gende = gender 
 	def eat(self):
 		print(self.name + " is eating his favorite breakfast ")
Person1 = Person("Mike",12,"jerusalem","male")
Person1.eat() 	
class Bird(object):
	def __init__(self,name,color,speed):
		self.name = name
		self.color = color
		self.speed = speed
	def speed_speed(self):
		print(str(self.name) + " is fast")
	def singing(self):
		print(str(self.name)+" is singing")	
Bird1 = Bird('bird',"orange","fast")
Bird1.speed_speed()	
Bird1.singing()

flower_song = (["roses are red", "violets are blue", "i wrote this song for you" ])
print(flower_song)