class Computer:
 	def __init__(self):
 		self.__prosesor = "Intel Core i7-6700K"
 		self.__memory = "16GB DDR4"
 		self.os = "Windows 10 Pro"
 		self.keyboard = "Razer"
 		self.mouse = "Logitech"
 	def tampilData(self):
 		print("Prosesor: ", self.__prosesor)
 		print("Memory: ", self.__memory)
 		print("OS: ", self.os)
 		print("Keyboard:", self.keyboard)
 		print("Mouse:", self.mouse)
 		print()
 	def setProsesor(self,Prosesor):
 		self.__prosesor = Prosesor
 	def setMemory(self,Memory):
 		self.__memory = Memory
 		
com1 = Computer()

print("|         sebelum perubahan         |")

#sebelum perubahan
com1.tampilData()

#proses perubahan
com1.setProsesor("Intel® Core™ i7-1165G7")
com1.setMemory("512 GB SSD")
setattr(com1,"os"," Linux")
setattr(com1,"keyboard","Cooler Master")
setattr(com1,"mouse","Logitech Mx Master 2S")

print("|         setelah perubahan         |")

#setelah perubahan
com1.tampilData()