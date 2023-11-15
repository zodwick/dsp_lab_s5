import numpy as np
import matplotlib.pyplot as plt
n = np.arange(-10,11,0.00001)
x = np.zeros_like(n)
x[(n >= -6) & (n < 0) ] = -1
x[(n >= 0) & (n <=6) ] = 1
plt.plot(n, x)
plt.xticks(n)
plt.show()