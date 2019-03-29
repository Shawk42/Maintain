#The intention of this code is to remeber how filters work

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


w = np.linspace(0.1,1,5)
print(w)
z = np.delete(w,3)
z = np.insert(z,3,50)
print(z)

w_sig = 10

x = np.linspace(0,25,1000)
y_sig = 1*np.cos((w_sig)*x)
y_sig = np.delete(y_sig,50)
y_sig = np.insert(y_sig,50,2)


b,a = signal.butter(4,0.5,'low',analog= True)
#Y = signal.filtfilt(b,a,y_sig)


plt.plot(x,y_sig)
plt.plot(x,Y)
plt.legend(("Orginal","Filtered"))
plt.show()