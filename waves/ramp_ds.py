import numpy as np
import matplotlib.pyplot as plt
t=np.arange(-21,21,1)
x=[]
for i in t:
    if i>=0:
        x.append(i)
    else:
        x.append(0)
plt.stem(t, x)
plt.xticks(x)
plt.show()