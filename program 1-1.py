import numpy as np
array=np.random.randint(1,20,(1,15))
print(array)
array=np.reshape(array,(3,5))
print(array)
for i in array:
    i[np.where(i==i.max())]=0
print(array)
