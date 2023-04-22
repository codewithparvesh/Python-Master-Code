from traceback import print_tb


a = "python"
print(a)

a = """Python is very easy language,
we can easly learn this langua
"""
print(a)
b = "Python and modules"
print(b[5])
print(b[0:3])
print(b[0:])
print("-------------")
print(b[-3])
print(b[-5:-2])

print("-------------")
b = "Python and modules"
print(b.replace("P","J"))
print(b.replace("y","asdasd"))
print(b.upper())
print(b.lower())
print("-------------")
b = "       Python and modules      "
print(b)
#use to remove spaces
print(b.strip())

print("-------------")
a = "Hello"
b= "world"
print(a + " " + b)

age = 17


#b = " You are not eligibe for the voting beacuse you are ase is ", +age
#print(b)
# this will gave you error bcz you can not add int to sting
b = "You are not eligibe for the voting beacuse you are ase is {} ".format(age)
print(b)

salary = 60
milage = 80
b = "My age is {} and my profit is {}k and bike milage{})".format(age,salary,milage)
print(b)

salary = 60
milage = 80
b = "My age is {} and my profit is {}k and bike milage{})".format(age,salary,milage)
print(b)
print(" my name is ", age," old")

b = "python and moduel"
a=b.count("p")
print(a)