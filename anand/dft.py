import numpy as np


x=np.array(input("Enter the elements of the input sequence: ").split(","),dtype=int)

def dft(x):
    N=len(x)
    y= np.zeros(N,dtype=complex)
    
    for  k in range(N):
        for n in range(N):
            y[k]+=x[n]*np.exp(-2j*np.pi*k*n/N)
            
    return y


time = np.arange(0,len(x),1)

import matplotlib.pyplot as plt
plt.stem(time,[abs(i) for i in dft(x)])
plt.show()