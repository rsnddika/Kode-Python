class computer:
	def _init_(self):
		self.__prosesor = None
		self.__memory = None
		self.os = None
		self.keyboard = None
		self.mouse = None
	def __setPros(self,newPros):
		self.__prosesor = newPros
	def __setMemo(self,newMemo):
		self.__memory = newMemo
	def tampilData(self):
		print("Data PC: ")
		print("Prosesor: ",self.__prosesor)
		print("Memory: ",self.__memory)
		print("OS: ",self.os)
		print("Keyboard: ",self.keyboard)
		print("Mouse: ",self.mouse)
		print()

class modify:
	pc = computer()
	pc.tampilData()
	newPro = input("Prosesor: ")
	newMem = input("Memory: ")
	print()