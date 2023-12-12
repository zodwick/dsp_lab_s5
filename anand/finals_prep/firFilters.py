# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal import firwin, lfilter, freqz

# # Filter specifications
# cutoff_freq = 0.1  # Normalized cutoff frequency (0.0 to 1.0)
# filter_order = 31  # Filter order

# # Generate Hamming window coefficients
# hamming_window = np.hamming(filter_order + 1)

# # Design the low pass filter using the Hamming window
# lpf_coeffs = firwin(filter_order, cutoff_freq, fs=1.0)

# # Frequency response of the filter
# w, h = freqz(lpf_coeffs, 1, worN=8000)
# plt.plot(0.5 * w / np.pi, np.abs(h), 'b')
# plt.title('Hamming Window Low Pass Filter Frequency Response')
# plt.xlabel('Frequency [Hz]')
# plt.ylabel('Gain')
# plt.grid()
# plt.show()

# # # Generate a test signal
# # fs = 1000  # Sampling frequency
# # t = np.arange(0, 1, 1/fs)
# # f_signal = 50  # Frequency of the input signal
# # input_signal = np.sin(2 * np.pi * f_signal * t)

# # # Apply the low pass filter to the input signal
# # filtered_signal = lfilter(lpf_coeffs, 1, input_signal)

# # # Plot the input and filtered signals
# # plt.figure(figsize=(10, 6))
# # plt.plot(t, input_signal, label='Input Signal')
# # plt.plot(t, filtered_signal, label='Filtered Signal')
# # plt.title('Input and Filtered Signals')
# # plt.xlabel('Time [s]')
# # plt.ylabel('Amplitude')
# # plt.legend()
# # plt.grid()
# # plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal import freqz

# # Filter specifications
# cutoff_freq = 0.1  # Normalized cutoff frequency (0.0 to 1.0)
# filter_order = 31  # Filter order

# # Manually calculate Hamming window coefficients
# hamming_window = 0.54 - 0.46 * np.cos(2 * np.pi * np.arange(filter_order + 1) / filter_order)

# plt.plot(hamming_window)
# plt.show()


# # Design the low pass filter using windowed sinc function
# n = np.arange(-filter_order // 2, filter_order // 2 + 1)
# lpf_coeffs = 2 * cutoff_freq * np.sinc(2 * cutoff_freq * n) * hamming_window

# # Normalize the filter coefficients
# lpf_coeffs /= np.sum(lpf_coeffs)

# # Frequency response of the filter
# w, h = freqz(lpf_coeffs, 1, worN=8000)
# plt.plot(0.5 * w / np.pi, np.abs(h), 'b')
# plt.title('Manually Designed Low Pass Filter Frequency Response')
# plt.xlabel('Frequency [Hz]')
# plt.ylabel('Gain')
# plt.grid()
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp


def triangular(n, N):
    x = np.empty(N)
    x[n < (N)//2] = 2*n[n < (N)//2]/(N-1)
    x[n >= (N)//2] = 2-2*n[n >= (N)//2]/(N-1)
    return x


def rectangular(n, N):
    x = np.ones(N)
    return x


def hanning(n, N):
    x = 0.5-0.5*np.cos(2*np.pi*n/(N-1))
    return x


def hamming(n, N):
    x = 0.54-0.46*np.cos(2*np.pi*n/(N-1))
    return x


def mfreq(b):
    w, h = sp.freqz(b, 1)
    db = 20*np.log10(abs(h))
    plt.subplot(2, 1, 1)
    plt.plot(w, db)
    # plt.subplot(2, 1, 2)
    # hphase = np.unwrap(np.arctan2(np.imag(h), np.real(h)))
    # plt.plot(w, hphase)
    plt.show()


def lpf(N, wc, win):
    a = (N-1)/2
    print(a)
    h = [wc/np.pi if i == a else np.sin(wc*(i-a))/((i-a)*np.pi)
         for i in np.arange(0, N)]

    # plt.plot(h)
    # plt.show()
    windows = [hanning, hamming, triangular, rectangular]
    h_ = h*windows[win-1](np.arange(0, N), N)

    mfreq(h_)


def hpf(N, wc, win):
    a = (N-1)/2
    h = [wc/np.pi if i == a else (np.sin((i-a)*np.pi)-np.sin((i-a)*wc))/(np.pi*(i-a)) for
         i in np.arange(0, N)]
    plt.plot(h)
    plt.show()
    # windows = [hanning, hamming, triangular, rectangular]
    # h_ = h*windows[win-1](np.arange(0, N), N)
    # mfreq(h_)


# N = int(input("Enter N: "))
# wc = float(input("Enter wc: "))
# win = int(
#     input("Choose window\n1. Hanning\n2. Hamming\n3.Triangular\n4.Rectangular\n"))
# # lpf(N, wc, win)
# hpf(N, wc, win)

for i in range(30, 35):
    hpf(i, 0.01, 1)

# for i in range(30, 35):
#     lpf(i, 0.01, 1)
