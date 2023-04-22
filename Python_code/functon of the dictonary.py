a={1:2,3:4,"list":[1,23],"dict":{1:2}}
print(a)
#print(a[0]) give error bcz 0 in not in the key
print(a[1])
print(a["list"])
a.get(1)
a.get(45)
print(a.get(45)) # so 45 not in key so it return none but in case of [] it return error
print(a.get(45),'Not PRE')

print(a.keys())
print(a.items())

for i in a:
    print(i,a[i])
for i in a:
    print(i)

"list" in a # check or search in the keys

print("Adding and remove in the dicornat")

a['t']=(1,2,3)
print(a)
a[1]=10
print(a)
b={3:5,'the':4,2:100}
a.update(b)
print(a)
a.pop('t')
print(a)
del a[1]
print(a)
a.clear()
print(a)
del a
print("Set")
s = {1,2,3,5,4,2,3,1}
print(len(s),end= " ")
s.add(4)
s.add(3)
print(len(s))


