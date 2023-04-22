import csv
import numpy as np
import pandas as pd
with open(r"C:\Users\dc\Downloads\android_version_historty.csv", 'r', encoding='utf8') as file:
    data = csv.reader(file)
    dl = list(data)

    print(dl[5][1])
    print(len(dl))
    print(type(dl[6]))
    for i in range(len(dl)-1):
        print(dl[i][5])
        if dl[i][5]=="Old version":
            dl[i][5]=" "
        temp = dl[i][6]
        temp= temp.split(': ')[-1]
        dl[i][6]=temp
        
        
    
    data =pd.DataFrame(dl)

    data.to_excel(r'D:\Coding\Data Science/new.xlsx', index = False)
  