class Vehicle():
	name = ""
	kind=""
	color=""
	value=""

	def description(self):
		result = "%s is a %s %s worth $%.2f" %(self.name,self.kind,self.color,self.value)
		return result

car1 = Vehicle()
car1.name="Fer"
car1.kind="convertible"
car1.color="red"
car1.value=60000

car2 = Vehicle()
car2.name="Jump"
car2.kind="van"
car2.color="blue"
car2.value=10000

print(car1.description())
print(car2.description())

		