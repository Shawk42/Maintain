#The intention of this code is to simuulate a signal from a production line sensor with random noise
#This version of the code is aimed to be more readable and have better ranges for acceptable values

import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

"""
PROBLEM STATEMENT
It has been determined that a piece of equipment vibrates during its normal operation. The following magnitude of the 
vibrations is below

0 = Machine is off [off]
0 to 3 = Machine is operating normally [normal] 
3 to 5 = Machine is operating poorly [caution]
5 to 7 = Machine is near failure       [warning]
7 to 10 = Machine failure is imminent [emergency]
"""

"""SIGNAL GENERATION"""
#Following lines generate a matrix to form as a random signal for more advanced signals a function outputting a matrix should be used

length = 100+1
rsig = rand.randint(-10,10,length)
t = np.linspace(0,length,length)

#Simple signal modifer
rsig = rsig*0.75

"""SIGNAL READING"""
fact = "null"
x = np.array([])

#Signal Interetation
off = 0
normal = 1
caution = 2
warning = 3
emergency = 4
headers = np.array(["Off","Normal","Warning","Emergency"])

for i in range(0,length):
    sig = rsig.item(i)
    if sig == 0:
        #print("Off")
        fact = off
        x = np.append(x, fact)
        #print(sig)
    elif sig >= -3 and sig <= 3:
        #print("Normal")
        fact = normal
        x = np.append(x, fact)
        #print(sig)
    elif sig > -5 and sig < 5:
        #print("Caution")
        fact = caution
        x = np.append(x, fact)
        #print(sig)
    elif sig > -7 and sig < 7:
        #print("Warning")
        fact = warning
        x = np.append(x, fact)
        #print(sig)
    elif sig <= -7 or sig >= 7:
        #print("Emergency")
        fact = emergency
        x = np.append(x, fact)
        #print(sig)
    else:
        print("No case")
        print(sig)

"""READING OUTPUT"""
state, count = np.unique(x,return_counts=True)


title = "null"
tit_mat = np.array([])
for i in range(0,np.size(state)):
    z = state.item(i)
    if z == 0:
        title = "Off"
        tit_mat = np.append(tit_mat,title)
    elif z == 1:
        title = "Normal"
        tit_mat = np.append(tit_mat, title)
    elif z == 2:
        title = "Caution"
        tit_mat = np.append(tit_mat, title)
    elif z == 3:
        title = "Warning"
        tit_mat = np.append(tit_mat, title)
    elif z == 4:
        title = "Emergency"
        tit_mat = np.append(tit_mat, title)

print(tit_mat)
print(state)
print(count)



plt.subplot(2,1,1)
plt.bar(tit_mat,count,align='center',alpha = 0.5)

plt.subplot(2,1,2)
plt.hlines(normal,0,t.item(length-1),color = "g")
plt.hlines(caution,0,t.item(length-1),color = "y")
plt.hlines(warning,0,t.item(length-1),color = "orange")
plt.hlines(emergency,0,t.item(length-1),color = "r")
plt.hlines(-normal,0,t.item(length-1),color = "g")
plt.hlines(-caution,0,t.item(length-1),color = "y")
plt.hlines(-warning,0,t.item(length-1),color = "orange")
plt.hlines(-emergency,0,t.item(length-1),color = "r")
plt.hlines(off,0,t.item(length-1),color = "black")
plt.plot(t,rsig,linewidth = 1,color = 'silver')
plt.xlabel("Time")
plt.ylabel("Amplitude")


plt.show()


