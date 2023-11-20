import numpy as np
import cmath

def fft(x):
    """
    Compute the Fast Fourier Transform (FFT) of a given sequence.

    Parameters:
    - x: Input sequence (NumPy array).

    Returns:
    - y: Output sequence (FFT of x).
    - twiddle: Twiddle matrix used in the computation.
    """
    k = len(x)
    # Twiddle matrix
    twiddle = np.ones(k, dtype="complex")
    for i in range(1, k):
        for j in range(k):
            num = np.exp(complex(-1j) * 2 * np.pi * i * j * float(1 / k))
            twiddle = np.append(twiddle, num)
    
    twiddle.shape = (k, k)

    # Output sequence
    y = np.dot(twiddle, x)

    return y, twiddle

# Example usage:
sequence_input = np.array(list(map(int, input("Enter the sequence:").split(","))))
output_sequence, twiddle_matrix = fft(sequence_input)


print("twiddle matrix:")
print(twiddle_matrix)

print("Output Sequence (FFT):")
print(output_sequence)



print(np.fft.fft(sequence_input))