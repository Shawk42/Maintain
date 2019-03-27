import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import time as timepack

start_time = timepack.time()
print("STATUS - Starting")


"""DATA IMPORATION"""
data_1 = genfromtxt('AfternoonControl.csv',delimiter=',')
time_1 = data_1[:,0]
x_1 = data_1[:,1]
y_1 = data_1[:,2]
z_1 = data_1[:,3]

data_2 = genfromtxt('MondayTest.csv',delimiter=',')
time_2 = data_2[:,0]
x_2 = data_2[:,1]
y_2 = data_2[:,2]
z_2 = data_2[:,3]

#Data Joining
time = np.append(time_1,time_2)
x = np.append(x_1,x_2)
y = np.append(y_1,y_2)
z = np.append(z_1,z_2)

intermed_time = timepack.time()
print("STATUS - Data import successfull",round(intermed_time-start_time,2),"Seconds required")


"""RESULTANT VECTOR"""
r = (x**2+y**2+z**2)**0.5
r_avg = np.average(r)
dev = abs(r-r_avg)
dev_avg = np.average(dev)
R = np.array([])
F = np.array([])
t_F = 0
t_Fprev = 0
T = np.array([])

print("STATUS - Resultant vector found",round(timepack.time()-intermed_time,2),"Seconds required")
intermed_time = timepack.time()

#Loop Analysis
#Filtering
for i in range(0,np.size(time)):
    if False :
        R = np.append(R,r_avg)
        F = np.append(F,0)
    else:
        R = np.append(R,r.item(i))
        F = np.append(F,1)


print("STATUS - Filter Loop Complete",round(timepack.time()-intermed_time,2),"Seconds required")
intermed_time = timepack.time()

for i in range(0,np.size(time)):
    if F.item(i) == 1:
        t_F = time.item(i)
        t_Fdel = t_F - t_Fprev
        t_F = t_Fprev
        T = np.append(T,t_Fdel)
    else:
        "w"


print("STATUS - Error Frequency Loop Complete",round(timepack.time()-intermed_time,2),"Seconds required")
intermed_time = timepack.time()

print("STATUS - Outputs")
print("Total Computation time")
print("Data Points",np.size(time))
print("r_avg",r_avg)
print("dev_avg",dev_avg)

plt.plot(time,R)
plt.show()



