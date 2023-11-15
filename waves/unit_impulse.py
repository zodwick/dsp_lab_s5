import numpy as np
import matplotlib.pyplot as plt
x= np.arange(-10,10,0.00001)
y=np.zeros(len(x))
y[np.isclose(x,0,atol=0.000001)]=1
plt.stem(x,y)
plt.show()