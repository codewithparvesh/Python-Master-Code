import numpy as np
np_casualty =[[1,2],[2,3],[5,6]]

print(np_casualty)    
    
np_casualty = np.sum(np_casualty, axis=1)
print(np_casualty)
total_casualty = np.sum(np_casualty)
print(np_casualty)
print(int(total_casualty))