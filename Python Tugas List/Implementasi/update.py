#update
a = {1,2,3,4,5}
b = {"grape", "orange", "apple"}
a.update(b)
print (a)

# dengan intersection
a = {1,2,3,4,5}
b = {4,5,6,7,8}
a &= (b)
print (a)

#  dengan  difference
a = {1,2,3,4,5}
b = {4,5,6,7,8}
a -= (b)
print (a)

# dengan symmetric difference
a = {1,2,3,4,5}
b = {4,5,6,7,8}
a ^= (b)
print (a)