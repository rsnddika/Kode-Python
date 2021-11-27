#if else
X = 5
print("Bilangan ganjil" if ((X%2)==1) else "Bilangan genap")

X = 2
print("Bilangan ganjil" if ((X%2)==1) else "Bilangan genap")


#turple
x=3
print(("Bilangan genap", "Bilangan ganjil")[((X%2)==1)])
x=6
print(("Bilangan genap", "Bilangan ganjil")[((X%2)==1)])

#dictionary
X = 3
print({True:"Bilangan ganjil", False:"Bilangan genap"}[((X%2)==1)])
X = 6
print({True:"Bilangan ganjil", False:"Bilangan genap"}[((X%2)==1)])

#lambda function
X = 3
print((lambda:"Bilangan genap", lambda:"Bilangan ganjil")[(X%2)==1]())
X = 6
print((lambda:"Bilangan genap", lambda:"Bilangan ganjil")[(X%2)==1]())