import numpy as np
x=np.array(input("enter the array").split(",")).astype(int)
N=int(input("enter the N-point:"))
z=np.zeros(N-len(x))
x=np.concatenate((x,z))
print(x)
y=np.zeros_like(x,dtype=complex)
for n in range (N):
  sum = 0
  for k in range (N):
    sum += x[k]*np.exp(complex(-1j)*2*np.pi*n*k*float(1/N))
  y[n] = sum
print(y.astype())


