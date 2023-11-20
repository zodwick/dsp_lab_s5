import numpy as np
import scipy
import numpy as np

x = np.array(input("Enter values for x: ").split(",")).astype(int)
h = np.array(input("Enter values for h: ").split(",")).astype(int)

total = len(x) + len(h) - 1
y = np.zeros(total)

if len(x) < len(h):
    (x, h) = (h, x)

if len(x) != len(h):
    z = np.zeros(len(x) - len(h), dtype=int)
    h = np.concatenate((h, z))

for n in range(total):
    s = 0
    for k in range(len(x)):
        i = n - k
        if 0 <= i < len(x):
            s += x[k] * h[i]
    y[n] = s

print("Convolution result:", y)


print((np.convolve(x,h)))
print((scipy.signal.convolve(x,h)))