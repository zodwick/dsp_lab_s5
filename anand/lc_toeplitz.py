import numpy as np

# Input the input sequence x[n] and impulse response h[n]
x = np.array(input("Enter the elements of the input sequence: ").split(","), dtype=int)
h = np.array(input("Enter the elements of the impulse response: ").split(","), dtype=int)
hn = h

row = len(x)
column = len(x) + len(h) - 1

if len(h) < column:
    z = np.zeros(column - len(h))
    h = np.concatenate((h, z))

# Toeplitz matrix
toeplitz = np.zeros((column, row))

for i in range(row):
    toeplitz[:, i] = np.roll(h, i)

print("Toeplitz Matrix:")
print(toeplitz)

# Convolution using the Toeplitz matrix
convolution_result = np.dot(toeplitz, x).astype(int)
print("The output sequence (using Toeplitz matrix) is:", convolution_result)

# Verifying the output
convolve_result = np.convolve(x, hn)
print("The output sequence (using numpy.convolve) is:", convolve_result)
