class Vehicle(object):
	""" A vehicle for sale  at the VehiclesDeralership"""

	base_sale_price = 0

	def __init__(self, wheels, miles, make, model, year, sold_on):
		"""Return a new vehicle object"""

		self.wheels = wheels
		self.miles = miles
		self.make = mamke
		self.model = model
		self.year = sold_on

	def sale_price(self):
		"""Return the sale price for this vehicles as a float amount."""
		if self.sold_on is not None:
			return 0.0 #alreay sold
		return 5000.0 * self.wheels

	def purchase_price(self):
		"""Retuen vehicle purchase price"""
		if self.sold_on is None:
			return 0.0 #not yet sold
		return self.base_sale_price - (.10 * self.miles)


class Car(Vehicle):

	def __init__(self, wheels, miles, make, model, year, sold_on):
		"""Return a new Car Object"""
		self.wheels = wheels
		self.miles = miles
		self.make = make
		self.model = model
		self.year = year
		self.sold_on = sold_on


class TrucK(Vehicle):

	def __init__(self, wheels, miles, make, model, year, sold_on):
		"""Return a new Truck Object"""
		self.wheels = wheels
		self.miles = miles
		self.make = make
		self.model = model
		self.year = year
		self.sold_on = sold_on
