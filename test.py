import numpy as np
#toeplitz matrix
#input the input sequence x[n] and impulse response h[n]
x = np.array(input("Enter the elements of the input sequence:").split(",")).astype(int)
h = np.array(input("Enter the elements of the impulse response:").split(",")).astype(int)
hn = h

row = len(x)
column = len(x)+len(h)-1

if len(h)<column:
  z = np.zeros(column-len(h))
  h = np.concatenate((h,z))

#toeplitz matrix
toeplitz = h

for i in range (row-1):
  h = np.roll(h,1) #to cirular shift elements of array
  toeplitz = np.concatenate((toeplitz,h))



