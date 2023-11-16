import numpy as np

def rolling(h,row,column):
    m=h
    for i in range(row-1):
        h=np.roll(h,1)
        m=np.concatenate((m,h))
    m.shape=(row,column)
    m=np.transpose(m)
    return m

x=np.array(input("enter x:").split(",")).astype(int)
h=np.array(input("enter x:").split(",")).astype(int)
hn=h
N=len(x)+len(h)-1
row=len(x)
column=N
z=np.zeros((N-len(h)))
h=np.concatenate((h,z))
print(np.convolve(x,hn))
h=rolling(h,row,column)
print(np.dot(h,x))