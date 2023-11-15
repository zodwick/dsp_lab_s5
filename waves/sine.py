import numpy as np
import matplotlib.pyplot as plt
#sampling rate = sr
sr = 44100.0
# sampling interval = ts
ts = 1.0/sr
t = np.arange(0,1,ts)
# frequency of the signal
my_freq = float(input("Enter the frequency: "))
y = np.sin(2*np.pi*my_freq*2*t)
plt.title('frequency = '+str(my_freq)+ 'hz')
plt.plot(t, y, 'c')
plt.ylabel('Amplitude')
plt.xlabel('Time (sec)')
plt.show()