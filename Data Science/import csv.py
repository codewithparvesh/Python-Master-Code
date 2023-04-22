import csv
import numpy as np


s =time.time()
with open( r"data set\terrorismData.csv", 'r', encoding = 'utf8') as f:
    data = csv.DictReader(f, skipinitialspace  = True)
    dl =list(data)
    arr=[]
    arr2=[]
    
    for row in dl:
        state=row['State']
        #print(state)
        if state== 'Jharkhand' or state == 'Odisha' or state == 'Andhra Pradesh' or state =='Chhattisgarh':
            #print(state)
            if row['Killed']:
                temp = row['Killed']
                temp = int(float(temp))
                arr.append(temp)
            if row['Wounded']:
                temp = row['Wounded']
                temp = int(float(temp))
                arr2.append(temp)

    arr = np.array(arr)
    arr2= np.array(arr2)
    ans = np.sum(arr) + np.sum(arr2)
    print(ans) 
e= time.time()
print(e-s)


# with open( r"data set/terrorismData.csv", 'r', encoding = 'utf8') as f:
#     data = csv.DictReader(f, skipinitialspace  = True)
#     dl =list(data)
    
#     cnt=0
#     for row in dl:
#         state=row['State']
#         #print(state)
#         ans=[]
#         if state== 'Jharkhand' or state == 'Odisha' or state == 'Andhra Pradesh' or state =='Chhattisgarh':
#             #print(state)
#             ans.append([row['Killed'],row['Wounded']])
#     ans = np.array(ans)
#     ans =ans[ans == ' '] = '0.0'
#     ans = np.array(ans, dtype = float)
#     print(ans)
#     ans = np.sum(ans, axis =1)
#     ans = np.sum(ans)
    
#     print(int(ans))
 
import time   

s =time.time()
with open( r"data set\terrorismData.csv", 'r', encoding = 'utf8') as f:
    data = csv.DictReader(f, skipinitialspace  = True)
    dl =list(data)
    arr=[]
    arr2=[]
    
    for row in dl:
        state=row['State']
        #print(state)
        if state== 'Jharkhand' or state == 'Odisha' or state == 'Andhra Pradesh' or state =='Chhattisgarh':
            #print(state)
            if row['Killed']:
                temp = row['Killed']
                temp = int(float(temp))
                arr.append(temp)
            if row['Wounded']:
                temp = row['Wounded']
                temp = int(float(temp))
                arr2.append(temp)

    arr = np.array(arr)
    arr2= np.array(arr2)
    ans = np.sum(arr) + np.sum(arr2)
    print(ans) 
e= time.time()
print(e-s)
    
s =time.time()
with open(r'data set/terrorismData.csv',encoding="utf8") as file_obj :
    data = csv.DictReader(file_obj,skipinitialspace=True)
    
    casualty = []
    for row in data:
        if row['State']=='Chhattisgarh' or row['State']=='Odisha' or row['State']=='Jharkhand' or row['State']=='Andhra Pradesh':
                casualty.append([row["Killed"],row["Wounded"]])

    np_casualty = np.array(casualty)
    
    np_casualty[np_casualty==''] = "0.0"
    np_casualty = np.array(np_casualty, dtype = float)
    
    np_casualty = np.sum(np_casualty, axis=1)
    total_casualty = np.sum(np_casualty)
    print(int(total_casualty))
e = time.time()
print(e-s)


s =time.time()
with open( r"data set\terrorismData.csv", 'r', encoding = 'utf8') as f:
    data = csv.DictReader(f, skipinitialspace  = True)
    dl =list(data)
    cnt=0
    for row in dl:
        state=row['State']
        #print(state)
        if state== 'Jharkhand' or state == 'Odisha' or state == 'Andhra Pradesh' or state =='Chhattisgarh':
            #print(state)
            if row['Killed']:
                temp = row['Killed']
                temp = int(float(temp))
                cnt+=temp
            if row['Wounded']:
                temp = row['Wounded']
                temp = int(float(temp))
                cnt+=temp
    print(cnt)
e= time.time()
print(e-s)
    
    

s =time.time()
with open( r"data set\terrorismData.csv", 'r', encoding = 'utf8') as f:
    data = csv.DictReader(f, skipinitialspace  = True)
    dl =list(data)
    arr=[]
    arr2=[]
    
    for row in dl:
        state=row['State']
        #print(state)
        if state== 'Jharkhand' or state == 'Odisha' or state == 'Andhra Pradesh' or state =='Chhattisgarh':
            #print(state)
            if row['Killed']:
                temp = row['Killed']
                temp = int(float(temp))
                arr.append(temp)
            if row['Wounded']:
                temp = row['Wounded']
                temp = int(float(temp))
                arr2.append(temp)

    arr = np.array(arr)
    arr2= np.array(arr2)
    ans = np.sum(arr) + np.sum(arr2)
    print(ans) 
e= time.time()
print(e-s)
