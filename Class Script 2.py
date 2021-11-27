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
 	def setOs(self,Os):
 		self.os = Os
 	def setKeyboard(self,Keyboard):
 		self.keyboard = Keyboard
 	def setMouse(self,Mouse):
 		self.mouse = Mouse
com1 = Computer()

print("-------------------------------------")
print("|         sebelum perubahan         |")
print("-------------------------------------")

#sebelum perubahan
com1.tampilData()

#proses perubahan
com1.setProsesor("Intel® Core™ i7-1165G7")
com1.setMemory("512 GB SSD")
com1.setOs("Windows 10")
com1.setKeyboard("Cooler")
com1.setMouse("Logitech MX Master 2S")

print("-------------------------------------")
print("|         setelah perubahan         |")
print("-------------------------------------")

#setelah perubahan
com1.tampilData()