str=input().split()
n,m=int(str[0]),int(str[1])
b= input().split()
arr=[[b[m*i+j] for j in range(m)]for i in range(n)]