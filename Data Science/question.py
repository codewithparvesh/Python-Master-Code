import numpy as np
import csv

with open(r'data set/terrorismData.csv',encoding="utf8") as file_obj :
    data = csv.DictReader(file_obj,skipinitialspace=True)
    
    days = []
    months = []
    year = []
    for row in data:
        print(row)
        days.append(row['Day'])
        months.append(row['Month'])
        year.append(row['Year'])
        
    np_day = np.array(days, dtype=float)
    np_month = np.array(months, dtype=float)
    np_year = np.array(year, dtype=float)
    
    
    np_day = np_day[np_month==1]
    
    np_year = np_year[np_month==1]
    np_day = np_day[np_year==2010]
    
    
    print(np_day)
    print(len(np_day))
    
    #Find the number of attack held between 1 Jan 2010 and 31 Jan 2010?(including both date).]
    
    # ans = np_day[((np_month == 1) & (np_year ==2010))]
    # print(ans)