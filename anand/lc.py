import numpy as np

def linear_convolution(x, h):
    # Length of the input and filter sequences
    len_x = len(x)
    len_h = len(h)

    # Length of the output sequence
    len_y = len_x + len_h - 1

    # Initialize the output sequence y
    y = np.zeros(len_y)

    # Perform linear convolution
    for i in range(len_y):
        for j in range(len_x):
            if i - j >= 0 and i - j < len_h:
                print(x[j], h[i-j],sep="*")
                y[i] += x[j] * h[i-j]
        print("....................")

    return y

# Example usage:
x = np.array([1, 2,3])
h = np.array([-1,-2,-3])
result = linear_convolution(x, h)

print("Input sequence x:", x)
print("Filter sequence h:", h)
print("Linear convolution result:", result)


print(np.convolve(x,h))