import numpy as np
import matplotlib.pyplot as plt
f=int(input("enter the frequency:"))
t0=int(input("enter the shifting:"))
t=np.arange(0,5,0.0001)
T=np.arange(0+t0,1+t0,0.0001)
x=np.sin(2*np.pi*f*t)
y=np.sin(2*np.pi*f*T)
plt.plot(t,x)
plt.plot(T,y,"g")
plt.show()