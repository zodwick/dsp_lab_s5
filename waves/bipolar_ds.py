import numpy as np
import matplotlib.pyplot as plt
n = np.arange(-5,6,0.5)
x = np.zeros_like(n)
x[(n >= -3) & (n < 0) ] = -1
x[(n >= 0) & (n < 3) ] = 1
plt.stem(n, x)
plt.xticks(n)
plt.show()