# class Vehicle:
# 	def __init__(self,registration_number,car_colour):
# 		self.car_colour =  car_colour
# 		self.registration_number = registration_number

class Car:

	def __init__(self,registration_number,car_colour):
		self.registration_number = registration_number
		self.car_colour = car_colour

	def getType(self):
		return "Car"