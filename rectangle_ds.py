import numpy as np
import matplotlib.pyplot as plt
T = int(input("Enter the width: "))
t_lower = -(T/2)
t_upper = T/2
n = np.arange(-20,20,1)
x = np.zeros_like(n,dtype=int)
x[(n >=t_lower) & (n <= t_upper) ] = 1
plt.stem(n, x)
plt.xticks(n)
plt.show()