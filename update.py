a = {1,2,3,4,5}
b = {"grap", "orange", "apple"}
a.update(b)
print(a)


a = {1,2,3,4,5}
b = {4,5,6,7,8}
a &= (b)
print(a)


a = {1,2,3,4,5}
b = {4,5,6,7,8}
a -= (b)
print(a)


a = {1,2,3,4,5}
b = {4,5,6,7,8}
a ^= (b)
print(a)