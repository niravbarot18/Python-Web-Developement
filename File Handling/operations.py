file1 =  open("bikes.txt","r").read()
print(file1)

file2 = open("bikes.txt","w")
file2.write("Honda SP 125")

file3=open("bikes.txt","r").read()
print(file3)

file4=open("bikes.txt","a")
file4.write("\nHero Splendor")

file5=open("bikes.txt","r").read()
print(file5)

#Starting add

file=open("bikes.txt","r")
data=file.read()
file.close()

file2=open("bikes.txt","w")
file2.write(f"GT\n{data}")

f1=open("cars.txt","r")
data=f1.read()
f1.close()

f2=open("cars.txt","r")
data2=f2.read()
f2.close()

print(data,"\n",data2)
