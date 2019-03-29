import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import time as timepack
from scipy import signal

data_1 = genfromtxt('MornNoise.csv',delimiter=',')
time_1 = data_1[:,0]
x_1 = data_1[:,1]
y_1 = data_1[:,2]
z_1 = data_1[:,3]

x = x_1
y = y_1
z = z_1

R = np.sqrt(x**2+y**2+z**2)

b,a = signal.butter(2,0.5,'low',analog= True)
#Y = signal.filtfilt(b,a,R)
Y = signal.lfilter(b,a,R)

print(Y)

plt.subplot(2,1,1)
plt.plot(time_1,R)
plt.title("Orginal")

plt.subplot(2,1,2)
plt.plot(time_1,Y)
plt.title("Filtered")

plt.show()

