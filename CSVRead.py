import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import time as timepack
from scipy import signal


start_time = timepack.time()
print("STATUS - Starting")


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


intermed_time = timepack.time()
print("STATUS - Data import successfull",round(intermed_time-start_time,2),"Seconds required")


"""RESULTANT VECTOR"""
r = (x**2+y**2+z**2)**0.5


print("STATUS - Resultant vector found",round(timepack.time()-intermed_time,2),"Seconds required")
intermed_time = timepack.time()

#Signal Conditioning
r_avg = np.average(r)
r = r-r_avg

r[abs(r) < 0.005] = 0     #Blocks noise at no signal

d_mat = np.array([])

def filtfunc(d):
    if d < 0.009:
        return False
    else:
        return True

r_filt = filter(filtfunc,r)

for d in r_filt:
    d_mat = np.append(d_mat,d)

d_mat_length = np.size(d_mat)

time_mat = np.array([])

for i in range(0,d_mat_length):
    value = d_mat.item(i)
    if value != r.item(i):
        "do nothing"
    elif value == r.item(i):
        print("I found a value")
        time_mat = np.append(time_mat,time.item(i))


print("STATUS - Filtering Complete",round(timepack.time()-intermed_time,2),"Seconds required")
intermed_time = timepack.time()


print("STATUS - Outputs")
print("Total Computation time",round(timepack.time()-start_time,2),"Seconds")
print("Data Points",np.size(time))


plt.subplot(2,1,1)
plt.plot(time,r)
plt.grid()


plt.subplot(2,1,2)
plt.plot(d_mat)
plt.show()






