#The intention of this code is to remeber how filters work

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

w_sig = 10

x = np.linspace(0,25,1000)
y_sig = 5+(1*np.cos((w_sig)*x))+(0.5*np.cos((w_sig*10)*x))

b,a = signal.butter(1,0.4,'low',analog= True)
Y = signal.filtfilt(b,a,y_sig)



plt.plot(x,y_sig)
plt.plot(x,Y)
plt.show()