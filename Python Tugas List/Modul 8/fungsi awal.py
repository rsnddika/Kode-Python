def luas_lingkaran(jarijari):
    phi = 3.14
    luas = phi * (jarijari**2)
    return luas


def keliling_lingkaran(jarijari):
    phi = 3.14
    keliling = 2 * phi * jarijari
    return keliling


def hello_world():
    kata = "Hello World"
    return kata


print(hello_world())
print(luas_lingkaran(10))
print(keliling_lingkaran(10))
print(luas_lingkaran(6))
print(keliling_lingkaran(6))