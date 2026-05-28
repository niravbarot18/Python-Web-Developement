mylist=[20,30,50,60,43,24,33,45]

print(mylist)
print(type(mylist))

#30
print(mylist[1])

#last data
print(mylist[-1])


floatlist=[1.13,5.23,4.25]
stringlist=["str1","str2","str3"]
mixedlist=["Nirav","nb@gmail.com",646165546,True,None]
nestedlist=[10,20,40,[50,60,30]]
print(nestedlist)
print(floatlist)
print(stringlist)

#slicing
print(mylist[0:4])

# INSERT
# 2 WAYS -- > insert() , append()

# insert -- > specific index -- > data add
mylist.insert(0,5)
print(mylist)

# append
mylist.append(10)
print(mylist)

# LAST DATA REMOVE
mylist.pop()
print(mylist)

#index vise remove
mylist.remove(10)
print(mylist)  