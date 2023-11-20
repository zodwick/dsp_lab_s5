import cmath
import numpy
def fft(x):
    N = len(x)
    
    if N <= 1:
        return x
    
    even = fft(x[0::2])
    odd = fft(x[1::2])
    
    T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
    
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]


def ifft(X):
    N = len(X)
    
    if N <= 1:
        return X
    
    even = ifft(X[0::2])
    odd = ifft(X[1::2])
    
    T = [cmath.exp(2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
    
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]


# Example usage:
if __name__ == "__main__":
    x = [0, 1, 2, 3, 4, 5, 6, 7]
    result = fft(x)
    print("FFT result:", result)
    print(numpy.fft.fft(x))
    result_ifft = ifft(result)
    print("IFFT result:", [elem / len(result) for elem in result_ifft])
