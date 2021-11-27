mydict = {"a": "alpha", "b": "beta", "o": "omega"}
print(dict["b"])

dict = {"a": "alpha", "b": "beta", "o": "omega"}
for data in dict:
	print(data)

dict = {"a": "alpha", "b": "beta", "o": "omega"}
for index, data in dict.items():
	print("index ke %s adalah %s"%(index,data))

dict = {"a": "alpha", "b": "beta", "o": "omega"}
for index in dict.keys():
	print("index ke %s"%(index))

dict = {“a”: “alpha”, “b”: “beta”, “o”: “omega”}
for data in dict.values():
	print("data %s"%(data))