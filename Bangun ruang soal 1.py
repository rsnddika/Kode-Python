import math

class bangunRuang(object):
	"""docstring for bangunRuang"""
	def __init__(self):
		super(bangunRuang, self).__init__()
		self.nama = 'Bangun Ruang'
		self.luasa = None
		self.tinggi = None

	def volume(self, luasa, tinggi):
		self.volume = luasa*tinggi
		return self.volume

bR = bangunRuang()
print("Volume :", bR.volume(20,20))