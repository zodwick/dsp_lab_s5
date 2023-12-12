import numpy as np
import matplotlib.pyplot as plt
import cmath
x=np.array(input("enter the array").split(",")).astype(int)
N=int(input("enter the N-point:"))
z=np.zeros(N-len(x))
x=np.concatenate((x,z))
print(x)
twiddle=np.ones(N,dtype=complex)
for n in range(1,N):
    for k in range(N):
        twi=np.exp(complex(-1j)*2*np.pi*float(1/N)*n*k)
        twiddle=np.append(twiddle,twi)
twiddle.shape=(N,N)
y=np.dot(twiddle,x)
#magnitude
plt.subplot(1,2,1)
x1=[abs(k) for k in y]
y1=np.arange(0,N,1)
plt.stem(y1,x1)
#phase
plt.subplot(1,2,2)
x2=[cmath.phase(k) for k in y]
y2=np.arange(0,N,1)
plt.stem(y2,x2)
plt.show()