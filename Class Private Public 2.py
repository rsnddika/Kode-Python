class computer :

	def _init_ (self):
		self.__prosesor = 'Intel Core i7 -6700K'
		self.__memory = '16GB DDR4'
		self.os = 'Windows 10 Pro'
		self.keyboard = 'Razer'
		self.mouse = 'Logitech'
		
	def tampilData(self):
		print('Prosesor : ',self.__prosesor)
		print('Memory :',self.__memory)
		print('OS : ',self.os)

ch = input("Prosesor :")
hp = input(" Memory :")
xi = input(" OS nya : ")
setattr(computer,'prosesor',ch)
setattr(computer,'Memory',hp)
setattr(computer,'OS',xi)

print(getattr(computer,'prosesor'))
print(getattr(computer,'Memory'))
print(getattr(computer,'OS'))