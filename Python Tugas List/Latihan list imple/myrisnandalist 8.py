list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
list3 = list1 + list2
print(list3)


list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
list1.extend(list2)
print(list1)

list1.extend("slow")
print(list1)