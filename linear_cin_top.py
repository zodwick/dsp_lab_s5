import numpy as np
x = np.array(input("Enter the elements of the input sequence:").split(",")).astype(int)
h = np.array(input("Enter the elements of the impulse response:").split(",")).astype(int)
hn = h

row = len(x)
column = len(x)+len(h)-1

if len(h)<column:
  z = np.zeros(column-len(h))
  h = np.concatenate((h,z))

#toeplitz matrix
tplz = h
print(tplz)
for i in range(row-1):
   h=np.roll(h,1)
   tplz=np.concatenate((tplz,h))

tplz.shape=(row,column)
tplz=np.transpose(tplz)
print(np.dot(tplz,x))

