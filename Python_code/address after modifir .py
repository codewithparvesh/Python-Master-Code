#import ctypes
import ctypes

# variable declaration
val = 20

# display variable
print("Actual value -", val)

# get the memory address of the python object
# for variable
x = id(val)

# display memory address
print("Memory address - ", x)

# get the value through memory address
a = ctypes.cast(x, ctypes.py_object).value

# display
print("Value - ", a)



# variable declaration
val = val + 20

# display variable
print("Actual value after upgrde-", val)

# get the memory address of the python object
# for variable
y = id(val)

# display memory address
print("Memory address  after upgrade- ", y)

# get the value through memory address
b = ctypes.cast(y, ctypes.py_object).value

# display
print("Value - ", b)


print("----------------------------------")
print("address of x", x)
print("address of y", y)
print("Value at x", a)
print("address ay y", b)

a1 = ctypes.cast(x, ctypes.py_object).value
b1 = ctypes.cast(y, ctypes.py_object).value

print("Value at x", a1)
print("address ay y", b1)

print("-------------")

val2 = 20

# display variable
print("Actual value -", val2)

# get the memory address of the python object
# for variable
x3 = id(val2)

# display memory address
print("Memory address - ", x3)