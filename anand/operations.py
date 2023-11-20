import numpy as np
import matplotlib.pyplot as plt

x = np.array((input("Enter values for x: ").split(","))).astype(int)
t0 = eval(input("enter shift factor"))

t = np.linspace(min(0, t0-1),max(t0+1, len(x)),len(x))

print(x)


plt.plot(t,x,'b',linewidth=2, label='original signal')
plt.plot(t+t0,x,'r',linewidth=2, label='shifted signal')
plt.legend()
plt.grid()
plt.show()