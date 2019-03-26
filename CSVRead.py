import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

"""DATA IMPORATION"""
data = genfromtxt('MondayTest.csv',delimiter=',')
time = data[:,0]
x = data[:,1]
y = data[:,2]
z = data[:,3]

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

#Loop Analysis
#Filtering
for i in range(0,np.size(time)):
    if abs(dev.item(i)) <= dev_avg or abs(r.item(i)- r_avg) <= 0.02 :
        R = np.append(R,r_avg)
        F = np.append(F,0)
    else:
        R = np.append(R,r.item(i))
        F = np.append(F,1)

for i in range(0,np.size(time)):
    if F.item(i) == 1:
        t_F = time.item(i)
        t_Fdel = t_F - t_Fprev
        t_F = t_Fprev
        T = np.append(T,t_Fdel)
    else:
        "w"


print("Data Points",np.size(time))
print("r_avg",r_avg)
print("dev_avg",dev_avg)

plt.plot(T)
plt.show()



