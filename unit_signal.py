import numpy as np
import matplotlib.pyplot as plt

# Define the time range
t = np.linspace(-10, 10, 400)  # create 400 points between -10 and 10

# Create a continuous unit step function using the Heaviside function
unit_step = np.heaviside(t,1)
# Plot the continuous unit step function
plt.plot(t, unit_step)
plt.title('Continuous Unit Step Function')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
