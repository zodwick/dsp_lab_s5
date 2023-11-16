import numpy as np
def overlap_save(x,h):
    N=len(x)+len(h)-1
    M=len(h)
    L=N-M+1
    x_pad=np.concatenate((x,np.zeros(N-1)))
    h_pad=np.concatenate((h,np.zeros(N-M)))
    y=np.zeros(N)
    for i in range(0,len(x),L):
        x_segment=x_pad[i:i+N]
        X=np.fft.fft(x_segment)
        H=np.fft.fft(h_pad)
        Y=X*H
        y_segment=np.real(np.fft.ifft(Y))
        y[i:i+N]+=y_segment
    return y
x=np.array(input("Enter the sequence of x1: ").split(",")).astype(int)
h=np.array(input("Enter the sequence of x2: ").split(",")).astype(int)
print(overlap_save(x,h))

