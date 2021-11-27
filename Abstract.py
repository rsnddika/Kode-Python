from abc import ABC, abstractmethod

class AbstractClassExample(ABC):
	def __init__(self, value):
		self.value = value
		super().__init__()

class tambah42(AbstractClassExample):
	def do_something(self):
		return self.value + 42

class kali42(AbstractClassExample):
	def do_something(self):
		return self.value * 42

x = tambah42(10)
print(x.do_something())