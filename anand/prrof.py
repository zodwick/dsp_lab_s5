import numpy as np

# Define two signals
signal1 = np.array([1, 2, 3])
signal2 = np.array([4, 5, 6])

# Perform convolution in the time domain
convolution_result = np.convolve(signal1, signal2, mode='full')

# Compute the Fourier Transforms
fft_result1 = np.fft.fft(signal1, len(convolution_result))
fft_result2 = np.fft.fft(signal2, len(convolution_result))

# Multiply the Fourier Transforms
multiplication_result = fft_result1 * fft_result2

# Inverse Fourier Transform to obtain the time-domain result
inverse_fft_result = np.fft.ifft(multiplication_result)

# Print the results
print("Left-hand side (LHS) - Convolution Result (Time Domain):")
print(convolution_result)

print("\nRight-hand side (RHS) - Inverse Fourier Transform (Frequency Domain):")
print(np.real(inverse_fft_result))
