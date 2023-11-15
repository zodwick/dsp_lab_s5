import numpy as np
import matplotlib.pyplot as plt
T = int(input("Enter the width: "))
t_lower = -(T/2)
t_upper = T/2
t = np.arange(-20,20,0.0001)
x = np.zeros_like(t,dtype=int)
x[(t >=t_lower) & (t<= t_upper) ] = 1
plt.plot(t, x)
plt.show()