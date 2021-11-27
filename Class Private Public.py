class computer:

	def __init__(self):
		self.__prosesor = 'Intel Core i7-6700K'
		self.__memory = '16GB DDR4'
		self.os = 'Windows 10 Pro'
		self.keyboard = 'Razer'
		self.mouse = 'Logitech'

	def tampilData(self):
		print('Prosesor: ', self.__prosesor)
		print('Memory: ', self.__memory)
		print('OS: ', self.os)

ab = input("Prosesor: ")
cd = input("Memory: ")
ef = input("OS: ")
setattr(computer,'Prosesor',ab)
setattr(computer,'Memory',cd)
setattr(computer,'OS',ef)

print(getattr(computer,'Prosesor'))
print(getattr(computer,'Memory'))
print(getattr(computer,'OS'))
