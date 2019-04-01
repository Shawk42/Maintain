import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import time as timepack
from scipy import signal

"""DATA IMPORATION"""
data_1 = genfromtxt('AfternoonControl.csv',delimiter=',')
time_1 = data_1[:,0]
x_1 = data_1[:,1]
y_1 = data_1[:,2]
z_1 = data_1[:,3]
time_1_max = np.max(time_1)

data_2 = genfromtxt('MondayTest.csv',delimiter=',')
time_2 = data_2[:,0]
x_2 = data_2[:,1]
y_2 = data_2[:,2]
z_2 = data_2[:,3]
time_2 = time_1_max+time_2

#Data Joining
time = np.append(time_1,time_2)
x = np.append(x_1,x_2)
y = np.append(y_1,y_2)
z = np.append(z_1,z_2)

#Sensor Calibration
x = -3.441+(7.026*x)
y = -3.072+(6.215*y)
z = -9.032+(15.963*z)

"""RAW DATA"""
r = (x**2+y**2+z**2)**0.5
r_prime = np.gradient(r)

#Signal Conditioning


R = r+r_prime



"""
error = 1-r
error[abs(error) < 0.025] = 0     #Blocks noise at no signal
r = error+1
"""
"""
error = 1-r
error[abs(error) < 0.025] = 0
r = r+error

r_prime = np.gradient(r)

error_prime = 1-r_prime
error_prime[abs(error_prime) < 0.01] = 0
r_prime = r_prime+error_prime
"""

#Graphing

plt.subplot(3,1,1)
plt.plot(time,r)
plt.title("Resultant gravity vector magnitude")
plt.ylabel("G")
plt.grid()

plt.subplot(3,1,2)
plt.plot(time,r_prime)
plt.title("r_prime")
plt.grid()

plt.subplot(3,1,3)
plt.plot(time,R)
plt.title("R score")
plt.grid()


plt.show()




