import numpy as np


import numpy as np


def dit_fft(x):
    N = len(x)
    
    if N <= 1:
        return x
    
    even = dit_fft(x[0::2])
    odd = dit_fft(x[1::2])
    T = [np.exp(-2j * np.pi * k/N)*odd[k] for k in range(N//2)]
    return [even[k]+T[k] for k in range(N//2)] + [even[k]-T[k] for k in range(N//2)]


def dit_ifft(x):

    N = len(x)
    if N <= 1:
        return x
    even = dit_ifft(x[0::2])
    odd = dit_ifft(x[1::2])
    T = [np.exp(2j*np.pi*k/N)*odd[k]for k in range(N//2)]
    return [(even[k]+T[k])/2 for k in range(N//2)]+[(even[k]-T[k])/2 for k in range
                                                    (N//2)]



def dif_fft(x):
    N = len(x)
    if N <= 1:
        return x

    even = dif_fft(x[0::2])
    odd = dif_fft(x[1::2])
    T = [np.exp(-2j * np.pi * k/N)*even[k] for k in range(N//2)]
    return [odd[k]+T[k] for k in range(N//2)] + [odd[k]-T[k] for k in range(N//2)]

x = np.array(
    input("Enter the elements of the input sequence: ").split(","), dtype=int)

print(dit_fft(x))

print(dif_fft(x))
print(np.fft.fft(x))
