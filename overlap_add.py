import numpy as np
def overlap_add(x,h):
    N=len(x)+len(h)-1
    N_fft=2**(int(np.ceil(np.log2(N))))
    X=np.fft.fft(np.pad(x,(0,(N_fft-len(x)))))
    H=np.fft.fft(np.pad(h,(0,(N_fft-len(h)))))
    Y=X*H
    y=np.real(np.fft.ifft(Y))
    y=y[:N]
    return y


x=np.array(input("Enter the sequence of x1: ").split(",")).astype(int)
h=np.array(input("Enter the sequence of x1: ").split(",")).astype(int)
print(overlap_add(x,h))

