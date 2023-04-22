import  os

li=[[1,2,3],[4,5,6],[7,8,9]]
n,m=3,3
print(len(li))
size=li.size()
print(size)
print("Start here")
for i in range(n):
    for j in range(m):
        print(li[i][j],end=" ")
    print()
# what id jag list
print(" 2nd list o/p")
li=[[1,2,3],[4,1],[7,8,9,10]]
for i in li:
    for j in i:
        print(j,end=" ")
    print()

# join in string
#contentation of two string possible but string and list is not possible
print('ab'.join('asd'))
print("ab".join(['1','2','3']))

# use
for i in li:
    output=" ".join([str(ele) for ele in i])
    print(output)