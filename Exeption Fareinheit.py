#Penggunaan Assert.
def KelvinFarenheit(suhu):
	assert(suhu >= 0), "Lebih dingin dari nol mutlak!"
	# suhu terdingin/nol terjadi ketika terdapat suhu 0 derajat kelvin
	# dan tidak boleh ada suhu dibawah 0 derajat kelvin
	return (((suhu-273)*1.8)+32)

print (KelvinFarenheit(5),"Farenheit")
print (KelvinFarenheit(515),"Farenheit")
print (KelvinFarenheit(-5),"Farenheit")