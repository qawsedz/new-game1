import numpy as np
a1=np.array([[55,5],
             [0,3]])
print(np.where(a1[:,0]!=0,a1[:,0],3))