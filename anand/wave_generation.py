import numpy as np
import matplotlib.pyplot as plt

# 1. Unit impulse signal

import numpy as np
import matplotlib.pyplot as plt

#discrete time

# t = np.arange(-5,5,1)
# x=np.zeros(len(t))
# x[len(t)//2]=1

# plt.stem(t,x)
# plt.show()

#continuous time

t = np.arange(-5,5,0.01)
x=np.zeros(len(t))
x[len(t)//2]=1
plt.plot(t,x)
plt.show()


# 2. Unit pulse signal
# 3. Unit ramp signal

# 4. Bipolar pulse
# 5. Triangular signal


